import requests


def get_recognitions(mem_skip, api_key):
    """This function triggers the GET RECOGNITIONS API.
       https://api.highground.com/#api-Recognition-GetRecognition
       
       
       Keyword Arguments:
        mem_skip -- tracks member records to skip for looping through all records
        api_key -- authorizes API call
            
       Return:
        resp_val -- returns a JSON object of the API response (JSON)
    """
    headers = {
        'Accept': 'application/json',
        'clientkey': api_key
    }
    params = ({
        'skip': mem_skip
    })
    resp_val = requests.get(
        'https://api.highground.com/1.0/Recognition/',
        headers=headers,
        params=params
    )
    return resp_val.json()
