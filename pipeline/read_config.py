import yaml
from pathlib import Path

#path 
config_path = Path(__file__).parent.parent / "config" / "config.yaml"

with open(config_path, "r") as file:
    config = yaml.safe_load(file)

print(config)
print("Base URL:", config['crypto_api']['base_url'])
print("Endpoint:", config['crypto_api']['coins_endpoint'])
print("Currency:", config['crypto_api']['currency'])