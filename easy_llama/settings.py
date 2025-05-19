from __future__ import annotations

import os
import sys
import nltk
import typing as t
from pathlib import Path
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, YamlConfigSettingsSource, SettingsConfigDict


PROJECT_ROOT = Path(os.environ.get("PROJECT_ROOT", ".")).resolve()


# class BasicSettings(BaseFileSettings):