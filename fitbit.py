import requests
import dotenv
import os
from datetime import datetime
# from api_info import update_steps_distance,ensure_daily_entry
dotenv.load_dotenv()
access_token = os.getenv('access')
header = {'Authorization': f'Bearer {access_token}'}

def todays_date():
    return datetime.today().strftime("%Y-%m-%d")

def steps_covered():
    response = requests.get(f'https://api.fitbit.com/1/user/-/activities/date/{todays_date()}.json', headers=header).json()
    return response['summary']['steps']

def dist_covered():
    response = requests.get(f'https://api.fitbit.com/1/user/-/activities/date/{todays_date()}.json', headers=header).json()
    return response['summary']['distances'][0]['distance']

def cal_burned():
    response = requests.get(f'https://api.fitbit.com/1/user/-/activities/date/{todays_date()}.json', headers=header).json()
    return response['summary']['caloriesOut']

if __name__ == '__main__':
    # response = requests.get(f'https://api.fitbit.com/1/user/-/activities/date/{todays_date()}.json', headers=header).json()
    # print(response)
    print(f"Steps Covered: {steps_covered()}")
    print(f"Distance Covered: {dist_covered()}")
    print(f"Calories Burned: {cal_burned()}")

# date,val = steps_burned(response)
# print(f"Calories Burned: {val} steps")

# date,val = dist_covered(response)
# print(f"Distance Covered: {val} kms")
# {'best': {'total': {'distance': {'date': '2024-12-27',
#                                   'value': 0.30739},
#                      'steps': {'date': '2024-12-27', 'value': 405}
#                     },
#           'tracker': {'distance': {'date': '2024-12-27', 'value': 0.30739}, 'steps': {'date': '2024-12-27', 'value': 405}}
#           },
# 'lifetime': {'total': {'activeScore': -1, 'caloriesOut': -1, 'distance': 0.31, 'floors': 0, 'steps': 405},
# 'tracker': {'activeScore': -1, 'caloriesOut': -1, 'distance': 0.31, 'floors': 0, 'steps': 405}}
 
#  }

{   'activities': [], 
    'summary': {'caloriesOut': 9, 'activityCalories': 0, 'caloriesBMR': 7, 'activeScore': -1, 'steps': 0, 'floors': 0, 'elevation': 0.0, 'sedentaryMinutes': 6, 'lightlyActiveMinutes': 0, 'fairlyActiveMinutes': 0, 'veryActiveMsBMR': 7, 'activeScore': -1, 'steps': 0, 'floors': 0, 'elevation': 0.0, 'sedentasBMR': 7, 'activeScore': -1, 'steps': 0, 'floors': 0, 'elevation': 0.0, 'sedentasBMR': 7, 'activeScore': -1, 'steps': 0, 'floors': 0, 'elevation': 0.0, 'sedentasBMR': 7, 'activeScore': -1, 'steps': 0, 'floors': 0, 'elevation': 0.0, 'sedentaryMinutes': 6, 'lightlyActiveMinutes': 0, 'fairlyActiveMinutes': 0, 'veryActiveMinutes': 0, 'distances': [{'activity': 'total', 'distance': 0.0}, {'activity': 'tracker', 'distance': 0.0}, {'activity': 'sedentaryActive', 'distance': 0.0}, {'activity': 'lightlyActive', 'distance': 0.0}, {'activity': 'moderatelyActive', 'distance': 0.0}, {'activity': 'veryActive', 'distance': 0.0}, 
    {'activity': 'loggedActivities', 'distance': 0.0}],
     'marginalCalories': 0, 'heartRateZones': []},
     'goals': {'caloriesOut': 2624, 'steps': 10000, 'distance': 8.05, 'floors': 10, 'activeMinutes': 30}
 }