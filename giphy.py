#!/usr/bin/python

import time
import giphy_client
from giphy_client.rest import ApiException

def giphy(tag):
    api_instance = giphy_client.DefaultApi()
    api_key = open(".giphy-api-key.txt", "r").read().rstrip()
    fmt = 'json' 
    rating = 'g' 
    try: 
        api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
        return api_response.data.image_url
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

if __name__ == "__main__":
    print(giphy("cake"))
