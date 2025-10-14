from fastapi import FastAPI
import os
import redis

app = FastAPI(title="FastAPI + Redis App")

# Redis configuration
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Redis client
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI + Redis App!"}

@app.get("/hit")
def hit():
    try:
        r.incr("hits")
        hits = r.get("hits")
        return {"hits": hits}
    except Exception as e:
        return {"error": f"Redis error: {str(e)}"}
