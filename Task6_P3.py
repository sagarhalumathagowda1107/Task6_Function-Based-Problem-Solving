def seat_occupancy_analyzer(total_seats, booked_seats):
    booked_count = len(booked_seats)

    # Percentage calculation
    occupancy_percentage = (booked_count / total_seats) * 100

    # Show status logic
    if occupancy_percentage == 100:
        status = "Housefull"
        suggestion = "No additional shows required"
    elif occupancy_percentage >= 70:
        status = "Almost Full"
        suggestion = "Consider opening additional shows"
    else:
        status = "Seats Available"
        suggestion = "No action required"

    return occupancy_percentage, status, suggestion

total_seats = 200
booked_seats = [1] * 150   # 150 booked seats

occupancy, status, suggestion = seat_occupancy_analyzer(total_seats, booked_seats)

print("Occupancy:", int(occupancy), "%")
print("Show Status:", status)
print("Suggestion:", suggestion)