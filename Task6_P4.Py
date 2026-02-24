def classify_server_load(cpu_readings):
    total = 0

    # Loop to calculate total CPU usage
    for cpu in cpu_readings:
        total += cpu

    average_cpu = total / len(cpu_readings)

    # Classification based on average CPU
    if average_cpu < 50:
        status = "Normal"
    elif average_cpu <= 80:
        status = "Warning"
    else:
        status = "Critical"

    return average_cpu, status

cpu_readings = [45, 60, 70, 85, 90]

average, status = classify_server_load(cpu_readings)

print("Average CPU Load:", int(average), "%")
print("Server Status:", status)