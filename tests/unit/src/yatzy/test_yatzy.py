from src.yatzy.yatzy import Yatzy


class TestChance:

    def test_chance_should_return_sum_of_all_dice(self):
        # Arrange / Act / Assert
        assert Yatzy.chance(1, 1, 3, 3, 6) == 14

    def test_chance_should_return_sum_when_all_dice_are_different(self):
        # Arrange / Act / Assert
        assert Yatzy.chance(4, 5, 5, 6, 1) == 21

    def test_chance_should_return_sum_when_all_dice_are_equal(self):
        # Arrange / Act / Assert
        assert Yatzy.chance(6, 6, 6, 6, 6) == 30

    def test_chance_should_return_minimum_when_all_dice_are_ones(self):
        # Arrange / Act / Assert
        assert Yatzy.chance(1, 1, 1, 1, 1) == 5


class TestYatzy:

    def test_yatzy_should_return_50_when_all_dice_are_equal(self):
        # Arrange / Act / Assert
        assert Yatzy.yatzy([1, 1, 1, 1, 1]) == 50

    def test_yatzy_should_return_50_with_all_sixes(self):
        # Arrange / Act / Assert
        assert Yatzy.yatzy([6, 6, 6, 6, 6]) == 50

    def test_yatzy_should_return_0_when_dice_are_not_all_equal(self):
        # Arrange / Act / Assert
        assert Yatzy.yatzy([1, 1, 1, 2, 1]) == 0

    def test_yatzy_should_return_0_when_all_dice_are_different(self):
        # Arrange / Act / Assert
        assert Yatzy.yatzy([1, 2, 3, 4, 5]) == 0


class TestOnes:

    def test_ones_should_return_sum_of_dice_showing_one(self):
        # Arrange / Act / Assert
        assert Yatzy.ones(1, 1, 2, 4, 4) == 2

    def test_ones_should_return_0_when_no_ones(self):
        # Arrange / Act / Assert
        assert Yatzy.ones(3, 3, 3, 4, 5) == 0

    def test_ones_should_return_5_when_all_dice_are_ones(self):
        # Arrange / Act / Assert
        assert Yatzy.ones(1, 1, 1, 1, 1) == 5

    def test_ones_should_return_1_when_only_one_die_is_one(self):
        # Arrange / Act / Assert
        assert Yatzy.ones(1, 2, 3, 4, 5) == 1


class TestTwos:

    def test_twos_should_return_sum_of_dice_showing_two(self):
        # Arrange / Act / Assert
        assert Yatzy.twos(2, 3, 2, 5, 1) == 4

    def test_twos_should_return_0_when_no_twos(self):
        # Arrange / Act / Assert
        assert Yatzy.twos(1, 3, 4, 5, 6) == 0

    def test_twos_should_return_10_when_all_dice_are_twos(self):
        # Arrange / Act / Assert
        assert Yatzy.twos(2, 2, 2, 2, 2) == 10


class TestThrees:

    def test_threes_should_return_sum_of_dice_showing_three(self):
        # Arrange / Act / Assert
        assert Yatzy.threes(3, 3, 3, 4, 5) == 9

    def test_threes_should_return_0_when_no_threes(self):
        # Arrange / Act / Assert
        assert Yatzy.threes(1, 2, 4, 5, 6) == 0

    def test_threes_should_return_15_when_all_dice_are_threes(self):
        # Arrange / Act / Assert
        assert Yatzy.threes(3, 3, 3, 3, 3) == 15


class TestFours:

    def test_fours_should_return_sum_of_dice_showing_four(self):
        # Arrange / Act / Assert
        assert Yatzy.fours(1, 1, 2, 4, 4) == 8

    def test_fours_should_return_0_when_no_fours(self):
        # Arrange / Act / Assert
        assert Yatzy.fours(1, 2, 3, 5, 6) == 0

    def test_fours_should_return_20_when_all_dice_are_fours(self):
        # Arrange / Act / Assert
        assert Yatzy.fours(4, 4, 4, 4, 4) == 20        


class TestFives:

    def test_fives_should_return_sum_of_dice_showing_five(self):
        # Arrange / Act / Assert
        assert Yatzy.fives(5, 6, 5, 5, 2) == 15

    def test_fives_should_return_0_when_no_fives(self):
        # Arrange / Act / Assert
        assert Yatzy.fives(1, 2, 3, 4, 6) == 0

    def test_fives_should_return_25_when_all_dice_are_fives(self):
        # Arrange / Act / Assert
        assert Yatzy.fives(5, 5, 5, 5, 5) == 25


class TestSixes:

    def test_sixes_should_return_sum_of_dice_showing_six(self):
        # Arrange / Act / Assert
        assert Yatzy.sixes(1, 1, 6, 2, 6) == 12

    def test_sixes_should_return_0_when_no_sixes(self):
        # Arrange / Act / Assert
        assert Yatzy.sixes(1, 2, 3, 4, 5) == 0

    def test_sixes_should_return_30_when_all_dice_are_sixes(self):
        # Arrange / Act / Assert
        assert Yatzy.sixes(6, 6, 6, 6, 6) == 30


class TestScorePair:

    def test_score_pair_should_return_0_when_no_pair(self):
        # Arrange / Act / Assert
        assert Yatzy.score_pair(1, 2, 3, 4, 5) == 0

    def test_score_pair_should_return_sum_of_highest_pair(self):
        # Arrange / Act / Assert
        assert Yatzy.score_pair(3, 3, 3, 4, 4) == 8

    def test_score_pair_should_return_highest_pair_when_two_pairs_exist(self):
        # Arrange / Act / Assert
        assert Yatzy.score_pair(1, 1, 6, 2, 6) == 12


class TestTwoPair:

    def test_two_pair_should_return_sum_of_both_pairs(self):
        # Arrange / Act / Assert
        assert Yatzy.two_pair(1, 1, 2, 3, 3) == 8

    def test_two_pair_should_return_0_when_only_one_pair(self):
        # Arrange / Act / Assert
        assert Yatzy.two_pair(1, 1, 2, 3, 4) == 0

    def test_two_pair_should_return_sum_when_three_of_a_kind_counts_as_pair(self):
        # Arrange / Act / Assert
        assert Yatzy.two_pair(1, 1, 2, 2, 2) == 6

    def test_two_pair_should_return_0_when_four_of_a_kind(self):
        # Arrange / Act / Assert
        assert Yatzy.two_pair(3, 3, 3, 3, 1) == 0


class TestThreeOfAKind:

    def test_three_of_a_kind_should_return_sum_of_three_matching_dice(self):
        # Arrange / Act / Assert
        assert Yatzy.three_of_a_kind(3, 3, 3, 4, 5) == 9

    def test_three_of_a_kind_should_return_0_when_no_three_matching(self):
        # Arrange / Act / Assert
        assert Yatzy.three_of_a_kind(3, 3, 4, 5, 6) == 0

    def test_three_of_a_kind_should_score_when_four_of_a_kind_exists(self):
        # Arrange / Act / Assert
        assert Yatzy.three_of_a_kind(3, 3, 3, 3, 1) == 9


class TestFourOfAKind:

    def test_four_of_a_kind_should_return_sum_of_four_matching_dice(self):
        # Arrange / Act / Assert
        assert Yatzy.four_of_a_kind(2, 2, 2, 2, 5) == 8

    def test_four_of_a_kind_should_return_0_when_only_three_matching(self):
        # Arrange / Act / Assert
        assert Yatzy.four_of_a_kind(2, 2, 2, 5, 5) == 0

    def test_four_of_a_kind_should_score_when_five_of_a_kind_exists(self):
        # Arrange / Act / Assert
        assert Yatzy.four_of_a_kind(2, 2, 2, 2, 2) == 8


class TestSmallStraight:

    def test_small_straight_should_return_15_for_1_through_5(self):
        # Arrange / Act / Assert
        assert Yatzy.small_straight(1, 2, 3, 4, 5) == 15

    def test_small_straight_should_return_15_regardless_of_dice_order(self):
        # Arrange / Act / Assert
        assert Yatzy.small_straight(5, 4, 3, 2, 1) == 15

    def test_small_straight_should_return_0_for_invalid_sequence(self):
        # Arrange / Act / Assert
        assert Yatzy.small_straight(2, 3, 4, 5, 6) == 0

    def test_small_straight_should_return_0_when_dice_are_not_a_straight(self):
        # Arrange / Act / Assert
        assert Yatzy.small_straight(1, 1, 3, 4, 5) == 0


class TestLargeStraight:

    def test_large_straight_should_return_20_for_2_through_6(self):
        # Arrange / Act / Assert
        assert Yatzy.large_straight(2, 3, 4, 5, 6) == 20

    def test_large_straight_should_return_20_regardless_of_dice_order(self):
        # Arrange / Act / Assert
        assert Yatzy.large_straight(6, 5, 4, 3, 2) == 20

    def test_large_straight_should_return_0_for_small_straight(self):
        # Arrange / Act / Assert
        assert Yatzy.large_straight(1, 2, 3, 4, 5) == 0

    def test_large_straight_should_return_0_when_not_a_straight(self):
        # Arrange / Act / Assert
        assert Yatzy.large_straight(2, 2, 4, 5, 6) == 0


class TestFullHouse:

    def test_full_house_should_return_sum_of_all_dice(self):
        # Arrange / Act / Assert
        assert Yatzy.full_house(1, 1, 2, 2, 2) == 8

    def test_full_house_should_return_0_when_no_full_house(self):
        # Arrange / Act / Assert
        assert Yatzy.full_house(2, 2, 3, 3, 4) == 0

    def test_full_house_should_return_0_when_five_of_a_kind(self):
        # Arrange / Act / Assert
        assert Yatzy.full_house(4, 4, 4, 4, 4) == 0

    def test_full_house_should_return_sum_with_different_values(self):
        # Arrange / Act / Assert
        assert Yatzy.full_house(6, 6, 6, 3, 3) == 24

    def test_full_house_should_return_0_when_only_three_of_a_kind(self):
        # Arrange / Act / Assert
        assert Yatzy.full_house(3, 3, 3, 4, 5) == 0
