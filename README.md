# Modifying Pydantic models

This is some WIP/thoughts on how I can modify a Pydantic Model to return only a
specified (dynamic) subset of fields.

Currently, `model_test4.py` is the closest to what I want to achieve.

This is work to improve my `sqliter` project, specifically the case where the
user wants to return only a subset of fields from a table.
