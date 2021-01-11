def age():
    x = int(input("Enter your age in years: "))
    beats_life = heartbeats(x)
    yawns_life = yawns(x)
    print(beats_life, "heartbeats and", yawns_life, "yawns so far")


def heartbeats(age):
    x = 72
    beats_hour = 60 * x
    beats_year = beats_hour * 365
    beats_life = beats_year * age
    x = beats_life
    return x


def yawns(age):
    x = 5
    yawns_year = 5 * 365
    yawns_life = age * yawns_year
    x = yawns_life
    return x


age()
