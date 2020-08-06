import yaml

def deserialize():
    with open('config.yaml') as file:
        key_list = yaml.load(file, Loader=yaml.FullLoader)
        return {
            'bot-token': key_list['bot-token'],
            'giphy-key': key_list['giphy-key'] 
        }