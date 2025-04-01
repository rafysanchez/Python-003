# Serviço de Produto 

from app.domain.models.product import Product
from app.repository.product_repository import ProductRepository
from app.domain.schemas.product_schema import product_schema
from typing import List, Optional, Dict, Any

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product(self, id: int) -> Optional[Dict[str, Any]]:
        product = self.repository.get(id)
        return product_schema.dump(product) if product else None

    def get_all_products(self) -> List[Dict[str, Any]]:
        products = self.repository.get_all()
        return product_schema.dump(products, many=True)

    def create_product(self, data: Dict[str, Any]) -> Dict[str, Any]:
        product = Product(**data)
        created_product = self.repository.create(product)
        return product_schema.dump(created_product)

    def update_product(self, id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        product = Product(**data)
        updated_product = self.repository.update(id, product)
        return product_schema.dump(updated_product) if updated_product else None

    def delete_product(self, id: int) -> bool:
        return self.repository.delete(id) 
