def hello_name(user_name):
    print(f"hello_{user_name}")


def first_odds():
    print([x for x in range(1, 101) if x % 2 == 1])


def max_num_in_list(list):
    return max(list)


def is_leap_year(a_year):
    """Returns true if the year is a leap year.  Leap year is divisible by 4 but not 100, unless also divisible by 400. If is divisible by 4 and 400, it's a leap year. If divisible by 4, not 400, and not 100, it's a leap year. If not divisible by 4, it's not a leap year.

    Args:
        a_year (int): A 4 digit year

    Returns:
        bool: True if it's a leap year, False if it's not.
    """
    year_bool = False
    if a_year % 4 == 0:
        if a_year % 400 == 0:
            year_bool = True
        if a_year != 100:
            year_bool = True
    return year_bool


def is_consecutive(num_list):
    """Returns True if the list of nums (or ASCII vals) is in consecutive order (+ or -1)

    Args:
        num_list (int): a list of integers

    Returns:
        bool: True if they are consecutive, False if not.
    """
    index = 0
    list_bool = False
    for num in num_list:
        if index == 0:
            index += 1
            continue
        if num_list[index] == num_list[index - 1] + 1:
            list_bool = True
        index += 1
    return list_bool


hello_name("mattdubbz")
first_odds()
print(max_num_in_list([x for x in range(99)]))
print(is_leap_year(2016))

# test with a consecutive list
print(is_consecutive([x for x in range(1, 27)]))
# test but non-consecutive list
print(is_consecutive([x for x in range(1, 10, 3)]))
