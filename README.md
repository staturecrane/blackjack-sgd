# Basic Blackjack SGD

A very simple bot using online (or realtime) stochastic gradient descent to play a simplified version of blackjack without splitting or doubling down. The only depdency is NumPy.

#Parameters

The parameters for the game are a single of matrix of real numbers, 21 X 11, with the number of rows matching the potential player points and the columns representing the potential dealer points. Since the dealer's hand only shows one card while the player takes her turn, we are only cocerned with 11 possible dealer values.

Each parameter corresponds to a single player/dealer hand combination. To hit, we use a logistic function to squash the dot product of the sum of the player's hand and the corresponding player/dealer parameter. We use the logistic to determine whether or not to hit, but a cost function to determine the error and update our paramters. 
