def check_age(age):
    if age < 0:
        raise ValueError('age cannot be negative')

    if age >= 18:
        return "you are adult"
    else:
        return "you are minor"


# print(check_age(-17))


def book_ticket(number):
    if number <= 0:
        raise Exception('ticket count must be greater then zero')
    print(f"successfully booked{number} tickets")


# book_ticket(-3)
# book_ticket(0)
book_ticket(3)
