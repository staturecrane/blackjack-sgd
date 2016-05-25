import numpy as np

def sig(z):
    return 1 / 1 - np.exp(-z)

def activate(z):
    z = sig(z)
    if z >= .5:
        return 1
    else:
        return -1

def update(i,j, error):
    weights[i,j] += rate * (i * error)
    
def update_b(b, error):
    b += rate * error
    return b

def get_errors(actual, prediction):
    return actual - prediction

def get_cost(error):
    return 0.5 * error**2

def net_input(i,j,bias):
    return weights[i,j] * i + bias

weights = np.zeros([21, 11])
bias = 1.0
rate = 0.0001

def fillShoe():
    suits = ["H","S","D","C"]
    num = ["A", "2", "3", "4", "5","6","7","8","9","10","J", "Q", "K"]
    deck = []

    for x in range(6):
        for i in suits:
            for j in num:
                deck.append(j + i)

    np.random.shuffle(deck)
    return deck

def getValue(card):
    if len(card) == 3:
        return int(card[0] + card[1])
    else:
        if card[0] == "A":
            return 11
        elif card[0] == "J" or card[0] == "K" or card[0] == "Q":
            return 10
        else:
            return int(card[0])
        
def sumHand(hand):
    sum = 0
    for i in hand:
        i = getValue(i)
        if i == 11 and i + sum > 21:
            sum += 1
        else:
            sum += i
    return sum 

def deal(deck):
    return deck.pop(0)

def decision(player, dealer, bias):
    return activate(net_input(player, dealer, bias))
    
def learn(hand):
    if hand > 20:
        return -1
    else:
        return 1
    
def updateWeights(player, dealer, delta):
    update(player, dealer, delta)

def playGame(weights, bias):
    deck = fillShoe()    
    player = []
    dealer = []
    
    player.append(deal(deck))
    dealer.append(deal(deck))
    player.append(deal(deck))
    dealer.append(deal(deck))
    
    p_hand = sumHand(player) - 1
    d_card = getValue(dealer[0]) - 1
    
    stay = decision(p_hand, d_card, bias)

    previous_hand = p_hand
    
    while stay != -1:
        player.append(deal(deck))
        p_hand = sumHand(player) - 1
        if p_hand > 20:
            output = net_input(previous_hand, d_card, bias)
            error = -1 - output
            update(previous_hand, d_card, error)
            
            return [get_cost(error), False]
        
        stay = decision(p_hand, d_card, bias)
        previous_hand = p_hand

    d_hand = sumHand(dealer)
    
    while d_hand <= 17:
        dealer.append(deal(deck))
        d_hand = sumHand(dealer)
        
    if d_hand > 21:
        output = net_input(p_hand, d_card, bias)
        error = 1 - output
        update(p_hand, d_card, error)
        return [get_cost(error), True]
    
    elif d_hand > p_hand:
        output = net_input(p_hand, d_card, bias)
        error = -1 - output
        update(p_hand, d_card, error)
        
        return [get_cost(error), False]
    
    elif p_hand > d_hand:
        output = net_input(p_hand, d_card, bias)
        error = 1 - output
        update(p_hand, d_card, error)
        
        return [get_cost(error), True]
    
    elif p_hand == d_hand:
        output = net_input(p_hand, d_card, bias)
        error = 1 - output
        update(p_hand, d_card, error)
        
        return [get_cost(error), True]

def countGame(boolean):
    if boolean:
        return 1
    else:
        return 0

errors = []
wins = 0

for l in range(10):
    wins = 0
    for z in range(10000):
        result = playGame(weights, bias)
        errors.append(result[0])
        wins += countGame(result[1])
    print(wins)
    wins = 0