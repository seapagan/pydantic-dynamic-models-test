"""WIP example of dynamically creating a modified Pydantic model."""

from typing import TypeVar

from pydantic import create_model

from model import BaseDBModel

T = TypeVar("T", bound=BaseDBModel)


# Original model with types
class OriginalModel(BaseDBModel):
    """The original model to modify."""

    name: str
    age: int
    email: str
    employed: bool
    address: str


# Define the function more explicitly to work with MyPy
def create_modified_model(base_model: type[T], exclude_fields: list[str]) -> type[T]:
    """Return a new model with specified fields excluded."""
    # Get all fields and types from the base model
    base_fields = base_model.__annotations__.copy()

    # Remove the fields that are in the exclude_fields list
    for field in exclude_fields:
        base_fields.pop(field, None)

    # Create a new model dynamically excluding specified fields
    ModifiedModel: type[T] = create_model(  # noqa: N806
        "ModifiedModel",
        __base__=BaseDBModel,
        **{field: (field_type, ...) for field, field_type in base_fields.items()},
    )  # type: ignore

    return ModifiedModel


# Example usage
exclude_fields = ["age", "email"]
ModifiedModel = create_modified_model(OriginalModel, exclude_fields)

# Check the retained typing of the new model
print(ModifiedModel.__annotations__)  # noqa: T201

# Instantiate the new modified model
model_instance = ModifiedModel(
    name="Alice",
    address="123 Street",
    employed=True,
)  # type: ignore

print(model_instance.model_dump())  # noqa: T201
