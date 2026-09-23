# FastAPI Security Demo

A small REST API for a diploma demonstration. It provides SQLite persistence,
JWT authentication, user and admin authorization, and simple item endpoints.
FastAPI's interactive documentation and OpenAPI schema remain enabled.

## Setup

Python 3.11 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Static checks

Run these commands from the `api` directory:

```bash
python -m pip install -r requirements-dev.txt
python -m pylint app
python -m bandit -r app
```

In CI, run the checks as separate steps or use `&&` between them so either
failure fails the job. Do not pipe Pylint output into Bandit. Omit `-lll` to
include low- and medium-severity findings as well as high-severity findings.
Scan `app`, not the virtual environment.

The `nosec B106` annotation on the login response only suppresses the false
positive for the public `bearer` authorization scheme. Other Bandit checks
remain enabled. SQLAlchemy data models locally exempt Pylint's minimum
public-method count because their behavior comes from the ORM.

## Seed the database

The seed command can safely be run more than once:

```bash
python -m app.seed
```

It creates these demo accounts:

- `security_user` / `password123` (`user` role)
- `security_admin` / `admin123` (`admin` role)

Passwords are stored as hashes, not as plaintext.

## Run the application

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive documentation is
at `http://127.0.0.1:8000/docs`, and the OpenAPI document is at
`http://127.0.0.1:8000/openapi.json`.

## Log in

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"security_user","password":"password123"}'
```

Copy the `access_token` value from the response, then use it as a bearer token:

```bash
curl http://127.0.0.1:8000/users/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Endpoints

| Method | Path | Access |
| --- | --- | --- |
| GET | `/health` | Public |
| POST | `/auth/login` | Public |
| GET | `/users/me` | Authenticated |
| GET | `/admin/users` | Admin only |
| GET | `/items` | Public |
| GET | `/items/{item_id}` | Public |
| POST | `/items` | Authenticated |
| GET | `/openapi.json` | Public |

To create an item:

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"name":"New item","description":"Created through the API"}'
```

For a real deployment, set a strong secret instead of the demo default:

```bash
export JWT_SECRET_KEY="replace-with-a-long-random-secret"
```
