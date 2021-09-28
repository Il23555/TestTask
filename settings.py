import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Server
HOST = os.environ.get("HOST", default='0.0.0.0')
PORT = os.environ.get("PORT", default=5000)
DEBUG = os.environ.get("DEBUG", default=True)

# models
PATH_TO_MODEL = os.path.join(BASE_DIR, "model/files/model.h5")
