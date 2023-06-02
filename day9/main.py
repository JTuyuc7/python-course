

# * Day 9 Dictionaries in python
import os
programming_dictionary = {"first": "This is the first element",
                          "second": 'This is the second elemenent on a dictinaory'}
# print(programming_dictionary)
# print(type(programming_dictionary))

# print(programming_dictionary["second"])

programming_dictionary["third"] = 'this will be our third item on the dictionarie'
# print(programming_dictionary)

#! Empty dictionary
empty_dictionary = {}

#! Update values from a dictionary
programming_dictionary["third"] = "This should have a totally new value"

# print(programming_dictionary)

#! loop on a dictionary
# for key in programming_dictionary:
#     print(programming_dictionary[key])

# * Excersice Day 9 No.1

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = "Outstanding"
#     elif score > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

# ^ Nested dictionaries

capitals = {
    "france": 'Paris',
    'Germany': 'Berlin'
}

# ^ Nesting a List in a dictionary

travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Sturllgart'], 'total_visits': 20}
}

# ^ Nesting Dictionary in a List
travel_log1 = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# def add_new_country(country, visited, cities):
#     temp_dic = {}

#     temp_dic['country'] = country
#     temp_dic['visits'] = visited
#     temp_dic['cities'] = cities

#     travel_log1.append(temp_dic)


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# print(travel_log1)


#^ Final Project

bids = {}
biding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for key in bidding_record:
        bid_amount = bidding_record[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f'The winner is {winner} with a bid of $ {highest_bid}')

while not biding_finished:
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))

    bids[name] = price
    response = input('Are there any other bidders? type "y" for yest, "n" for no \n')

    if (response == 'n'):
        biding_finished = True
    elif response == 'y':
        os.system('clear')

# print(bids, 'todoas las bids? que no se que sean xD')

find_highest_bidder(bids)