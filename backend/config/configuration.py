import json
import os

def get_config():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, 'config', 'config.json')
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config


if __name__ == "__main__":
    print(get_config()["base_dir"])