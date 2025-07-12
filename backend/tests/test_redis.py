# tests/test_redis.py

import redis
import pytest

def test_redis_ping():
    try:
        r = redis.Redis(host="redis", port=6379)
        assert r.ping() is True
    except Exception as e:
        pytest.fail(f"Redis ping a échoué avec l'erreur : {e}")
