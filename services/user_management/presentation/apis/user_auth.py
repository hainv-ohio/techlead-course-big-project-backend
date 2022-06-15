

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from services.user_management.domain.usecases.login_w_password import LoginWithPasswordUseCase
from ...domain.usecases import GetUserUseCase, LoginWithPasswordUseCase

from ..schemas.base import BaseResponseSchema
from ..schemas.user_auth import UserLoginResponse, UserPasswordLoginRequest

router = APIRouter()


@router.get('/{id}')
async def get_user_by_id(id: str,
                         get_user_by_id_usecase: GetUserUseCase = Depends(GetUserUseCase)):
    result = await get_user_by_id_usecase.execute(id)
    return {'name': "Hello", 'phone': '123456'}


@router.post("/password-login",
             name="Login with password",
             description='Login with password',
             response_model=UserLoginResponse,
             responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
             })
async def login_w_password(data: UserPasswordLoginRequest,
                           login_w_password_usecase = Depends(lambda: LoginWithPasswordUseCase())):
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
