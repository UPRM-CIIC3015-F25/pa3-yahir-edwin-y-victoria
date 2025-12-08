from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
from collections import Counter

RANK_VALUES = {
    "ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11,
    "TEN": 10, "NINE": 9, "EIGHT": 8, "SEVEN": 7,
    "SIX": 6, "FIVE": 5, "FOUR": 4, "THREE": 3, "TWO": 2
}


def evaluate_hand(hand):
    if not hand:
        return "High Card"

    ranks = [RANK_VALUES[c.rank.name] if hasattr(c.rank, "name") else RANK_VALUES[str(c.rank).upper()] for c in hand]
    suits = [c.suit for c in hand]

    rank_count = Counter(ranks)
    suit_count = Counter(suits)

    flush = any(v >= 5 for v in suit_count.values())

    vals = sorted(set(ranks))
    if 14 in vals:
        vals.append(1)
    straight = any(vals[i + 4] - vals[i] == 4 for i in range(len(vals) - 4))

    if flush and straight:
        return "Straight Flush"
    if 4 in rank_count.values():
        return "Four of a Kind"
    if 3 in rank_count.values() and 2 in rank_count.values():
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if 3 in rank_count.values():
        return "Three of a Kind"
    if list(rank_count.values()).count(2) == 2:
        return "Two Pair"
    if 2 in rank_count.values():
        return "One Pair"
    return "High Card"



