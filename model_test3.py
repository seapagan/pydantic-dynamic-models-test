"""Another example by modifying the model class itself."""

from typing import TypeVar

from model import BaseDBModel

T = TypeVar("T", bound=BaseDBModel)


# Original model
class OriginalModel(BaseDBModel):
    name: str
    age: int
    email: str
    employed: bool
    address: str


# Function to modify the model class itself by removing unwanted fields
def modify_model(model: type[T], exclude_fields: list[str]) -> type[T]:
    """ "Return a model with specified fields excluded."""
    # Remove fields from model's __annotations__ and model_fields
    for field in exclude_fields:
        model.__annotations__.pop(field, None)
        model.model_fields.pop(field, None)

    # Rebuild the Pydantic model's internal validator and schema
    model.model_rebuild(force=True)

    return model


# Example usage
exclude_fields = ["age", "email"]
ModifiedModel = modify_model(OriginalModel, exclude_fields)

print(ModifiedModel.__annotations__)
# Instantiate the modified model
model_instance = ModifiedModel(
    name="Alice",
    employed=True,
    address="123 Street",
)  # type: ignore
print(model_instance.model_dump())
