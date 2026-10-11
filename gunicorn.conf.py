import os
import multiprocessing

# Port binding: Render, Heroku, Railway supply PORT in the environment
port = os.environ.get("PORT", "5000")
bind = f"0.0.0.0:{port}"

# Concurrency settings
# For memory efficiency with large in-memory JSON datasets, default to 2-4 workers/threads
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
threads = int(os.environ.get("PYTHON_MAX_THREADS", "4"))
worker_class = "gthread"

# Timeout: Allow 120s for dataset indexing on cold starts
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "120"))
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("LOG_LEVEL", "info")
