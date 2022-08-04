from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..schemas.base import BaseResponseSchema
from ..schemas.user_auth import UserLoginResponse, UserPasswordLoginRequest
from ...domain.usecases import GetUserUseCase, LoginWithPasswordUseCase
from ...domain.entities import User

router = APIRouter()


@router.get('/{id}')
async def get_user_by_id(id: str,
                         get_user_by_id_usecase: GetUserUseCase = Depends(GetUserUseCase)):
    result = await get_user_by_id_usecase.execute(id)
    return result


@router.post("/login",
             name="Login with password",
             description='Login with password',
             response_model=UserLoginResponse,
             responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
             })
async def login_w_password(data: UserPasswordLoginRequest,
                           login_w_password_usecase: LoginWithPasswordUseCase=Depends(lambda: LoginWithPasswordUseCase())):
    user, token, failure = await login_w_password_usecase.execute(data.email, data.password)
    if failure is not None:
        return JSONResponse(
            status_code=failure.code,
            content={'status': 'unauthorized', 'message': "Incorrect username or password"})
    return {
        'status': 'success',
        'message': '',
        'data': {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone_number
        }
    }

@router.post("/register",
             name="Register",
             response_model=UserLoginResponse,
             responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
             })
async def login_w_password(data: UserPasswordLoginRequest,
                           login_w_password_usecase=Depends(lambda: LoginWithPasswordUseCase())):
    user, failure = await login_w_password_usecase.execute(data.email, data.password)
    if failure is not None:
        return JSONResponse(
            status_code=failure.code,
            content={'status': 'unauthorized', 'message': "Incorrect username or password"})
    return {
        'status': 'success',
        'message': '',
        'data': {
            "name": user.full_name,
            "status": user.status,
            "phone": user.phone_number
        }
    }