def resource_usage_monitor(resource_usage):
    overused_resources = []
    threshold = 6  # hours

    for resource, hours in resource_usage.items():
        if hours > threshold:
            overused_resources.append(resource)

    # Energy alert condition
    if overused_resources:
        alert = "Yes"
    else:
        alert = "No"

    return overused_resources, alert

resource_usage = {
    "Projector": 6,
    "AC": 9,
    "Lights": 4
}

overused, alert = resource_usage_monitor(resource_usage)

print("Overused Resources:", ", ".join(overused))
print("Energy Alert:", alert)