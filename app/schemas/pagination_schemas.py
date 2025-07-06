from math import ceil

from pydantic import BaseModel, Field, model_validator


class PaginationQuery(BaseModel):
    page: int = Field(gt=0, examples=[2])
    size: int = Field(gt=0, le=500, default=100, examples=[100])


class PaginationResult[M](PaginationQuery):
    total_items: int = Field(examples=[215])
    total_pages: int = Field(default=0, examples=[3])
    items_count: int = Field(default=0, examples=[100])
    items: list[M]

    @model_validator(mode="after")
    def validate_model(self):
        self.items_count = len(self.items)
        self.total_pages = ceil(self.total_items / self.size) or 1
        return self
