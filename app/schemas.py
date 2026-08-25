from pydantic import BaseModel, EmailStr


# =========================
# Authentication Schemas
# =========================

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# =========================
# Job Schemas
# =========================

class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    company: str


class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    company: str
    is_active: bool
    recruiter_id: int

    model_config = {
        "from_attributes": True
    }