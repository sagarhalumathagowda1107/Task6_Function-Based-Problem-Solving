"""
Problem Statement 2:Online Food Delivery Time Estimator
Create a function that estimates delivery time based on:
Distance (km)
Weather condition
Traffic level
Apply delays dynamically and display final ETA.

"""

def estimate_delivery_time(distance,weather,traffic):
    time = distance * 5 # 5 minutes per km

    if traffic =="low":
        time += 0
    elif traffic == "high":
        time +=5

    if weather == "rainy":
        time +=10
    elif weather == "stormy":
        time +=20
    
    return time


distance = 8
weather = "rainy"
traffic = "high"
print(f"Estimated Delivery Time:",estimate_delivery_time(distance,weather,traffic),"minutes")