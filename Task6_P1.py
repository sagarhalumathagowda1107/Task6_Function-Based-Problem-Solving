"""
Problem Statement 1:Smart Parking Lot Management System
Design a function to manage a smart parking lot.
The system should:
Accept vehicle entry and exit logs
Calculate total parked vehicles
Identify peak parking usage
Alert if parking exceeds capacity

"""

def Smart_Parking_Lot(Parking_Capacity,Vehicle_logs):

    parked_vehicles = 0
    peak_usage = 0

    for logs in Vehicle_logs:
        if logs =="IN":
            parked_vehicles +=1
        elif logs=="OUT" and parked_vehicles>0:
            parked_vehicles-=1

    #Track peak usage
    peak_usage = max(peak_usage,parked_vehicles)

    if peak_usage >Parking_Capacity:
        status = "Alert! Parking Exceeded Capacity"
    elif peak_usage == Parking_Capacity:
        status = "Parking Full"
    else:
        status = "Parking Available"

    return parked_vehicles,peak_usage,status


Parking_Capacity = 50
Vehicle_Logs = ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"]

current_parkedVehicles , peak, status = Smart_Parking_Lot(Parking_Capacity,Vehicle_Logs)
print(f"Current Parked Vehicles: {current_parkedVehicles}")
print(f"Peak Parking Usage: {peak}")
print(f"Parking Status: {status}")
