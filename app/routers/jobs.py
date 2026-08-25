from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db, require_role
from app.models import Job, User
from app.schemas import JobCreate, JobResponse


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED
)
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("recruiter"))
):
    new_job = Job(
        title=job_data.title,
        description=job_data.description,
        location=job_data.location,
        company=job_data.company,
        recruiter_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


@router.get(
    "",
    response_model=list[JobResponse]
)
def get_jobs(
    db: Session = Depends(get_db)
):
    return (
        db.query(Job)
        .filter(Job.is_active == True)
        .all()
    )


@router.get(
    "/{job_id}",
    response_model=JobResponse
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    return job