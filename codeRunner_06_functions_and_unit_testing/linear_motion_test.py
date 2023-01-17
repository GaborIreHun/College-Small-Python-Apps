from linear_motion import calc_free_fall_height
from pytest import approx


def test_calc_free_fall_height():
    assert calc_free_fall_height(3.375) == approx(55.814, 0.001)
    assert calc_free_fall_height(10, 1.62) == approx(81.0, 0.1)
    assert calc_free_fall_height(2.79, 3.721) == approx(14.4823, 0.0001)
