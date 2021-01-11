import requests


url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={
    "page_likes": 6983,
    "page_checkins":4000,
    "page_talking":5,
    "page_category":19,
    "cc1_min":2.0,
    "cc1_max":800.0,
    "cc1_avg": 8.0,
    "cc1_med":1.0,
    "cc1_std":70.0,
    "cc2_min":2.0,
    "cc2_max":800.0,
    "cc2_avg": 8.0,
    "cc2_med":1.0,
    "cc2_std":70.0,
    "cc3_min":2.0,
    "cc3_max":800.0,
    "cc3_avg": 8.0,
    "cc3_med":1.0,
    "cc3_std":70.0,
    "cc4_min":2.0,
    "cc4_max":800.0,
    "cc4_avg": 8.0,
    "cc4_med":1.0,
    "cc4_std":70.0,
    "cc5_min":2.0,
    "cc5_max":800.0,
    "cc5_avg": 8.0,
    "cc5_med":1.0,
    "cc5_std":70.0,
    "CC1":41,
    "CC2":30,
    "CC3":3,
    "CC4":7,
    "CC5":27,
    "base_time":34,
    "post_length":178,
    "post_share_count":134,
    "hour_local":24,
    "post_pub_sunday": 0,
    "post_pub_monday": 1,
    "post_pub_tuesday": 0,
    "post_pub_wednesday": 0,
    "post_pub_thursday": 0,
    "post_pub_friday": 0,
    "post_pub_saturday": 0,
    "base_date_sunday": 0,
    "base_date_monday": 0,
    "base_date_tuesday": 1,
    "base_date_wednesday": 0,
    "base_date_thursday": 0,
    "base_date_friday": 0,
    "base_date_saturday": 0
})

print(r.json())




