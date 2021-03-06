import json
import os

os.environ['PY_ENV'] = os.environ.get('PY_ENV') or 'development'
CONFIG_NAME_MAP = {
    'test': 'example_default',
    'development': 'default',
}
ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

config_name = CONFIG_NAME_MAP.get(os.environ['PY_ENV'])
with open(os.path.join(ROOT_DIR, 'config', f'{config_name}.json')) as f:
    config = json.load(f)
