water_level = 25


if water_level < 30:
    print("Sprinkler ON (Water level too low)")
elif water_level > 80:
    print("Sprinkler OFF (Water level high enough)")
else:
    print("Water level normal(No need to activate sprinkler)")
