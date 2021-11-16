# Flask Celery Redis

Run flask Server
```shell
python run.py
```

Start Redis
```shell
docker run -p 6379:6379 -d redis:5.0
```

Start Workers
```shell
celery -A worker.celery worker --loglevel=info
```

Start Monitor
```shell
celery -A app flower --port=5566
```