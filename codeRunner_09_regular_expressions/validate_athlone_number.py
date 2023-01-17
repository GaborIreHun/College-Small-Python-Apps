import re


def is_valid_athlone_landline_number(phone_number):
    match = re.fullmatch("090 64[0-9]{5}", phone_number)
    if match:
        return True
    else:
        return False
