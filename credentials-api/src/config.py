import os
# --- About The App ---
APP_NAME = os.getenv("APP_NAME", "fastapi-folder-structure")
APP_DESCRIPTION = "API which contains industry standard folder structure"

# Local setup without services and auth. Defaults to false. Local must be set explicitly
LOCAL_APP = bool(os.getenv("LOCAL_APP", 1))

if LOCAL_APP:
    APP_HOST = "localhost"
    APP_PORT = 8000
else:
    # If you are deploying then add your owned apphost and port here
    pass

# Number of concurrent processes
APP_WORKER = int(os.getenv("APP_WORKER", 1))

# Endpoint to Swagger UI
SWAGGER_ENDPOINT = os.getenv("SWAGGER_ENDPOINT", "/docs")
MONGO_CREDENTIALS_PATH = "secrets/mongo-credentials.json"
