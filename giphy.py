#!/usr/bin/python
import time
import giphy_client
from deserialize_yaml import deserialize
from giphy_client.rest import ApiException

def giphy(tag, rating):
    api_instance = giphy_client.DefaultApi()
    try: 
        api_response = api_instance.gifs_random_get(deserialize('giphy-key'), tag=tag, rating=rating, fmt='json')
        return api_response.data.image_url
    except ApiException as e:
        print(f'Exception when calling DefaultApi->gifs_search_get: {e}')

if __name__ == "__main__":
    print(giphy("Hello, World!", 'g'))
