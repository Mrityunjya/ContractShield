import pytest
from pathlib import Path

from utils.contract_validator import (
    assert_required_fields,
    validate_response_schema,
)


SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "user_schema.json"


@pytest.mark.parametrize("user_id", [1, 2, 3, 5, 10])
def test_user_api_contract(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200

    validate_response_schema(response, SCHEMA_PATH)


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

    assert_required_fields(payload, required_fields)