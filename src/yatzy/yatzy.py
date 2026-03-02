"""
Yatzy Scoring Module
====================
Provides scoring logic for all categories of the Yatzy dice game.

Each scoring method receives five individual dice values (integers from 1 to 6)
or a list of dice, and returns the score according to the official rules.

Reference:
    https://sammancoaching.org/kata_descriptions/yatzy.html
"""


class Yatzy:
    """Scoring calculator for the Yatzy dice game."""

    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        """Initialize a Yatzy instance with five dice values.

        Args:
            d1-d5 (int): Individual die values (1–6).
        """
        self.dice = [d1, d2, d3, d4, d5]

    @staticmethod
    def _count_dice(d1: int, d2: int, d3: int, d4: int, d5: int) -> list[int]:
        """Return a frequency table of dice values.

        Args:
            d1-d5 (int): Individual die values (1–6).

        Returns:
            list[int]: A list of length 6 where index ``i`` holds the count of dice showing face ``i+1``.

        """
        counts = [0] * 6
        for die in (d1, d2, d3, d4, d5):
            counts[die - 1] += 1
        return counts

    @staticmethod
    def chance(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Return the sum of all five dice."""
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def yatzy(dice: list[int]) -> int:
        """Returns 50 points if all five dice show the same face; otherwise 0."""
        counts = [0] * 6
        for die in dice:
            counts[die - 1] += 1
        return 50 if 5 in counts else 0

    @staticmethod
    def ones(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all dice showing the face value 1."""
        return sum(d for d in (d1, d2, d3, d4, d5) if d == 1)

    @staticmethod
    def twos(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """ Returns the sum of all dice showing the face value 2."""
        return sum(d for d in (d1, d2, d3, d4, d5) if d == 2)

    @staticmethod
    def threes(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all dice showing the face value 3."""
        return sum(d for d in (d1, d2, d3, d4, d5) if d == 3)

    @staticmethod
    def fours(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all dice showing the face value 4."""
        return sum(d for d in (d1, d2, d3, d4, d5) if d == 4)

    @staticmethod
    def fives(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all dice showing the face value 5."""
        return sum(d for d in (d1, d2, d3, d4, d5) if d == 5)

    @staticmethod
    def sixes(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all dice showing the face value 6."""
        return sum(d for d in (d1, d2, d3, d4, d5) if d == 6)

    @staticmethod
    def score_pair(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of the two highest matching dice. If no pair exists, returns 0."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        for i in range(5, -1, -1):
            if counts[i] >= 2:
                return (i + 1) * 2
        return 0

    @staticmethod
    def two_pair(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all four dice that form exactly two distinct pairs.
        If fewer than two pairs exist, returns 0."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        pairs_found = 0
        score = 0
        for i in range(5, -1, -1):
            if counts[i] >= 2:
                pairs_found += 1
                score += (i + 1) * 2
        return score if pairs_found == 2 else 0

    @staticmethod
    def three_of_a_kind(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of the three matching dice. If no three-of-a-kind exists, returns 0."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        for i in range(6):
            if counts[i] >= 3:
                return (i + 1) * 3
        return 0

    @staticmethod
    def four_of_a_kind(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of the four matching dice. If no four-of-a-kind exists, returns 0."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        for i in range(6):
            if counts[i] >= 4:
                return (i + 1) * 4
        return 0

    @staticmethod
    def small_straight(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns 15 if the dice show exactly 1-2-3-4-5; otherwise 0."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        return 15 if counts[:5] == [1, 1, 1, 1, 1] else 0

    @staticmethod
    def large_straight(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns 20 if the dice show exactly 2-3-4-5-6; otherwise 0."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        return 20 if counts[1:] == [1, 1, 1, 1, 1] else 0

    @staticmethod
    def full_house(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        """Returns the sum of all five dice if the roll contains one pair and one three-of-a-kind of different face values.
        Five-of-a-kind does not qualify. Returns 0 for any other combination."""
        counts = Yatzy._count_dice(d1, d2, d3, d4, d5)
        has_pair = False
        has_three = False
        pair_face = 0
        three_face = 0

        for i, count in enumerate(counts):
            if count == 2:
                has_pair = True
                pair_face = i + 1
            elif count == 3:
                has_three = True
                three_face = i + 1

        if has_pair and has_three:
            return pair_face * 2 + three_face * 3
        return 0
