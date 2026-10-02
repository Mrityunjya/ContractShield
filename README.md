# ContractShield

**Automated API Contract Validation Framework**

[![ContractShield Tests](https://github.com/Mrityunjya/contractshield/actions/workflows/tests.yml/badge.svg)](https://github.com/Mrityunjya/contractshield/actions/workflows/tests.yml)

ContractShield is an **API automation and contract validation framework** built with **Python, PyTest, Requests, and JSON Schema**.

It validates REST API responses against predefined contracts and helps detect **schema violations, missing fields, incorrect data types, invalid endpoints, and unexpected API failures** through automated regression tests.

---

## **Key Features**

- **REST API Testing** using `Requests`
- **JSON Schema Contract Validation**
- **Required Field Validation**
- **Data Type Validation**
- **Parameterized Testing** with PyTest
- **Negative & Error-Handling Testing**
- **Response-Time Guardrails**
- **Reusable API Client**
- **Reusable Contract Validation Utilities**
- **HTML Test Reporting**
- **GitHub Actions CI Automation**

---

## **Architecture**

```text
                         ContractShield
                               |
              +----------------+----------------+
              |                                 |
              v                                 v
         API Client                         Test Suite
              |                                 |
              v                     +-----------+-----------+
          REST API                   |                       |
              |                      v                       v
              v              Contract Tests          Negative Tests
       JSON Response                 |
              |                      |
              +----------+-----------+
                         |
                         v
                  JSON Schema
                    Validation
                         |
                    +----+----+
                    |         |
                    v         v
                  PASS       FAIL
                    |
                    v
             CI / Test Reports
```

---

## **Project Structure**

```text
contractshield/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── schemas/
│   └── user_schema.json
│
├── tests/
│   ├── test_users_contract.py
│   └── test_users_negative.py
│
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   └── contract_validator.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## **Test Coverage**

| **Test Area** | **Coverage** |
|---|---|
| HTTP status validation | ✅ |
| JSON Schema validation | ✅ |
| Required field validation | ✅ |
| Data type validation | ✅ |
| Parameterized API testing | ✅ |
| Invalid resource handling | ✅ |
| Invalid endpoint handling | ✅ |
| 5xx response detection | ✅ |
| Response-time guardrail | ✅ |
| HTML test reporting | ✅ |
| CI automation | ✅ |

---

## **Tech Stack**

| **Technology** | **Purpose** |
|---|---|
| **Python** | Test framework implementation |
| **PyTest** | Test execution and parameterization |
| **Requests** | HTTP/API communication |
| **JSON Schema** | API contract validation |
| **pytest-html** | HTML test reporting |
| **GitHub Actions** | CI test automation |
| **Git** | Version control |

---

## **Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/contractshield.git
cd contractshield
```

### **2. Create a Virtual Environment**

```bash
python -m venv .venv
```

### **3. Activate the Environment**

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **Running Tests**

Run the complete test suite:

```bash
pytest -v
```

A successful execution should produce a result similar to:

```text
6 passed
```

The exact number may increase as additional test cases are added.

---

## **HTML Test Report**

Generate a standalone HTML test report using:

```bash
pytest --html=reports/report.html --self-contained-html
```

The generated report is stored locally at:

```text
reports/report.html
```

The `reports/` directory is excluded from version control for generated HTML artifacts.

---

## **Continuous Integration**

ContractShield uses **GitHub Actions** to automatically execute the test suite.

The CI workflow runs on:

- **Pushes to `main`**
- **Pull requests targeting `main`**

The pipeline performs:

```text
Checkout Repository
        ↓
Set Up Python
        ↓
Install Dependencies
        ↓
Execute PyTest Suite
        ↓
PASS / FAIL
```

This provides an automated regression check whenever changes are pushed to the repository.

---

## **Design Approach**

ContractShield separates API communication, contract definitions, and test logic into independent components.

### **API Client**

`utils/api_client.py`

Provides a reusable HTTP client abstraction using `requests.Session`.

### **Contract Validator**

`utils/contract_validator.py`

Centralizes:

- JSON Schema loading
- Response schema validation
- Required-field validation

### **Schema Definitions**

`schemas/`

Contains JSON Schema definitions representing the expected structure of API responses.

### **Test Suite**

`tests/`

Contains functional contract tests and negative/error-handling scenarios.

This separation keeps the framework **reusable, maintainable, and easier to extend**.

---

## **Current Validation Flow**

```text
API Request
    ↓
HTTP Response
    ↓
Status Code Validation
    ↓
JSON Payload Extraction
    ↓
Schema Validation
    ↓
Required Field Validation
    ↓
Test Result
```
