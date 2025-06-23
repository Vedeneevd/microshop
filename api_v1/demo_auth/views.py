from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix='/demo_auth', tags=['Demo-auth'])

security = HTTPBasic()

@router.get("/basic-auth")
def demo_basic_auth_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {'message': 'Hi',
            'username': credentials.username,
            'password': credentials.password}

