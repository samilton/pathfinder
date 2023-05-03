from fastapi import APIRouter, HTTPException, Depends
from app.dependencies.lease_manager import get_lease_manager

router = APIRouter(
    prefix="/tokens",
    tags=["tokens"],
    responses={404: {"description": "Not Found"}},
    dependencies=[Depends(get_lease_manager)]
)

fake_keys = ["abc", "123", "def"]


@router.get("/{hostname}")
async def get_token(hostname: str):
    """
    Get Token will take a hostname and return a valid API token

    params: hostname
    returns: API token
    """

    if hostname == "":
        raise HTTPException(status_code=400, detail="No Hostname provided")

    get_lease_manager().renew("abc")
    return "abc"
