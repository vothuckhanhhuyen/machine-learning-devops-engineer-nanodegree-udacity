## Key Points

- The following are operational issues that we'll discuss in this lesson:
    + Missing data: when you ingest new data, you may find that some entries are missing. Missing data can cause your model to make inaccurate predictions.
    + Unstable data: you may find that the data is not stable, that its values and means have changed substantially. Unstable data can also lead to inaccurate predictions.
    + Timing problems: some parts of your project may suddenly have delays and timing problems. This can cause your predictions to arrive late or not arrive at all.
    + Dependency issues: some modules that your code depends on may be outdated or buggy. This can cause your model to make inaccurate or useless predictions.

- Process timing: how to measure the timing of your project's ML processes
    + Timing a process in Python follows the same logic as timing a process in the real world:
        + Start a timer or stopwatch.
        + At the moment when the timer starts, or as soon as possible afterward, begin the process you want to time.
        + The process that you're timing ends.
        + At the moment when the process ends, or as soon as possible afterward, stop the timer or stopwatch.

- Integrity and stability: how to diagnose integrity and stability issues in data
    + Integrity: a dataset's state of being fully intact, with no missing or invalid entries
    + Stability: the similarity of data values between consecutive versions of datasets
    + Imputation: making educated guesses about the correct values of NA entries

- Dependencies: understanding the third-party modules your code depends on
    + We can use the software tool called pip to install and work with Python dependencies. The following are some useful pip commands that you can run from your workspace's command line:
        + pip list (return a list of all installed Python modules)
        + pip list --outdated (show only the outdated modules)
        + pip freeze (provides an output in “requirements format”)
        + pip show pandas(provide specific information an installed module)
        + pip install pandas (installs modules)
        + python -m pip list (run pip through Python)

- Data imputation: an important method for resolving data integrity issues
    + zero imputation: the simplest possible way to make guesses about data is to simply guess that all missing values are equal to zero. This is simple and easy, although it's rarely highly accurate.
    + mean imputation: you can take the means of every column of your data, and set every missing entry to be equal to the mean of the column where it appears.
    + regression imputation: you can use linear regression to predict the value of each missing data entry, and replace every missing entry with the regression prediction.

## Key Terms

- This lesson was about diagnosing and resolving operational issues. In this lesson, you learned how to:
    + Time ML processes, and determine whether there are speed or latency issues
    + Check for integrity and stability issues in data
    + Check for dependencies, and resolve dependency issues
    + Perform data imputation: a method for resolving data integrity problems

- For your reference, here are all the new terms we introduced in this lesson:
    + latency: Latency refers to the time delay in a program or the amount of time one part of your program has to wait for another part. If your processes take a long time to execute, it can cause latency in your project, and this could cause problems.
    + timestamp: a timestamp is a representation of a specific date and time in a standard format. Modules related to time and timing often record timestamps to keep track of when processes begin and end.
    + timeit: the name of the module that we've used as a timer in this lesson.
    + integrity: a dataset's state of being fully intact, with no missing or invalid entries
    + stability: the similarity of data values between consecutive versions of datasets
    + dependencies: 3rd-party modules that Python scripts import and depend on.
    + pip: the Python package installer. You can use this tool from the workspace to install modules and check information about installed modules.
    + data imputation: replacing missing entries with educated guesses about true values
    + mean imputation: using column means to replace missing data entries