from model import BaseDBModel


# Original model
class OriginalModel(BaseDBModel):
    name: str
    age: int
    email: str
    employed: bool
    address: str


# Function to modify the model class itself by keeping only the specified fields
def modify_model_to_include(
    model: type[BaseDBModel], include_fields: list[str]
) -> type[BaseDBModel]:
    """Return a model with only the specified fields included."""
    # Get all fields from model
    all_fields = set(model.__annotations__.keys())

    # Compute the fields to exclude
    exclude_fields = all_fields - set(include_fields)

    # Remove fields from model's __annotations__ and model_fields
    for field in exclude_fields:
        model.__annotations__.pop(field, None)
        model.model_fields.pop(field, None)

    # Rebuild the Pydantic model's internal validator and schema
    model.model_rebuild(force=True)

    return model


# Example usage
include_fields = ["name", "employed", "address"]
ModifiedModel = modify_model_to_include(OriginalModel, include_fields)

print(ModifiedModel.__annotations__)

# Instantiate the modified model
model_instance = ModifiedModel(
    name="Alice",
    employed=True,
    address="123 Street",
)  # type: ignore

# will only have 'name', 'employed', and 'address' fields
print(model_instance.model_dump())
