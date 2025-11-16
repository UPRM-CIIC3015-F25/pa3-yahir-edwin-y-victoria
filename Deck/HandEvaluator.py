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
def evaluate_hand(hand: list[Card]):
    return "High Card" # If none of the above, it's High Card
from collections import Counter

RANK_TO_VALUE = {
    "A": 14, "K": 13, "Q": 12, "J": 11,
    "10": 10, "9": 9, "8": 8, "7": 7,
    "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

def _values_from_hand(hand):

    vals = []
    ranks = []
    for c in hand:
        r = str(c.rank)
        ranks.append(r)
        vals.append(RANK_TO_VALUE.get(r, None))
    return vals, ranks

def _is_consecutive(sorted_vals):
    if len(sorted_vals) < 5:
        return False
    for i in range(len(sorted_vals) - 4):
        window = sorted_vals[i:i+5]
        ok = True
        for j in range(4):
            if window[j+1] - window[j] != 1:
                ok = False
                break
        if ok:
            return True
    return False

def evaluate_hand(hand):
    if not hand:
        return "High Card"
    vals, ranks = _values_from_hand(hand)
    suits = [c.suit for c in hand]
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)
    counts_desc = sorted(rank_counts.values(), reverse=True)
    flush = False
    for suit, cnt in suit_counts.items():
        if cnt >= 5:
            flush = True
            flush_suit = suit
            break
    unique_vals = sorted(set(v for v in vals if v is not None))
    straight = False
    if 14 in unique_vals:
        unique_vals_with_ace_low = unique_vals + [1]
        unique_vals_with_ace_low = sorted(set(unique_vals_with_ace_low))
    else:
        unique_vals_with_ace_low = unique_vals
    if _is_consecutive(unique_vals):
        straight = True
    elif _is_consecutive(unique_vals_with_ace_low):
        straight = True
    if flush:
        flush_vals = sorted(set(RANK_TO_VALUE[str(c.rank)] for c in hand if c.suit == flush_suit))
        if 14 in flush_vals:
            fv_with_ace_low = sorted(set(flush_vals + [1]))
        else:
            fv_with_ace_low = flush_vals
        if _is_consecutive(flush_vals) or _is_consecutive(fv_with_ace_low):
            return "Straight Flush"
    if counts_desc and counts_desc[0] == 4:
        return "Four of a Kind"
    if len(counts_desc) >= 2 and counts_desc[0] == 3 and counts_desc[1] >= 2:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if counts_desc and counts_desc[0] == 3:
        return "Three of a Kind"
    if counts_desc.count(2) >= 2 or (len(counts_desc) >= 2 and counts_desc[0] == 2 and counts_desc[1] == 2):
        return "Two Pair"
    if 2 in counts_desc:
        return "One Pair"
    return "High Card"

