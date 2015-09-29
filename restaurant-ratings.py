import sys

def sort_ratings():
    file_path = sys.argv[1]
    log_file = open(file_path)
    restaurant_ratings = {}

    for line in log_file:
        line = line.strip()
        rest_rating_list = line.split(":")

        restaurant_ratings[rest_rating_list[0]] = rest_rating_list[1]

    alphabetical_rest = sorted(restaurant_ratings)
    for restaurant in alphabetical_rest:
        print ("{} is rated at {}."
             .format(restaurant, restaurant_ratings[restaurant]))

sort_ratings()

