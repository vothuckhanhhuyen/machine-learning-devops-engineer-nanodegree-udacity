## Key Points

- Automated data ingestion: how to gather, compile, aggregate, clean, and output data for use in ML projects, including how to automate all processes
    - You need to ingest data in order to perform machine learning. Data ingestion is the term for the process of finding, gathering, recording, cleaning, and providing data as input to an ML project.
        - First, you need to find data. Your data might be in several different places, in different formats, with different sizes and update frequencies.
        - Next, you need to read your data into a Python script, and aggregate all source datasets into one, combined dataset.
        - You need to do de-duplication and cleaning.
        - Finally, you need to write the dataset to a single output file or table.
    - There are some methods from the os module that can be useful as you're performing data ingestion:
        - os.getwcd() gets the current working directory, which will enable you to search for files on your workspace.
        - os.listdir() generates a list of filenames in a particular directory. This will help you know which files to read during your ingestion process.
    - A crontab file contains rows of simple commands call cron jobs. Every cron job schedules a particular job or script to run at a particular regular interval. Cron jobs can run Python scripts, or any other command that can be run from the Linux command line.
    - Cron jobs are so important because they enable automation, and they reduce the manual intervention required in ML projects

- Process record keeping: how to keep records of data ingestion and other ML project processes, and what to record
    - As you're doing data ingestion, you should make sure to document the details of your process. The following are ingestion details you'll want to keep records of:
        - The name and location of every file you read as a source.
        - The date when you performed data ingestion.
        - The datasets you worked with
        - Other details about the data, maybe including how many duplicates you dealt with, and how many formatting changes you made.
        - The name and location of the final output file you wrote.
    - timestamp: a character string recording a particular date and time
    - datetime: a module containing capabilities for recording timestamps

- Retraining and re-deployment: how to automatically retrain models and re-deploy them to production environments
    - pickle: the module used to read and write trained ML models
    - logistic regression: an ML method used for categorical (0-1) classifications
    - re-deployment: the process of overwriting a deployed ML model with a newer, improved version
    - dump(): the method in the pickle module used to save a trained ML model

- Advanced comparisons: how to make detailed comparisons between datasets, to determine observations that are shared in common or are duplicates
    - If you have two datasets, called df1 and df2, you can use this line of code to accomplish the comparison:
    ```
    df_all = df1.merge(df2.drop_duplicates(),on=['col1','col2'],how='outer', indicator=True)
    ```

    - This will merge the two datasets together, and also create a new column called _merge, which will indicate whether each row is common to both datasets, or unique to only one.

- Big data: how to work with extremely large datasets using distributed file systems and parallel processing
    - merge(): a method for combining two datasets - also including an option to record which entries are unique to particular datasets, and which are common across both
    - distributed file system: a collection of machines that allow data to be spread across multiple locations, to make work with extremely large datasets more feasible
    - client/server model: a hierarchical model allowing one machine to perform executive functions and control others, for more efficient data processing
    - MapReduce: a framework for performing operations on distributed datasets

## Key Terms
- This lesson was concerned with data ingestion and model training and deployment. In this lesson, we learned how to:
    - automatically ingest data, for use in the model, and for model training
    - keep records related to ML processes, including data ingestion
    - automate ML processes using cron jobs
    - retrain and re-deploy ML models

- These skills are important for every ML project. It's crucial to be able to ingest new data that your model needs. It's just as crucial to retrain and re-deploy your model regularly to keep it up-to-date. Being able to keep records about processes and automate them will also be important throughout the rest of the course