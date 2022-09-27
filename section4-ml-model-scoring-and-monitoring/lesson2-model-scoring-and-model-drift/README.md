## Key Points

- Automatic scoring: reading saved models, making predictions, and comparing predictions to actual values - all automatically
    + Model drift is a term that refers to the degradation or decrease in a model's performance over time. It's important to check the performance of your model frequently to ensure that its performance remains high and model drift doesn't occur.
    + We train ML models to make sure they're as accurate as possible. But usually, model performance gets worse as models get older. There are a few things that can cause model performance to decrease over time:
        + Changes in the target variable: in the example illustrated above, you can see a hypothetical ML model predicting house prices. When prices change, as they do almost constantly, a previously trained model will become less accurate, and obsolete.
        + Changes in the predictor variable: if the model was trained to predict prices of houses with 2 or 3 bedrooms, but builders start to build houses with 4 or 5 bedrooms, it's possible that the model will perform worse because the predictor variable is outside the range where the model was trained.
        + Changes in the relationship between predictor and target: many factors, such as utility prices, changing tastes, and new technology, can cause the relationship between predictors and targets to change, which can make models perform worse.
    + The world is always changing. Changes in the world can cause models to perform worse over time - in other words, it can cause models to drift. You need to constantly check for model drift, and retrain and re-deploy your models whenever drift occurs.
    + Model scoring is a straightforward idea: we have to compare predictions to actual values. The difference between predicted and actual values is the model's score.
    + Scoring is a model is important because it shows us how we expect a model to perform in production. It's also important because it allows us to check for model drift. It doesn't need to be a very hard process, and we can fully automate it.

- Record keeping: generating and saving records of model performance
    + Recording model scores is a straightforward process:
        + First, read historical records into your Python session.
        + Next, perform model scoring, as we went over earlier in this lesson. Make sure the score you calculate is the same type of score as the scores in your historical records. Also, make sure you use the most recently deployed ML model to calculate scores.
        + Finally, write a record of all previous and current scores to your workspace.

- Model drift: how to measure and reason about changing model performance over time
    + In some cases, the raw comparison test is too sensitive, it will tell us that model drift occurred even in cases where the newest model is only very slightly worse than previous models.
    + In order to avoid this sensitivity, we can try a different test: the "parametric significance test." This test will check the standard deviation of all previous scores. Then, it will conclude that a new model has worse performance than previous models if the new model score is more than two standard deviations lower than the mean of all the previous scores.
    + The parametric significance test relies on the standard deviation of previous scores. In some cases, the standard deviation can lead to misleading conclusions. This can be especially true if your data isn't distributed like a bell curve, or if it has many outliers.
    + In cases where we don't want to use the parametric significance test, we can use another, similar test called the "non-parametric outlier test." Instead of the standard deviation, this test uses the interquartile range: the difference between the 75th percentile and the 25th percentile. A model score is regarded as an extreme value if it is either:
        + more than 1.5 interquartile ranges above the 75th percentile (a high outlier)
        + more than 1.5 interquartile ranges below the 25th percentile (a low outlier)
    + If a model score is worse than previous scores to an extent that it's an outlier (either a high or low outlier), then the non-parametric outlier test concludes that model drift has occurred.

- Hypothesis testing: using tools from statistics to compare the performance of different models

## Key Terms

- For your reference, here are all the new terms we introduced in this lesson:
    + F1 score: a common metric for measuring classification accuracy (higher scores are better).
    + reshape(): a method for changing the shape of data to prepare it for ML predictions.
    + r-squared: a metric used to measure model performance for regressions (between 0 and 1, the higher the better)
    sum of squared errors (SSE): a metric used to measure model performance for regressions: (0 or higher, the lower the better)
    + raw comparison test: a test for model drift that consists of checking whether a new model score is worse than all previous scores
    + parametric significance test: a test model drift that consists of checking whether a new model score is more than 2 standard deviations worse than the mean of all previous scores
    + non-parametric outlier test: a test for model drift that consists of checking whether a new score is more than 1.5 interquartile ranges worse than the 25th or 75th percentile of previous scores
    + standard deviation: a measure of how far spread apart the observations in a dataset are
    interquartile range: the difference between the 75th percentile and the 25th percentile of a set of observations
    + p-value: a numerical result from a t-test used to determine whether two sets of numbers differ
    + t-test: a statistical test for comparing two sets of numbers
    + statistical significance: a concept describing the degree of evidence that two sets differ

- In this lesson, we learned how to score models and check for model drift. We covered all of the following topics:
    + Automatic model scoring: how to read data and score models automatically
    + Recording model scores: how to keep persistent records of model scores in your workspace
    + Model drift: how to perform several different tests to check for model drift
    + Hypothesis testing: how to use statistical tests to compare two different models