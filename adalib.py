# ADA lib v0.0.1
import requests

API_URL = 'https://api.ada-tool.com/'
API_TIMEOUT = 10  # seconds


def get_business_info(business_name: str, business_location: str):
    ENDPOINT = 'business'
    params = {
        'business_name': business_name,
        'business_location': business_location
    }
    url = API_URL + ENDPOINT

    try:
        response = requests.get(url,
                                params,
                                timeout=API_TIMEOUT)
        return response.json()
    except Exception as e:
        return {'error': str(e)}


businesses = get_business_info(
    business_name="Noma", business_location="Copenhagen"
)
print(businesses)

"""
{
   "results":[
      {
         "source":"Yelp",
         "name":"School House Restaurant & Tavern",
         "phone":"(559) 787-3271",
         "price":"$$",
         "rating":4.0,
         "review_count":507,
         "location":[
            "1018 S Frankwood Ave",
            "Sanger, CA 93657"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-",
         "url":"https://www.yelp.com/biz/school-house-restaurant-and-tavern-sanger-3?adjust_creative=c_q8ZW1Lhf3fTNJWYqvlUw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=c_q8ZW1Lhf3fTNJWYqvlUw",
         "weekday_text":"['Wednesday: 16:00 - 20:00', 'Thursday: 16:00 - 20:00', 'Friday: 16:00 - 20:00', 'Saturday: 16:00 - 20:00', 'Sunday: 16:00 - 20:00']"
      },
   ],
   "errors":[

   ]
}
"""


def get_wines(wine_name: str):
    ENDPOINT = 'wines'
    params = {'search': wine_name, }
    url = API_URL + ENDPOINT

    try:
        response = requests.get(
            url,
            params,
            timeout=API_TIMEOUT
        )
        return response.json()
    except Exception as e:
        return {'error': str(e)}


wines = get_wines(wine_name="flores")
print(wines)

"""
{
   "results":[
      {
         "status":"Live",
         "display_name":"Val de Flores, Mendoza",
         "producer_title":"",
         "producer_name":"Val de Flores",
         "wine":"",
         "country":"Argentina",
         "region":"Mendoza",
         "sub_region":"",
         "site":"",
         "parcel":"",
         "colour":"Red",
         "type":"Wine",
         "sub_type":"Still",
         "designation":"",
         "classification":"",
         "vintage_config":"sequential",
         "first_vintage":""
            }
   ],
   "error":"None"
}
"""
