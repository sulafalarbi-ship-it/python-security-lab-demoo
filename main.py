import yaml

def load_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.load(f, Loader=yaml.Loader)
if __name__ == "__main__":
    config = load_config("config.yaml")
    print(config)
