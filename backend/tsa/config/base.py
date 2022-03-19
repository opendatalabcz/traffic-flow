from pathlib import Path

from konfetti import env

DATABASE_URL = env("DATABASE_URL")
DATABASE_NAME = env("DATABASE_NAME")

CELERY_BROKER = env("CELERY_BROKER", default="redis://localhost:6379/1")

MODELS_PATH = env("MODELS_PATH", cast=Path)

SOURCE_FILES_PATH = env("SOURCE_FILES_PATH", cast=Path)
OUTPUT_FILES_PATH = env("OUTPUT_FILES_PATH", cast=Path)

VIDEO_FRAME_RATE = env("VIDEO_FRAME_RATE", default=15, cast=int)
VIDEO_MAX_FRAMES = env("VIDEO_MAX_FRAMES", default=None, cast=int)
VIDEO_SHOW_CLASS = env("VIDEO_SHOW_CLASS", default=True, cast=bool)

INTERPOLATION_POLYNOMIAL_DEGREE = env("INTERPOLATION_POLYNOMIAL_DEGREE", default=3, cast=int)

VISUALIZATION_MIN_PATH_LENGTH = env("VISUALIZATION_MIN_PATH_LENGTH", default=150.0, cast=float)
VISUALIZATION_N_CLUSTERS = env("VISUALIZATION_N_CLUSTERS", default=12, cast=int)
