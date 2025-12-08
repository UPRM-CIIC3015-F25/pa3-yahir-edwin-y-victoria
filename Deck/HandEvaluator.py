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

RANK_TO_VALUE = {
    "ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11,
    "TEN": 10, "NINE": 9, "EIGHT": 8, "SEVEN": 7,
    "SIX": 6, "FIVE": 5, "FOUR": 4, "THREE": 3, "TWO": 2
}

HAND_MULTIPLIER = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 8,
    "Four of a Kind": 10,
    "Straight Flush": 12
}

def _values_from_hand(hand):
    vals, ranks = [], []
    for c in hand:
        name = c.rank.name if hasattr(c.rank, "name") else str(c.rank).upper()
        ranks.append(name)
        v = RANK_TO_VALUE.get(name)
        if v is not None:
            vals.append(v)
    return vals, ranks

def _is_consecutive(vals):
    if len(vals) < 5:
        return False
    vals = sorted(vals)
    for i in range(len(vals) - 4):
        window = vals[i:i+5]
        if all(window[j+1] - window[j] == 1 for j in range(4)):
            return True
    return False

def evaluate_hand(hand):
    if not hand:
        return "High Card"

    vals, ranks = _values_from_hand(hand)
    suits = [c.suit for c in hand]
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)
    counts = sorted(rank_counts.values(), reverse=True)

    flush_suit = None
    for s, c in suit_counts.items():
        if c >= 5:
            flush_suit = s
            break

    uvals = sorted(set(vals))
    low_ace = sorted(set(uvals + [1])) if 14 in uvals else uvals
    straight = _is_consecutive(uvals) or _is_consecutive(low_ace)

    if flush_suit:
        fv = sorted(set(
            RANK_TO_VALUE[c.rank.name] if hasattr(c.rank, "name") else RANK_TO_VALUE.get(str(c.rank).upper())
            for c in hand if c.suit == flush_suit
        ))
        fv_low = sorted(set(fv + [1])) if 14 in fv else fv
        if _is_consecutive(fv) or _is_consecutive(fv_low):
            return "Straight Flush"

    if counts[0] == 4:
        return "Four of a Kind"
    if counts[0] == 3:
        if len(counts) > 1 and counts[1] >= 2:
            return "Full House"
        return "Three of a Kind"

    pairs = [v for v in counts if v == 2]
    if len(pairs) >= 2:
        return "Two Pair"
    if len(pairs) == 1:
        return "One Pair"

    if flush_suit:
        return "Flush"
    if straight:
        return "Straight"

    return "High Card"

def hand_value(hand):
    """Devuelve el multiplicador basado en la mano evaluada"""
    hand_name = evaluate_hand(hand)
    return HAND_MULTIPLIER.get(hand_name, 1)
