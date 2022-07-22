# import pytest
# import bcrypt

# from unittest.mock import MagicMock

# from kink import di

# from services.user_management.domain.repository import UserRepository
# from services.user_management.domain.usecases import UserResetPasswordUsecase
# from core.types.failure import Failure

# def get_hashed_password(plain_text_password):
#     # Hash a password for the first time
#     #   (Using bcrypt, the salt is saved into the hash itself)
#     return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

# def check_password(plain_text_password, hashed_password):
#     # Check hashed password. Using bcrypt, the salt is saved into the hash itself
#     return bcrypt.checkpw(plain_text_password, hashed_password)

# @pytest.mark.asyncio
# async def test_user_reset_password_success():
#     """
#     User call reset password with a correct old password, new password and correct confirm password
#     Expect: Success, call the data layer, return nothing
#     """
#     # **Arrange**
#     # Set up Mock repository
#     user_id = "abcXyz"
#     user_old_password = "old_paZZW@R6"
#     user_new_password = "new_paZZW@R6"
#     user_new_password2 = "new_paZZW@R6"

#     mock_repository = UserRepository()
#     mock_repository.check_password = MagicMock(
#         return_value=(None, None)
#     )
#     mock_repository.change_password = MagicMock(
#         return_value=(None, None)
#     )

#     di[UserRepository] = mock_repository

#     usecase = UserResetPasswordUsecase()

#     # **Act**
#     result, failure = await usecase.execute(
#         user_id=user_id,
#         old_password=user_old_password,
#         new_password=user_new_password,
#         cf_new_password=user_new_password2,
#     )

#     # **Assert**

#     # Assert the repository is called with the above input data
#     mock_repository.check_password.assert_called_once_with(
#         user_id=user_id, 
#         password=get_hashed_password(user_old_password), 
#     )
#     mock_repository.change_password.assert_called_once_with(
#         user_id=user_id, 
#         password=get_hashed_password(user_old_password), 
#     )
#     # Assert it return expected Success results + registered User
#     assert failure is None
