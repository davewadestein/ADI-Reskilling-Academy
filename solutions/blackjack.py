from collections import namedtuple
import random
import time

Card = namedtuple('Card', 'rank suit')
ranks = [str(num) for num in range(2, 11)] + list('JQKA')

# The Unicode table has characters for the card suits...these are they
suits = '\u2663 \u2662 \u2661 \u2660'.split()

# Build the rank_to_value dict in 2 steps. First, add the picture cards.
# Next, add the numeric ranks. The | operator combines dictionaries.
rank_to_value = { 'A': 11, 'K': 10, 'Q': 10, 'J': 10 }
rank_to_value |= { str(rank): rank for rank in range(2, 11) }

# The hands dict holds each players hand. This makes it easy to access them
# and would make it somewhat easy to extend the game to multiple players.
hands = { 'dealer': [], 'player': [] }

pronouns = { 'dealer': 'I', 'player': 'You' }
possessives = { 'dealer': '  My', 'player': 'Your' }

# Global variables. The deck of cards and an index into the deck which indicates
# the next card to be dealt.
deck = [Card(rank, suit) for rank in ranks for suit in suits]
next_card = 0

def format_card(card):
    """Return a string representing a formatted card."""
    return f'{card.rank:>2}{card.suit}'


def show_hand(who, show_first=True, hold_last=False, show_total=True, show_possessive=True):
    """Print out the contents of a hand. A bit complicated so can make it look
    as though the dealer is dealing cards.

    Keyword arguments:
        show_first: determines whether we show just the latest card ('hit') or
        the entire hand
        hold_last: do we wait a second before showing the last card ('hit')?
        show_total: do we show the total value of the hand after?
        show_possessive: do we show "My hand:" or "Your hand:"
    """

    if show_possessive:
        print(f'{possessives[who]} hand: ', end=' ')
    if show_first:
        for card in hands[who][:-1]:
            print(format_card(card), end=' ', flush=True)
    if hold_last:
        time.sleep(1)
    print(format_card(hands[who][-1]), end=' ', flush=True)
    if hold_last:
        time.sleep(1)
    if show_total:
        print(f' ({value_of_hand(who)})')


def value_of_hand(who):
    """Total up the value of a hand. If the total exceeds 21 and there is an ace
    in the hand, devalue the ace to be worth 1 point instead of 11. Note that we
    may have to do that more than once!
    """
    ranks = [rank_to_value[card.rank] for card in hands[who]]
    while (total := sum(ranks)) > 21: # not a "bust" if hand contains an ace
        if 11 not in ranks:
            break
        ranks[ranks.index(11)] = 1 # if ace, count it as 1

    return total


def deal():
    """Deal two cards to player and dealer."""
    global next_card

    next_card = 0
    random.shuffle(deck)

    for hand in hands:
        hands[hand].clear()

    print()
    hit('player'), hit('dealer'), hit('player'), hit('dealer')
    show_hand('dealer'), show_hand('player')


def hit(who):
    """Grab the next card from the deck and return it."""
    global next_card

    card = deck[next_card]
    hands[who].append(card)
    next_card += 1

    return card


def blackjack(who):
    """Does a player have blackjack?"""
    return value_of_hand(who) == 21


def player_plays():
    """Allow player to hit or stand. Check for bust or an outright win."""
    while True:
        if (response := input('\n(h)it or (s)tand: ')) == 'h':
            hit('player')
            show_hand('player', hold_last=True)
            if (player_score := value_of_hand('player')) > 21:
                return 'bust'
            if player_score == 21: # stop, since player won't hit
                return '21'
            if player_won():
                return 'win'
        elif response == 's':
            print(f'\nPlayer stands at {value_of_hand("player")}.')
            return 'stand'
        else:
            print('Unknown response:', response)


def dealer_plays():
    """Play for the dealer. Hit on 16, stand on 17. Check for bust."""
    print()
    if (val := value_of_hand('dealer')) < 17:
        show_hand('dealer', hold_last=False, show_total=False, show_possessive=True)
        while (val := value_of_hand('dealer')) < 17:
            card = hit('dealer')
            show_hand('dealer', show_first=False,
                    show_total=False, hold_last=True, show_possessive=False)

        print(f' ({value_of_hand("dealer")})\n')

    if val > 21:
        print('Dealer busts!')
    else:
        print('Dealer stands.')


def player_won():
    """Did player win outright–in other words, check if dealer has at least 17
    and player has more than that. Only called in contexts where player cannot
    bust, so we don't check for that here.
    """
    dealer_score, player_score = value_of_hand('dealer'), value_of_hand('player')

    return dealer_score >= 17 and player_score > dealer_score


def see_who_wins():
    """With both players standing see who won."""
    dealer_score, player_score = value_of_hand('dealer'), value_of_hand('player')
    print()

    if player_score > dealer_score or dealer_score > 21:
        print('You win!')
    elif dealer_score > player_score:
        print('I win!')
    else:
        print('PUSH!')

# Until player wants to stop, deal a hand and ask player to hit or stand.
while (response := input("\nHit return to play (or 'q' for quit): ")) != 'q':
    deal()
    # If either player has a natural blackjack the hand is over. If BOTH have
    # blackjack, it's a PUSH.
    if blackjack('dealer') and blackjack('player'):
        see_who_wins() # It's a PUSH in this case
        continue
    if blackjack('dealer') or blackjack('player'):
        print('\nBLACKJACK!')
        see_who_wins()
        continue
    # Did player win outright, i.e., dealer has to stand and player has a
    # higher score?
    if player_won():
        print('\nYou win!')
        continue

    # Player didn't win outright, so see if player wants more cards.
    result = player_plays()
    time.sleep(1)
    if result == 'bust':
        print('\nBUST! You lose.')
        continue
    if result == 'blackjack':
        continue
    if result != 'win':
        dealer_plays()
    see_who_wins()
