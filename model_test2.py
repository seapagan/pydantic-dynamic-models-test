import copy

from pydantic import BaseModel


# Base model with new config for immutability in Pydantic v2
class BaseDBModel(BaseModel):
    model_config = {
        "frozen": True  # This replaces `allow_mutation = False` from v1
    }

    @classmethod
    def class_method(cls) -> str:
        return "Class method from BaseDBModel"


class OriginalModel(BaseDBModel):
    """The original model to modify."""

    name: str
    age: int
    email: str
    employed: bool
    address: str


# Example instance
original_instance = OriginalModel(
    name="Alice", age=30, email="alice@example.com", employed=True, address="123 Street"
)


# Function to deep-copy the instance and remove fields
def copy_and_remove_fields(
    instance: OriginalModel, exclude_fields: list[str]
) -> OriginalModel:
    # Deep copy the original instance
    modified_instance = copy.deepcopy(instance)

    # Remove fields by manipulating the instance's __dict__
    for field in exclude_fields:
        modified_instance.__dict__.pop(field, None)

    return modified_instance


# Example usage
exclude_fields = ["age", "email"]
modified_instance = copy_and_remove_fields(original_instance, exclude_fields)

# Check the retained fields of the modified instance
print(
    modified_instance.model_dump()
)  # Only 'name', 'employed', and 'address' will appear

# Check that the modified instance still has access to class methods and base class config
print(modified_instance.class_method())  # Output: "Class method from BaseDBModel"
print(modified_instance.model_config["frozen"])
