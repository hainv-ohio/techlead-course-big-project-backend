import pytest

from unittest.mock import MagicMock

from kink import di

from services.user_management.domain.entities.user import User
from services.user_management.domain.repository import UserRepository
from services.user_management.domain.usecases import RegisterUserUsecase
from core.types.failure import Failure

@pytest.mark.asyncio
async def test_user_register_success():
    """
    User register with a good email, good password, full basic info
    Expect: Success, return registered User
    """
    # **Arrange**
    # Set up Mock repository
    user_id = "abcXyZ"
    user_name = "Test full name"
    user_email = "test@gmail.com"
    user_phone = "0313333888"
    user_password = "pass@78"

    mock_repository = UserRepository()
    # Return a mock user
    mock_repository.register_user = MagicMock(
        return_value=(
            User(
                id=user_id,
                full_name=user_name, 
                phone_number=user_phone, 
                email=user_email, 
            ), None)
    )

    di[UserRepository] = mock_repository

    usecase = RegisterUserUsecase()

    # **Act**

    user, failure = await usecase.execute(
        name=user_name, 
        email=user_email, 
        phone=user_phone, 
        password=user_password)

    # **Assert**

    # Assert the repository is called with the above input data
    mock_repository.register_user.assert_called_once_with(
        full_name=user_name, 
        phone_number=user_phone, 
        email=user_email, 
        password=user_password
    )
    # Assert it return expected Success results + registered User
    assert failure is None
    assert user.id==user_id

@pytest.mark.asyncio
async def test_user_register_with_existed_email_and_fail():
    """
    User register with an existed email
    Expect: Return duplicated email failure
    """
    # **Arrange**
    # Set up Mock repository
    user_id = "abcXyZ"
    user_name = "Test full name"
    user_email = "test@gmail.com" # Existed
    user_phone = "0313333888"
    user_password = "pass1234"

    failure_message = "Email existed"

    mock_repository = UserRepository()
    # Data layer will return a mock failure
    mock_repository.register_user = MagicMock(return_value=(None, Failure(400, failure_message)))

    di[UserRepository] = mock_repository
    usecase = RegisterUserUsecase()

    # **Act**
    user, failure = await usecase.execute(
        name=user_name, 
        email=user_email, 
        phone=user_phone, 
        password=user_password)

    # **Assert**
    # Assert the repository is called with the above input data
    mock_repository.register_user.assert_called_once_with(
        full_name=user_name, 
        phone_number=user_phone, 
        email=user_email, 
        password=user_password
    )
    # Assert it return expected Failure results + registered User
    assert user is None
    assert failure.message == failure_message
    assert failure.code == 400

@pytest.mark.asyncio
async def test_user_register_with_weak_password_and_fail():
    """
    User register with a weak password (len < 6)
    Expect: Return failure
    """
    # **Arrange**
    # Set up Mock repository
    user_id = "abcXyZ"
    user_name = "Test full name"
    user_email = "test@gmail.com"
    user_phone = "0313333888"
    user_password = "12345" # weak

    failure_message = "Weak password"

    mock_repository = UserRepository()
    # Return a mock user
    mock_repository.register_user = MagicMock()

    di[UserRepository] = mock_repository
    usecase = RegisterUserUsecase()

    # **Act**
    user, failure = await usecase.execute(
        name=user_name, 
        email=user_email, 
        phone=user_phone, 
        password=user_password)

    # **Assert**
    # Must not be called because the input is invalid
    mock_repository.register_user.assert_not_called()

    # Assert it return expected Failure results + registered User
    assert user is None
    assert failure.message == failure_message
    assert failure.code == 400
