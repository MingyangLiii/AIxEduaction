import json
import os

def get_config():
    # project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # config_path = os.path.join(project_root, 'config', 'config.json')
    
    # with open(config_path, 'r') as file:
    #     config = json.load(file)

    config = {
        'base_dir': os.path.dirname(os.getcwd()),
        "api_key": "sk"
    }

    print(config['base_dir'])
    
    return config

