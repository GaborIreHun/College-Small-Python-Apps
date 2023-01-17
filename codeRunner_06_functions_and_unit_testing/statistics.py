
def calc_mean(numbers):
    """
    Calculate the mean of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The mean of a list of numbers.
    """
    return sum(numbers) / len(numbers)


def calc_median(numbers):
    """
    Calculate the median of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float, int
        The mean of a list of numbers.
    """
    numbers.sort()
    if len(numbers) % 2 == 0:
        med1 = numbers[len(numbers) // 2]
        med2 = numbers[len(numbers) // 2 - 1]
        return (med1 + med2) / 2
    else:
        return numbers[len(numbers) // 2]


def calc_mode(numbers):
    """
    Calculate the mode of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float, int
        The mode of a list of numbers.
    """
    uniques = sorted(set(numbers))
    frequencies = [numbers.count(value) for value in uniques]
    max_frequencies = max(frequencies)
    max_freq_index = frequencies.index(max_frequencies)

    return uniques[max_freq_index]


def calc_iqr(numbers):
    """
    Calculate the Interquartile Range of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The Interquartile Range of a list of numbers.
    """
    numbers.sort()
    mid_index = int(len(numbers) / 2)

    if len(numbers) % 2 == 0:
        lower_half = numbers[:mid_index]
        upper_half = numbers[mid_index:]
    else:
        lower_half = numbers[:mid_index]
        upper_half = numbers[mid_index + 1:]

    q1 = calc_median(lower_half)
    q3 = calc_median(upper_half)

    return q3 - q1


def calc_std_dev(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    :param numbers: float, int
        List of numbers.
        
    :return: float
        The standard deviation of a list of numbers.
    """
    return (sum((x-(calc_mean(numbers)))**2 for x in numbers) / (len(numbers)-1))**0.5


def calc_median_skewness(numbers):
    """
    Calculate the median skewness of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The median skewness of a list of numbers.
    """
    return 3 * (calc_mean(numbers) - calc_median(numbers)) / calc_std_dev(numbers)


def calc_mode_skewness(numbers):
    """
    Calculate the mode skewness of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The mode skewness of a list of numbers.
    """
    return (calc_mean(numbers) - calc_mode(numbers)) / calc_std_dev(numbers)




