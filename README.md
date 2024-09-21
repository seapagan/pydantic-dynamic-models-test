# Modifying Pydantic models

This is some WIP/thoughts on how I can modify a Pydantic Model to return only a
specified (dynamic) subset of fields.

Currently, `model_test4.py` is the closest to what I want to achieve.

This is work to improve my `sqliter` project, specifically the case where the
user wants to return only a subset of fields from a table, and will eventually
replace the code in the `model_validate_partial` class method in `model.py`.

Putting it out here in the hope that someone else can benefit from it. There is
not a lot of info on how to do this, so I had to figure it out myself.

## Usage

You need to have [uv](https://github.com/astral-sh/uv) installed to run the
code, then you can set up the virtual environment and install the dependencies:

```bash
uv sync
```

Then activate the virtual environment:

```bash
source .venv/bin/activate
```

> [!NOTE]
>
> The only dependency is `pydantic`, so you can install it with `pip` if you
> don't want to use `uv`, or add this to your own project.

Then you can run the individual example files:

```bash
python model_test4.py
```
