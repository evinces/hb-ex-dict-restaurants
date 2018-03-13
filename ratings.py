"""Restaurant rating lister."""
from os import listdir
from random import choice
from sys import argv


def add_new_restaurant(ratings):
    """Prompt user to add new restaurant rating"""

    print "Enter a restaurant name:"
    new_name = raw_input("> ")

    print "Enter a rating:"
    ratings[new_name] = get_rating()

    print_rating(new_name, ratings[new_name])


def get_int():
    """Get an integer from the user"""

    while True:
        try:
            choice = int(raw_input("> "))
            return choice
        except ValueError:
            print "Error: Enter a number"


def get_int_in_range(upper_bound):
    """Get an integer within range 1 and upper_bound inclusive"""

    while True:
        input_int = get_int()
        if 1 <= input_int <= upper_bound:
            return input_int
        else:
            print "Error: Enter a value between 1 and {}".format(upper_bound)


def get_rating():
    """Get an integer between 1 and 5 inclusive"""

    return get_int_in_range(5)


def get_new_file():
    """Prompt user to select a new .txt file from local dir"""

    file_list = listdir(".")
    txt_list = []

    for file_name in file_list:
        if file_name[-4:] == ".txt":
            txt_list.append(file_name)

    for index, name in enumerate(txt_list):
        print "  {}. {}".format(index + 1, name)

    print ""
    print "Enter a file selection:"
    file_selection = get_int_in_range(len(txt_list)) - 1
    return txt_list[file_selection]


def parse_file(file_name, ratings={}):
    """Parse data from file_name, store in ratings_dict"""

    file_in = open(file_name)
    for line in file_in:
        line = line.strip()
        words = line.split(":")
        ratings[words[0]] = words[1]

    file_in.close()
    return ratings


def print_highest_rated():
    """Load all .txt files in local dir and print the highest rated"""

    all_ratings = {}

    file_list = listdir(".")
    for file_name in file_list:
        if file_name[-4:] == ".txt":
            all_ratings = parse_file(file_name, all_ratings)

    all_ratings = sorted(all_ratings.items(), key=lambda x: x[1], reverse=True)
    highest = all_ratings[0][1]

    for name, rating in all_ratings:
        if rating == highest:
            print_rating(name, rating)
        else:
            break


def print_sorted_ratings(ratings):
    """Print alphabetized list of restaurants followed by their rating"""

    for name, rating in sorted(ratings.items()):
        print_rating(name, rating)


def print_rating(name, rating):
    """Print restaurant followed by rating"""

    print "     {} is rated: {}".format(name, rating)


def update_random_restaurant(ratings):
    """Prompt user to rate random restaurant"""

    rand_name = choice(ratings.keys())
    print_rating(rand_name, ratings[rand_name])

    print ""
    print "Enter a new rating:"
    ratings[rand_name] = get_rating()

    print ""
    print_rating(rand_name, ratings[rand_name])


def update_restaurant(ratings):
    """Prompt user to select a restaurant to update"""

    sorted_names = sorted(ratings.keys())
    for index, name in enumerate(sorted_names):
        print "     {}. {}".format(index + 1, name)

    print ""
    print "Enter a restaurant selection:"
    user_choice = sorted_names[get_int_in_range(len(sorted_names)) - 1]
    print "Enter a rating:"
    ratings[user_choice] = get_rating()

    print ""
    print_rating(user_choice, ratings[user_choice])


line_width = 80

title = """{}
 Restaurant Ratings App
{}""".format("=" * line_width, "=" * line_width)

menu = """
  1. See all ratings in this file
  2. Add a restaurant to this file
  3. Update a random restaurant
  4. Update a specified restaurant
  5. Choose another ratings file
  6. See highest rated restaurant across all files
  7. See this menu again
  8. Quit
"""

print ""
print title

if len(argv) > 1:
    file_name = argv[1]
else:
    file_name = get_new_file()

ratings = parse_file(file_name)

print menu
while True:
    print "-" * line_width
    user_choice = get_int_in_range(8)
    print "-" * line_width
    print ""

    if user_choice == 1:
        print_sorted_ratings(ratings)

    elif user_choice == 2:
        add_new_restaurant(ratings)

    elif user_choice == 3:
        update_random_restaurant(ratings)

    elif user_choice == 4:
        update_restaurant(ratings)

    elif user_choice == 5:
        file_name = get_new_file()
        ratings = parse_file(file_name)

    elif user_choice == 6:
        print_highest_rated()

    elif user_choice == 7:
        print menu

    elif user_choice == 8:
        break

    print ""
