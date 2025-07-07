### Quick Start

```sh
git clone https://github.com/dima-doroshenko/cmd-by-test-task.git
cd cmd-by-test-task
copy .env.example .env 
```

Paste the OpenWeatherMap API key into .env

```sh
docker compose up --build
docker compose exec app alembic upgrade head
```

---

### Check the result

-   **Frontend:** http://localhost:5000
-   **API documentation:** http://localhost:5000/docs