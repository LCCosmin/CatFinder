import yaml

def yaml_to_dict(filename: str) -> dict:
    with open(filename, 'r') as stream:
        dict_yaml = yaml.safe_load(stream)
    return dict_yaml
