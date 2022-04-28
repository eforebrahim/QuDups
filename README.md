# **QuDups**
# **Credits**: The project has been made following this [tutorial](https://youtu.be/1fvQU5yPjFs) with a lot of value addition.
# **For Live Demo click [here](https://duplicate-question-checker.herokuapp.com)**
# **Goal**
## Our goal is to create and deploy a model that predicts whether two questions are same or not. As Quora said while hosting this competition on Kaggle:

## "Currently, Quora uses a Random Forest model to identify duplicate questions. In this competition, Kagglers are challenged to tackle this natural language processing problem by applying advanced techniques to classify whether question pairs are duplicates or not. Doing so will make it easier to find high quality answers to questions resulting in an improved experience for Quora writers, seekers, and readers."

[![image-2022-04-29-010855400.png](https://i.postimg.cc/pdXZ768G/image-2022-04-29-010855400.png)](https://postimg.cc/dhprZn5r)
# Feature Enginerring, Modeling and Ensembling

## After creating 29 features like length of sentences, characters in sentences, fuzzy features, token features etc. and 2000 features using bag of words; lightGBM was used to classify whether two questions are duplicates or not. 4 LGBMs with different n_estimators were ensembled using soft VotingClassifier. The accuracy varied between 80 and 81.

# Deployment
## The WebApp was made using Streamlit and deployed on Heroku. Finally, deployed model will take two questions from user as input and give probability whether these questions are duplicates or not.
[![image-2022-04-28-061503739.png](https://i.postimg.cc/WbMzBgcG/image-2022-04-28-061503739.png)](https://postimg.cc/QHdj5BtC)
