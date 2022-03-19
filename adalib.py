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
         "name":"Noma",
         "phone":"+45 32 96 32 97",
         "price":"$$$$",
         "rating":4.5,
         "review_count":37,
         "location":[
            "Refshalevej 96",
            "1432 K\u00f8benhavn",
            "Denmark"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-"
      },
      {
         "source":"Yelp",
         "name":"H\u00f8st",
         "phone":"+45 89 93 84 09",
         "price":"$$$",
         "rating":4.5,
         "review_count":229,
         "location":[
            "N\u00f8rre Farimagsgade 41",
            "1364 K\u00f8benhavn K",
            "Denmark"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-"
      },
      {
         "source":"Yelp",
         "name":"Studio",
         "phone":"+45 72 14 88 08",
         "price":"$$$$",
         "rating":4.5,
         "review_count":41,
         "location":[
            "Havnegade 44",
            "1058 Copenhagen",
            "Denmark"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-"
      },
      {
         "source":"Yelp",
         "name":"Barr",
         "phone":"+45 32 96 32 93",
         "price":"$$$",
         "rating":4.5,
         "review_count":42,
         "location":[
            "Strandgade 93",
            "1401 K\u00f8benhavn",
            "Denmark"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-"
      },
      {
         "source":"Yelp",
         "name":"Geranium",
         "phone":"+45 69 96 00 20",
         "price":"$$$$",
         "rating":4.5,
         "review_count":86,
         "location":[
            "Per Henrik Lings All\u00e9 4, 8.",
            "2100 Copenhagen",
            "Denmark"
         ],
         "business_status":"-",
         "website":"-",
         "comment_count":"-",
         "share_count":"-",
         "description":"-"
      },
      {
         "source":"Google",
         "name":"Noma",
         "phone":"32 96 32 97",
         "price":4,
         "rating":4.6,
         "review_count":1523,
         "location":"Refshalevej 96, 1432 K\u00f8benhavn K, Denmark",
         "business_status":"OPERATIONAL",
         "website":"https://noma.dk/",
         "comment_count":"-",
         "share_count":"-",
         "description":"-"
      },
      {
         "source":"Facebook",
         "name":"-",
         "phone":"-",
         "price":"-",
         "rating":"-",
         "review_count":655,
         "location":"-",
         "business_status":"-",
         "website":"https://noma.dk/",
         "comment_count":406,
         "share_count":1180,
         "description":"Welcome Dear friends and guests, We are incredibly happy to be allowed to reopen the doors of noma, now that restrictions have eased in Denmark. In this moment, we are eager to connect with our community, and to celebrate summer in the best (and safest) way we can. Our reopening will happen in two s\u2026"
      }
   ],
   "errors":[

   ]
}
"""
