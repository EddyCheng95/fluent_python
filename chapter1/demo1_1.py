import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]





beer_card = Card('7', 'diamonds')
print('beer_card\n'+str(beer_card))

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])


from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

a = deck[:3]
print(a)
print(deck[12::13])

#实现了__getitem__方法，这一摞牌就变成可迭代的
print("迭代")
for card in deck: # doctest: +ELLTPSIS
    print(card)
#也可以反向迭代 tips：额。。。叫遍历更好吧
print("反向迭代")
for card in reversed(deck):
    print(card)


print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

#排序
print("排序")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

a = 0
for card in sorted(deck, key=spades_high):
    print(card)
    a += 1
print(a)