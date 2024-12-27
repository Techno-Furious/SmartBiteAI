import requests
import dotenv
import os

dotenv.load_dotenv()

access_token = os.getenv('access_token')
header = {'Authorization': f'Bearer {access_token}'}

response = requests.get('https://api.fitbit.com/1/user/-/activities.json', headers=header).json()

def cal_burned(response):
    date,val =  response['best']['total']['steps'].values()
    return date,val

def dist_covered(response):
    date,val =  response['best']['total']['distance'].values()
    return date,val

date,val = cal_burned(response)
print(f"Date: {date} \nCalories Burned: {val} steps")

date,val = dist_covered(response)
print(f"Date: {date} \nDistance Covered: {val} kms")
# {'best': {'total': {'distance': {'date': '2024-12-27',
#                                   'value': 0.30739},
#                      'steps': {'date': '2024-12-27', 'value': 405}
#                     },
#           'tracker': {'distance': {'date': '2024-12-27', 'value': 0.30739}, 'steps': {'date': '2024-12-27', 'value': 405}}
#           },
# 'lifetime': {'total': {'activeScore': -1, 'caloriesOut': -1, 'distance': 0.31, 'floors': 0, 'steps': 405},
# 'tracker': {'activeScore': -1, 'caloriesOut': -1, 'distance': 0.31, 'floors': 0, 'steps': 405}}
 
#  }