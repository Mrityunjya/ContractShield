import json
from pathlib import Path

from jsonschema import validate


def load_schema(schema_path: Path) -> dict:
    with open(schema_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_response_schema(response, schema_path: Path) -> None:
    schema = load_schema(schema_path)
    validate(instance=response.json(), schema=schema)


def assert_required_fields(payload: dict, required_fields: list[str]) -> None:
    for field in required_fields:
        assert field in payload, f"Missing required field: {field}"