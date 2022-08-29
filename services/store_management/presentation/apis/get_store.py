from fastapi import APIRouter, Depends

from services.store_management.domain.usecases.get_store import GetBaseStoreUsecase as GetBaseStoreUsecaseImpl
from services.store_management.domain.usecases.get_list_store import GetListStoreUseCase as GetListStoreUseCaseImpl

# from ...domain.usecases import GetBaseStoreUsecase

router = APIRouter()


@router.get('/get/{id}')
async def get_store_by_id(id: str, get_store_by_id_usecase: GetBaseStoreUsecaseImpl = Depends(GetBaseStoreUsecaseImpl)):
    result = await get_store_by_id_usecase.execute(id)
    return result

@router.get('/list')
async def get_list_store(get_list_store: GetListStoreUseCaseImpl = Depends(GetListStoreUseCaseImpl)):
    result = await get_list_store.execute()
    return result
