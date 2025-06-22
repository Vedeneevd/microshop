
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .depencies import get_product_by_id
from .schemas import Product, ProductCreate, ProductUpdate
from core.models import db_helper


router = APIRouter(tags=['Products'])

@router.get('/', response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)


@router.get('/{product_id}/', response_model=Product)
async def get_product(product: Product = Depends(get_product_by_id)):
    return product

@router.post('/', response_model=Product)
async def create_product(product_in: ProductCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_product(session=session, product_in=product_in)


@router.put('/update_product', response_model=ProductUpdate)
async def update_product(product_update: ProductUpdate,
                         session: AsyncSession = Depends(db_helper.session_dependency),
                         product: Product = Depends(get_product_by_id)):
    return await crud.update_product(session=session, product_update=product_update, product=product)


@router.delete('/{product_id}/')
async def delete_product(session: AsyncSession = Depends(db_helper.session_dependency),
                         product: Product = Depends(get_product_by_id)):
    return await crud.delete_product(session=session,product=product)

