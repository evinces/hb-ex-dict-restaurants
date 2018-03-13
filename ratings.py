"""Restaurant rating lister."""
from sys import argv
from random import choice
from os import listdir
from os.path import isfile


def parse_file(filename):
    restaurant_ratings = {}

    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        word = line.split(":")
        restaurant_name = word[0]
        rating = word[1]
        restaurant_ratings[restaurant_name] = rating

    input_file.close()
    return restaurant_ratings


def print_sorted_ratings(restaurant_ratings):
    sorted_ratings = sorted(restaurant_ratings.items())

    for restaurant_name, rating in sorted_ratings:
        print "{} is rated at {}.".format(restaurant_name, rating)


def add_new_restaurant(restaurant_ratings):
    new_name = raw_input("Enter a restaurant name: ")

    new_rating = get_rating()

    restaurant_ratings[new_name] = new_rating


def update_random_restaurant(restaurant_ratings):
    random_restaurant = choice(restaurant_ratings.keys())
    print "{} is rated at {}.".format(random_restaurant,
                                      restaurant_ratings[random_restaurant])
    new_rating = get_rating()
    restaurant_ratings[random_restaurant] = new_rating


def update_restaurant(restaurant_ratings):
    restaurant_list = sorted(restaurant_ratings.keys())
    for index, name in enumerate(restaurant_list):
        print "{}. {}".format(index + 1, name)
    restaurant = int(raw_input("Choose a restaurant to update: "))
    if restaurant > 0 and restaurant < len(restaurant_list) + 1:
        new_rating = get_rating()
        restaurant_ratings[restaurant_list[restaurant - 1]] = new_rating
    else:
        print "No such restaurant."


def get_rating():
    while True:
        new_rating = int(raw_input("Enter a rating: "))
        if new_rating > 5 or new_rating < 1:
            print "Enter a rating between 1 and 5."
        else:
            break
    return new_rating


def choose_file():
    file_list = listdir(".")
    index = 1

    txt_list = []

    for filename in file_list:
        if filename[-4:] == ".txt":
            txt_list.append(filename)
            print "{}. {}".format(index, filename)
            index += 1

    while True:
        input_file = int(raw_input("Which file? "))

        if isfile(txt_list[input_file - 1]):
            return txt_list[input_file - 1]
        else:
            print "Invalid file name."


def print_highest_rated():
    file_list = listdir(".")

    all_restaurants = {}

    for filename in file_list:
        if filename[-4:] == ".txt":
            input_file = open(filename)
            for line in input_file:
                line = line.strip()
                word = line.split(":")
                restaurant_name = word[0]
                rating = word[1]
                all_restaurants[restaurant_name] = rating
            input_file.close()
    all_restaurants = sorted(all_restaurants.items(), key=lambda x: x[1], reverse=True)

    highest = all_restaurants[0][1]

    for restaurant_name, rating in all_restaurants:
        if rating != highest:
            break
        else:
            print "{} is rated at {}.".format(restaurant_name, rating)

if len(argv) < 2:
    filename = choose_file()
else:
    filename = argv[1]

restaurants = parse_file(filename)

while True:
    print "----------------------"
    print "Restaurant Ratings App"
    print ""
    print "1. See all ratings"
    print "2. Add a restaurant"
    print "3. Update random restaurant"
    print "4. Choose restaurant to update"
    print "5. Choose another file"
    print "6. See highest rated restaurant"
    print "7. Quit"
    print ""
    print "----------------------"
    print ""
    user_choice = raw_input("> ")
    print ""
    if user_choice == "1":
        print_sorted_ratings(restaurants)
    elif user_choice == "2":
        add_new_restaurant(restaurants)
    elif user_choice == "3":
        update_random_restaurant(restaurants)
    elif user_choice == "4":
        update_restaurant(restaurants)
    elif user_choice == "5":
        filename = choose_file()
        restaurants = parse_file(filename)
    elif user_choice == "6":
        print_highest_rated()
    else:
        break
    print ""
