<h1> Analysis of Ridge, Random Forest and HistGradientBoost Model</h1>

Our data has already been cleaned and then we built 3 models and checked the performance using - root mean square metrics and compare them.

1. Ridge Model = 8.99
2. RandomForest Model = 8.94
3. HistGradientBoost Model = 8.76

Gradient Boosting model was great. Random Forest was not good at testing data, trying to do overfitting.

On taking the weighted combined result of Ridge and Gradient Boost Model - The performance was quite better. This means the model is trying to predict using Ridge and HGB better which was individually not possible by them.