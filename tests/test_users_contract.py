import json
from pathlib import Path

from jsonschema import validate


SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "user_schema.json"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_user_api_contract(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    payload = response.json()
    schema = load_schema()

    validate(instance=payload, schema=schema)
def test_user_required_fields(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    payload = response.json()

    required_fields = [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company",
    ]

    for field in required_fields:
        assert field in payload, f"Missing required field: {field}"