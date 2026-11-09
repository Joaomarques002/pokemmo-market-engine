from pydantic import BaseModel, Field

class GTLItem(BaseModel):
    item_name: str = Field(..., min_length=1, description="Nome do item no PokeMMO")
    category: str = Field(..., description="Categoria do item (ex: Medicine, Held Items, TMs)")
    price: int = Field(..., gt=0, description="Preço total ou unitário no GTL (deve ser maior que zero)")
    quantity: int = Field(..., gt=0, description="Quantidade do item transacionado")