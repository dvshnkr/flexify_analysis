from pathlib import Path
import yaml

# Determine the project root from the location of this script
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

def load_config():
    """Loads the YAML configuration and resolves paths."""
    config_path = PROJECT_ROOT / 'config' / 'paths.yaml'
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_data_path(key='raw', filename=None):
    """
    Returns a Path object for a data file.
    e.g., get_data_path('raw', 'data.csv')
    """
    config = load_config()
    relative_path = config['data'][key]
    full_path = PROJECT_ROOT / relative_path
    if filename:
        return full_path / filename
    return full_path
