# Project - Python for data analysis

## Dataset

This is the "Facebook Comment Volume Dataset" - https://archive.ics.uci.edu/ml/datasets/Facebook+Comment+Volume+Dataset.

- The dataset comes in 5 different variants. Each of these variants represents a base time for collection. I chose to only work with the first one : "Features_Variant_1"
- There are 54 attributes, one being the target output
- As the columns have no tags, let's add names to the attributes, as given on the UCI  website 
    - All the names are derived from their explanation in the papers related to the article (available in the presentation)

## Visualization

I did a lot of visualization, using different methods and tools provided in Python.

## Models & conclusion
 
I tried using three different models : Linear Regression, Random Forest et Gradient Boosting. I can't actually say that any of them was very accurate, but GB and RF were scoring quite well. After a GridSearch, RF gave decent results, and GB was always quite fine.

## API

To launch the flask app, juste run the api.py in a terminal, and the request.py in another.