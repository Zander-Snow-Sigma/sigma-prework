from datetime import date

today = date.today()

user_dob = input("Please enter your date of birth in the formt dd-mm-yyyy: ")

list_dob = user_dob.split("-")

date_dob = date(int(list_dob[2]), int(list_dob[1]), int(list_dob[0]))


def dob_later(dob):
    return today.month < dob.month or today.month == dob.month and today.day < dob.day


def calc_age(dob):
    age = today.year - dob.year

    if dob_later(dob):
        age -= 1

    return age


print(calc_age(date_dob))
