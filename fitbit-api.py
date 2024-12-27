import requests

access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BXSFYiLCJzdWIiOiJDRkJCMzQiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2lybiB3Y2Ygd3NldCB3bG9jIHdyZXMiLCJleHAiOjE3MzUzNDc0MDMsImlhdCI6MTczNTMxODYwM30.jJfgoP3AMz3SQBaG61cyCnN4Ch2_5fVpn-eDefBkGp0'

header = {'Authorization': f'Bearer {access_token}'}

response = requests.get('https://api.fitbit.com/1/user/-/activities.json', headers=header).json()

print(response['best']['total']['steps'])

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