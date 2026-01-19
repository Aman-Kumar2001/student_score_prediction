<h1> K Fold and MultiSeed Model Analysis </h1>

<h3> K Fold Method </h3>
K Fold method is used using individually models - Ridge and HGB, surprisingly in this case only HGB alone was performing much better than combining the two.

Ridge Model using K Fold(rmse value) = 8.89
HGB Model using K Fold(rmse value) = 8.76
Combined using K Fold(rmse value) = 8.8 (approx)

HGB Model performing best among all.

<h3> Multi Seed Method </h3>
Taking HGB Model, the model was trained for different values of seeds in random_state. Surprisingly for different random States, the rmse value was coming to be different.

Averaging the predicted values, and then calculated the rmse, the model gaved the best results.

Why this worked - HGB models works stochastically, setting differnt seed for random state allows the model to take diifferent data points which may be left earlier during training, which helped the model train more well and the result shows it.