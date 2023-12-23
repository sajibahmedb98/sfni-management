from fastapi import APIRouter

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
)


@router.post("/")
def create_employee():
    return {"message": "Employee created"}

@router.get("/")
def get_employee():
    return {"message": "Employee retrieved"}
