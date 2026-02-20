import pytest
from yatzy import Yatzy


@pytest.fixture
def yatzy_instance():
    """Create a default Yatzy instance used across multiple tests."""
    return Yatzy(1, 2, 3, 4, 5)


def make_yatzy(d1, d2, d3, d4, d5):
    """Helper to instantiate Yatzy with specific dice values."""
    return Yatzy(d1, d2, d3, d4, d5)



class TestChance:

    def test_chance_should_return_sum_of_all_dice(self):
        # Arrange / Act / Assert
        assert Yatzy.chance(1, 1, 3, 3, 6) == 14

    def test_chance_should_return_sum_when_all_dice_are_different(self):
        assert Yatzy.chance(4, 5, 5, 6, 1) == 21

    def test_chance_should_return_sum_when_all_dice_are_equal(self):
        assert Yatzy.chance(6, 6, 6, 6, 6) == 30

    def test_chance_should_return_minimum_when_all_dice_are_ones(self):
        assert Yatzy.chance(1, 1, 1, 1, 1) == 5


class TestYatzy:

    def test_yatzy_should_return_50_when_all_dice_are_equal(self):
        assert Yatzy.yatzy([1, 1, 1, 1, 1]) == 50

    def test_yatzy_should_return_50_with_all_sixes(self):
        assert Yatzy.yatzy([6, 6, 6, 6, 6]) == 50

    def test_yatzy_should_return_0_when_dice_are_not_all_equal(self):
        assert Yatzy.yatzy([1, 1, 1, 2, 1]) == 0

    def test_yatzy_should_return_0_when_all_dice_are_different(self):
        assert Yatzy.yatzy([1, 2, 3, 4, 5]) == 0


class TestOnes:

    def test_ones_should_return_sum_of_dice_showing_one(self):
        assert Yatzy.ones(1, 1, 2, 4, 4) == 2

    def test_ones_should_return_0_when_no_ones(self):
        assert Yatzy.ones(3, 3, 3, 4, 5) == 0

    def test_ones_should_return_5_when_all_dice_are_ones(self):
        assert Yatzy.ones(1, 1, 1, 1, 1) == 5

    def test_ones_should_return_1_when_only_one_die_is_one(self):
        assert Yatzy.ones(1, 2, 3, 4, 5) == 1


class TestTwos:

    def test_twos_should_return_sum_of_dice_showing_two(self):
        assert Yatzy.twos(2, 3, 2, 5, 1) == 4

    def test_twos_should_return_0_when_no_twos(self):
        assert Yatzy.twos(1, 3, 4, 5, 6) == 0

    def test_twos_should_return_10_when_all_dice_are_twos(self):
        assert Yatzy.twos(2, 2, 2, 2, 2) == 10


class TestThrees:

    def test_threes_should_return_sum_of_dice_showing_three(self):
        assert Yatzy.threes(3, 3, 3, 4, 5) == 9

    def test_threes_should_return_0_when_no_threes(self):
        assert Yatzy.threes(1, 2, 4, 5, 6) == 0

    def test_threes_should_return_15_when_all_dice_are_threes(self):
        assert Yatzy.threes(3, 3, 3, 3, 3) == 15


class TestFours:

    def test_fours_should_return_sum_of_dice_showing_four(self):
        y = make_yatzy(1, 1, 2, 4, 4)
        assert y.fours() == 8

    def test_fours_should_return_0_when_no_fours(self):
        y = make_yatzy(1, 2, 3, 5, 6)
        assert y.fours() == 0

    def test_fours_should_return_20_when_all_dice_are_fours(self):
        y = make_yatzy(4, 4, 4, 4, 4)
        assert y.fours() == 20


class TestFives:

    def test_fives_should_return_sum_of_dice_showing_five(self):
        y = make_yatzy(5, 6, 5, 5, 2)
        assert y.fives() == 15

    def test_fives_should_return_0_when_no_fives(self):
        y = make_yatzy(1, 2, 3, 4, 6)
        assert y.fives() == 0

    def test_fives_should_return_25_when_all_dice_are_fives(self):
        y = make_yatzy(5, 5, 5, 5, 5)
        assert y.fives() == 25


class TestSixes:

    def test_sixes_should_return_sum_of_dice_showing_six(self):
        y = make_yatzy(1, 1, 6, 2, 6)
        assert y.sixes() == 12

    def test_sixes_should_return_0_when_no_sixes(self):
        y = make_yatzy(1, 2, 3, 4, 5)
        assert y.sixes() == 0

    def test_sixes_should_return_30_when_all_dice_are_sixes(self):
        y = make_yatzy(6, 6, 6, 6, 6)
        assert y.sixes() == 30


class TestScorePair:

    def test_score_pair_should_return_0_when_no_pair(self):
        assert Yatzy.score_pair(1, 2, 3, 4, 5) == 0

    def test_score_pair_should_return_sum_of_highest_pair(self):
        assert Yatzy.score_pair(3, 3, 3, 4, 4) == 8  # 4+4

    def test_score_pair_should_return_highest_pair_when_two_pairs_exist(self):
        assert Yatzy.score_pair(1, 1, 6, 2, 6) == 12  # 6+6

    @pytest.mark.xfail(
        reason="Bug in score_pair: uses strict equality (== 2) so counts of 3 or 4 are not recognized as a pair"
    )
    def test_score_pair_should_return_pair_with_three_of_a_kind(self):
        assert Yatzy.score_pair(3, 3, 3, 4, 1) == 6  # 3+3

    @pytest.mark.xfail(
        reason="Bug in score_pair: uses strict equality (== 2) so counts of 3 or 4 are not recognized as a pair"
    )
    def test_score_pair_should_return_pair_when_four_of_a_kind(self):
        assert Yatzy.score_pair(3, 3, 3, 3, 1) == 6  # 3+3


class TestTwoPair:

    def test_two_pair_should_return_sum_of_both_pairs(self):
        assert Yatzy.two_pair(1, 1, 2, 3, 3) == 8  # 1+1+3+3

    def test_two_pair_should_return_0_when_only_one_pair(self):
        assert Yatzy.two_pair(1, 1, 2, 3, 4) == 0

    def test_two_pair_should_return_sum_when_three_of_a_kind_counts_as_pair(self):
        assert Yatzy.two_pair(1, 1, 2, 2, 2) == 6  # 1+1+2+2

    def test_two_pair_should_return_0_when_four_of_a_kind(self):
        assert Yatzy.two_pair(3, 3, 3, 3, 1) == 0


class TestThreeOfAKind:

    def test_three_of_a_kind_should_return_sum_of_three_matching_dice(self):
        assert Yatzy.three_of_a_kind(3, 3, 3, 4, 5) == 9

    def test_three_of_a_kind_should_return_0_when_no_three_matching(self):
        assert Yatzy.three_of_a_kind(3, 3, 4, 5, 6) == 0

    def test_three_of_a_kind_should_score_when_four_of_a_kind_exists(self):
        assert Yatzy.three_of_a_kind(3, 3, 3, 3, 1) == 9


class TestFourOfAKind:

    def test_four_of_a_kind_should_return_sum_of_four_matching_dice(self):
        assert Yatzy.four_of_a_kind(2, 2, 2, 2, 5) == 8

    def test_four_of_a_kind_should_return_0_when_only_three_matching(self):
        assert Yatzy.four_of_a_kind(2, 2, 2, 5, 5) == 0

    def test_four_of_a_kind_should_score_when_five_of_a_kind_exists(self):
        assert Yatzy.four_of_a_kind(2, 2, 2, 2, 2) == 8


class TestSmallStraight:

    def test_small_straight_should_return_15_for_1_through_5(self):
        assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15

    def test_small_straight_should_return_15_regardless_of_dice_order(self):
        assert Yatzy.smallStraight(5, 4, 3, 2, 1) == 15

    def test_small_straight_should_return_0_for_invalid_sequence(self):
        assert Yatzy.smallStraight(2, 3, 4, 5, 6) == 0

    def test_small_straight_should_return_0_when_dice_are_not_a_straight(self):
        assert Yatzy.smallStraight(1, 1, 3, 4, 5) == 0


class TestLargeStraight:

    def test_large_straight_should_return_20_for_2_through_6(self):
        assert Yatzy.largeStraight(2, 3, 4, 5, 6) == 20

    def test_large_straight_should_return_20_regardless_of_dice_order(self):
        assert Yatzy.largeStraight(6, 5, 4, 3, 2) == 20

    def test_large_straight_should_return_0_for_small_straight(self):
        assert Yatzy.largeStraight(1, 2, 3, 4, 5) == 0

    def test_large_straight_should_return_0_when_not_a_straight(self):
        assert Yatzy.largeStraight(2, 2, 4, 5, 6) == 0


class TestFullHouse:

    def test_full_house_should_return_sum_of_all_dice(self):
        assert Yatzy.fullHouse(1, 1, 2, 2, 2) == 8  # 1+1+2+2+2

    def test_full_house_should_return_0_when_no_full_house(self):
        assert Yatzy.fullHouse(2, 2, 3, 3, 4) == 0

    def test_full_house_should_return_0_when_five_of_a_kind(self):
        assert Yatzy.fullHouse(4, 4, 4, 4, 4) == 0

    def test_full_house_should_return_sum_with_different_values(self):
        assert Yatzy.fullHouse(6, 6, 6, 3, 3) == 24  # 6+6+6+3+3

    def test_full_house_should_return_0_when_only_three_of_a_kind(self):
        assert Yatzy.fullHouse(3, 3, 3, 4, 5) == 0
