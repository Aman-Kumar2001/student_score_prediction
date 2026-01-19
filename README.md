<h1> Predicting Student Score (Kaggle Competetion)</h1>

<h3>Problem Statement</h3>

The goal of this project is to predict students’ final exam scores using available demographic, academic, and behavioral data. The task is framed as a regression problem, where the objective is to build a model that can accurately estimate a student’s performance based on patterns learned from historical data. The evaluation metric for this project is Root Mean Squared Error (RMSE), which measures how close the predicted scores are to the actual scores.

<h3>Project Approach</h3>

In this project, we will follow a structured, real-world machine learning workflow. We will begin with exploratory data analysis (EDA) to understand the dataset and feature distributions. Next, we will build a reproducible preprocessing pipeline for handling numerical and categorical features. Multiple regression models will be trained and evaluated using cross-validation, with a strong focus on avoiding data leakage. We will start with baseline models and progressively move to more advanced techniques such as gradient boosting, out-of-fold (OOF) training, and ensembling to improve generalization. The final model will be selected based on cross-validated performance and validated on the Kaggle leaderboard.