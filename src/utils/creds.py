import os
import sys

import toml

CONFIG_FILE = ".credentials.toml"
ENV = os.getenv("ENV", "local")

with open(CONFIG_FILE, mode="r", encoding="utf-8") as config_file:
    config = toml.load(config_file)
    if ENV not in config["env"]:
        sys.exit(f"EnvError: \033[1;91m{ENV}\033[0m")
    DEFAULTS: dict = config["credentials"]["default"]
    RETRIEVE: dict = config["credentials"]["retrieve"]


def get_value(key: str) -> str:
    if key in DEFAULTS:
        return DEFAULTS[key]
    if ENV == "local":
        return os.getenv(key, f"KeyError: \033[1;91m{key}\033[0m")
    if key in RETRIEVE:
        "implement for secure retrieval of passkeys"
        pass


def get_map() -> dict:
    key_map: dict = {}
    if ENV == "local":
        for key in RETRIEVE:
            key_map[key] = os.getenv(key, "Not Found")
    else:
        "implement for secure retrieval of passkeys"
    DEFAULTS.update(key_map)
    return DEFAULTS


if __name__ == "__main__":
    for k, v in get_map().items():
        sys.stdout.write(f"{k}: {v}\n")
