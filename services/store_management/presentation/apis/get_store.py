from fastapi import APIRouter, Depends

from services.store_management.domain.usecases.get_store import GetBaseStoreUsecase as GetBaseStoreUsecaseImpl

# from ...domain.usecases import GetBaseStoreUsecase

router = APIRouter()


@router.get('/{id}')
async def get_store_by_id(id: str, get_store_by_id_usecase: GetBaseStoreUsecaseImpl = Depends(GetBaseStoreUsecaseImpl)):
    result = await get_store_by_id_usecase.execute(id)
    return result
