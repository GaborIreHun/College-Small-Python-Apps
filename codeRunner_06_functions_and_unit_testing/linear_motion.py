
def calc_free_fall_height(time_elapsed, gravity=9.8):
    """
    Calculate the height of the free fall.

    :param time_elapsed: float
        The elapsed time.
    :param gravity: float, optional
        The acceleration due to gravity.

    :return: float
        The height of the free fall.
    """
    return (1/2 * gravity) * (time_elapsed ** 2)


if __name__ == "__main__":

    # Object dropped from the Leaning Tower of Pisa takes 3.375 seconds to fall under normal gravity
    print(f"Height fallen is {calc_free_fall_height(3.375):.3f} metres")

    # Height fallen in 10 seconds on the Moon (gravity 1.62 m/s²)
    print(f"Height fallen is {calc_free_fall_height(10, 1.62):.1f} metres")

    # Height fallen in 2.79 seconds on Mars (gravity 3.721 m/s²)
    print(f"Height fallen is {calc_free_fall_height(2.79, 3.721):.4f} metres")
