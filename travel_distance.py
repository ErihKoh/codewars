def travel_distance(avg_speed, travel_time):
    KM_PER_MILE = 1.852
    travel_hours = travel_time / 60
    travel_kms = avg_speed * KM_PER_MILE
    return travel_kms


if __name__ == '__main__':
    avg_speed = 600
    travel_time = 60
    print(travel_distance(avg_speed, travel_time))
