import os
from typing_extensions import Required

def getenv(key, requires=True):
    value = os.environ.get(key)
    if value is None and Required:
        raise RuntimeError(f"Missing required config: %{key}")
    return value