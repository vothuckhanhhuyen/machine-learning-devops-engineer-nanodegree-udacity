## Key Points

- We perform data validation in order to verify that our assumptions about the data are correct and stay correct even for new datasets. This latter point is not guaranteed. Indeed, the data can change for many reasons:
    - Bugs are introduced upstream (for example in ETL pipelines)
    - Changes in the source of the data are not communicated properly and produce unexpected changes in the input data
    - The world changes and the distribution of the input data changes

- Running the tests: If the tests are within the tests directory, we can run all the tests with (the -vv option means verbose, and it yields a more pleasant visualization of the results):
```
pytest tests/ -vv
```

- [Great Expectations](https://greatexpectations.io/) is an alternative tool to validate, document, and profile your data. It provides:
    - A rich set of pre-defined tests
    - Automatic profiling: it can generate a set of tests based on an input dataset, that can then be applied to a different dataset
    - HTML reports showing histograms and other useful information about the dataset
    - However, it has a pretty steep learning curve.

## Key Terms

- Alternative Hypothesis: In statistical hypothesis testing, the alternative hypothesis is a statement that contradicts the null hypothesis.

- Deterministic Test: A test that involves a measurement without randomness. For example, measuring the number of columns in a table.

- ETL Pipelines: Extract Transform Load pipelines. They are a classic structure for data pipelines. An ETL pipeline is used to fetch, preprocess and store a dataset.

- Hypothesis Testing: A statistical method to test a null hypothesis against an alternative hypothesis. The main element of HT is a statistical test.

- Non-Deterministic Test: A test that involves a measurement of a random variable, i.e., of a quantity with intrinsic randomness. Examples are the mean or standard deviation from a sample from a population. If you take two different samples, even from the same population, they will not have exactly the same mean and standard deviation. A non-deterministic test uses a statistical test to determine whether an assumption about the data is likely to have been violated.

- Null Hypothesis: In statistical hypothesis testing, the null hypothesis is the assumption that we want to test. For example, in case of the t-test the null hypothesis is that the two samples have the same mean.

- P-Value: The probability of measuring by chance a value for the Test Statistic equal or more extreme than the one observed in the data assuming that the null hypothesis is true.

- Statistical Test: An inference method to determine whether the observed data is likely or unlikely to occur if the null hypothesis is true. It typically requires the specification of an alternative hypothesis, so that a Test Statistic (TS) can be formulated and the expected distribution of TS under the null hypothesis can be derived. A statistical test is characterized by a false positive rate alpha (probability of Type I error) and a false negative rate beta (probability of a Type II error). There are many statistical tests available, depending on the null and the alternative hypothesis that we want to probe.

- Test Statistic: A random variable that can be computed from the data. The formula for the TS is specified by the appropriate statistical test that can be chosen once a null hypothesis and an alternative hypothesis have been formulated. For example, to test whether two samples have the same mean (null hypothesis) or a different mean (alternative hypothesis) we can use the t-test. The t-test specifies how to compute the TS appropriate for this case, as well as what is the expected distribution of TS under the null hypothesis.