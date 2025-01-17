import os
from dotenv import load_dotenv

load_dotenv()

REDS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
QUEUES = ["emails", "default"]

