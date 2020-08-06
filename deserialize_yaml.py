import yaml


def deserialize(dict_key):
    with open('config.yaml') as file:
        key_list = yaml.load(file, Loader=yaml.FullLoader)
        return key_list[dict_key]
