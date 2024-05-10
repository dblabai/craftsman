import os
from shlex import quote
import subprocess
from craftsman.core.app_support_path import (
    get_app_support_path,
    pip_env_path,
    python_env_path,
)
from craftsman.core.constants import SystemConstants
from craftsman.resources.resources_path import get_requirements_path
from craftsman.utils.message_util import show_message


def init_env():
    app_support_path = get_app_support_path()
    env_path = os.path.join(app_support_path, SystemConstants.ENV)

    if not os.path.exists(env_path):
        subprocess.run(["python", "-m", SystemConstants.ENV, env_path], check=True)

    init_requirements()


def init_requirements():
    command = f"{quote(pip_env_path())} install -r {quote(get_requirements_path())}/requirements.txt"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        pass
    else:
        show_message(f"Failed to initialize dependencies: {result.stderr}")
