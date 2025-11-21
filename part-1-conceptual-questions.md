# Test
1. Classification Basics
a. Difference between classification and regression
- Classification predicts a category or class, like “spam or not spam.” It deals with labels.
- Regression predicts a number, like “house price” or “temperature.” It deals with continuous values.

b. Examples
Binary Classification (two classes):
- Predicting if an email is spam or not spam.
- Predicting if a student will pass or fail.
Multiclass Classification (more than two classes):
- Predicting the type of animal (cat, dog, bird).
- Predicting a grade level (A, B, C, D, F).

c. Definitions of evaluation metrics
- Accuracy – The percentage of correct predictions out of all predictions.
- Precision – Out of all the items the model marked as “positive,” how many were actually positive.
- Recall – Out of all the actual positive items, how many the model was able to find.
- F1 Score – The balance of precision and recall. Helpful when classes are not balanced.
- Confusion Matrix – A table that shows correct and wrong predictions for each class (true positive, true negative, false positive, false negative).

2. Logistic Regression
a. Why is logistic regression considered a classification algorithm, not a regression algorithm?
- Even if the name has “regression,” it produces a probability that is turned into a class label (like yes/no). So it is used for classification tasks, not for predicting a number.

b. What is the role of the sigmoid function in logistic regression?
- The sigmoid function turns any value into a number between 0 and 1. This helps the model decide if something belongs to a class (for example, if probability > 0.5, classify as “1”).

c. List two advantages and two disadvantages of logistic regression.

    Advantages:
        1. It is simple and easy to understand.
        2. It works well when the classes are clearly separated.

    Disadvantages:
        1. It does not perform well with complex or non-linear data.
        2. It can be sensitive to outliers and noise.

3. K-Nearest Neighbors (KNN)
a. What does it mean that KNN is a non-parametric and lazy learning algorithm?

    Non-parametric means KNN does not assume a fixed shape for the data. It learns only from the stored points.
    Lazy learning means it does not train before prediction. It only works when a new point needs to be classified.

b. Describe the steps of how KNN classifies a new data point.

    1. Store all training data points.
    2. When a new data point comes, calculate its distance from all stored points.
    3. Pick the K nearest points.
    4. Check their labels.
    5. The label that appears the most becomes the prediction.

c.  Explain how choosing a small K vs. a large K affects the model

    Small K:
        More sensitive to noise, may overfit, but can capture fine patterns.

    Large K:
        More stable, less noise, but may miss small patterns and may underfit.

d. Why is feature scaling (normalization/standardization) important for KNN?

    KNN uses distance to compare points. If features are not scaled, bigger-valued features will dominate the distance. Scaling makes all features contribute fairly.