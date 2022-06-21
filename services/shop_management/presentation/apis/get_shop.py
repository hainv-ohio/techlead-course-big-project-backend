from fastapi import APIRouter, Depends

from services.shop_management.domain.usecases.get_shop import GetBaseShopUsecase as GetBaseShopUsecaseImpl

# from ...domain.usecases import GetBaseShopUsecase

router = APIRouter()


@router.get('/{id}')
async def get_user_by_id(id: str, get_shop_by_id_usecase: GetBaseShopUsecaseImpl = Depends(GetBaseShopUsecaseImpl)):
    result = await get_shop_by_id_usecase.execute(id)
    return result
