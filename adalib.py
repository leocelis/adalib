# ADA lib v0.0.1
import requests

# Constants
API_URL = 'https://api.ada-tool.com/'
API_TIMEOUT = 10  # seconds


def get_business_info(business_name, business_location):
    ENDPOINT = 'business'
    params = {'business_name': business_name, 'business_location': business_location}
    url = API_URL + ENDPOINT
    try:

        response = requests.get(url,
                                params,
                                timeout=API_TIMEOUT)
        return response.json()
    except Exception as e:
        return {'error': str(e)}


# example request
b = get_business_info(business_name="Noma",
                      business_location="Copenhagen")

"""
Example response

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
      {
         "source":"Yelp",
         "name":"Dog House Grill",
         "phone":"(559) 294-9920",
         "price":"$$",
         "rating":4.0,
         "review_count":2332,
         "location":[
            "2789 E Shaw Ave",
            "Fresno, CA 93710"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-",
         "url":"https://www.yelp.com/biz/dog-house-grill-fresno-2?adjust_creative=c_q8ZW1Lhf3fTNJWYqvlUw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=c_q8ZW1Lhf3fTNJWYqvlUw",
         "weekday_text":"['Monday: 11:00 - 21:00', 'Tuesday: 11:00 - 21:00', 'Wednesday: 11:00 - 21:00', 'Thursday: 11:00 - 22:00', 'Friday: 11:00 - 22:00', 'Saturday: 11:00 - 22:00', 'Sunday: 11:00 - 21:00']"
      },
      {
         "source":"Google",
         "name":"Main Street Grill",
         "phone":"(650) 726-5300",
         "price":null,
         "rating":4.5,
         "review_count":404,
         "location":"547 Main St, Half Moon Bay, CA 94019, USA",
         "business_status":"OPERATIONAL",
         "website":"https://www.mainstreetgrillhmb.com/",
         "comment_count":"-",
         "share_count":"-",
         "description":"-",
         "url":"https://maps.google.com/?cid=5399955144204974389",
         "weekday_text":"['Monday: 7:30 AM \u2013 2:00 PM', 'Tuesday: 7:30 AM \u2013 2:00 PM', 'Wednesday: Closed', 'Thursday: 7:30 AM \u2013 2:00 PM', 'Friday: 7:30 AM \u2013 2:00 PM', 'Saturday: 7:30 AM \u2013 2:00 PM', 'Sunday: 7:30 AM \u2013 2:00 PM']"
      },
      {
         "source":"Facebook",
         "name":"-",
         "phone":"-",
         "price":"-",
         "rating":"-",
         "review_count":0,
         "location":"-",
         "business_status":"-",
         "website":"https://www.mainstreetgrillhmb.com/",
         "comment_count":0,
         "share_count":0,
         "description":null,
         "url":"-",
         "weekday_text":"-"
      }
   ],
   "errors":[

   ]
}
"""
