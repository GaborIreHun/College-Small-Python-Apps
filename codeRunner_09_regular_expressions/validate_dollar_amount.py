import re


def is_valid_dollar_amount(dollar_amount):
    match = re.fullmatch("^\$[0-9]+(\.[0-9]{2})?", dollar_amount)
    if match:
        return True
    else:
        return False

