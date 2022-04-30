"""
This is the churn_library.py procedure.
Artifact produced will be in images and models folders.

Author: HuyenVTK1
Date: April 30, 2022
"""

import os
import logging
from sklearn.metrics import plot_roc_curve, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

os.environ["QT_QPA_PLATFORM"] = "offscreen"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def import_data(pth):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''
    df = pd.read_csv(pth)

    return df


def perform_eda(df):
    '''
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    '''
    df["Churn"] = df["Attrition_Flag"].apply(
        lambda val: 0 if val == "Existing Customer" else 1)

    column_name_lst = ["Churn", "Customer_Age",
                       "Marital_Status", "Total_Trans_Ct", "Heatmap"]
    for column_name in column_name_lst:
        plt.figure(figsize=(20, 10))
        if column_name in ("Churn", "Customer_Age"):
            df[column_name].hist()
        elif column_name == "Marital_Status":
            df[column_name].value_counts('normalize').plot(kind='bar')
        elif column_name == "Total_Trans_Ct":
            sns.histplot(df[column_name], stat='density', kde=True)
        elif column_name == "Heatmap":
            sns.heatmap(df.corr(), annot=False, cmap='Dark2_r', linewidths=2)
        plt.savefig("images/eda/%s.jpg" % column_name)
        plt.close()


def encoder_helper(df, category_lst, response):
    '''
    helper function to turn each categorical column into a new column with
    propotion of churn for each category - associated with cell 15 from the notebook

    input:
            df: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name [optional argument that \
                could be used for naming variables or index y column]

    output:
            df: pandas dataframe with new columns for
    '''
    for category_column_name in category_lst:
        category_column_lst = []
        category_column_groups = df.groupby(
            category_column_name).mean()[response]

        for val in df[category_column_name]:
            category_column_lst.append(category_column_groups.loc[val])

        df[category_column_name + "_" + response] = category_column_lst

    return df


def perform_feature_engineering(df, response):
    '''
    input:
              df: pandas dataframe
              response: string of response name [optional argument that \
                  could be used for naming variables or index y column]

    output:
              x_train: x training data
              x_test: x testing data
              y_train: y training data
              y_test: y testing data
    '''
    x = pd.DataFrame()
    y = df[response]

    keep_cols = [
        "Customer_Age",
        "Dependent_count",
        "Months_on_book",
        "Total_Relationship_Count",
        "Months_Inactive_12_mon",
        "Contacts_Count_12_mon",
        "Credit_Limit",
        "Total_Revolving_Bal",
        "Avg_Open_To_Buy",
        "Total_Amt_Chng_Q4_Q1",
        "Total_Trans_Amt",
        "Total_Trans_Ct",
        "Total_Ct_Chng_Q4_Q1",
        "Avg_Utilization_Ratio",
        "Gender_Churn",
        "Education_Level_Churn",
        "Marital_Status_Churn",
        "Income_Category_Churn",
        "Card_Category_Churn"]

    x[keep_cols] = df[keep_cols]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42)

    return x_train, x_test, y_train, y_test


def classification_report_image(y_train, y_test, y_train_preds_lr, \
                                y_train_preds_rf, y_test_preds_lr, y_test_preds_rf):
    '''
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds_lr: training predictions from logistic regression
            y_train_preds_rf: training predictions from random forest
            y_test_preds_lr: test predictions from logistic regression
            y_test_preds_rf: test predictions from random forest

    output:
             None
    '''
    classification_reports_data = {
        "Random_Forest": (
            "Random Forest Train",
            y_test,
            y_test_preds_rf,
            "Random Forest Test",
            y_train,
            y_train_preds_rf),
        "Logistic_Regression": (
            "Logistic Regression Train",
            y_train,
            y_train_preds_lr,
            "Logistic Regression Test",
            y_test,
            y_test_preds_lr)}

    for title, classification_data in classification_reports_data.items():
        plt.rc("figure", figsize=(5, 5))

        plt.text(0.01, 1.25, str(classification_data[0]), {
                 "fontsize": 10}, fontproperties="monospace")
        plt.text(
            0.01, 0.05, str(
                classification_report(
                    classification_data[1], classification_data[2])), {
                "fontsize": 10}, fontproperties="monospace")
        plt.text(0.01, 0.6, str(classification_data[3]), {
                 "fontsize": 10}, fontproperties="monospace")
        plt.text(
            0.01, 0.7, str(
                classification_report(
                    classification_data[4], classification_data[5])), {
                "fontsize": 10}, fontproperties="monospace")
        plt.axis("off")
        plt.savefig("images/results/%s.jpg" % title)
        plt.close()


def feature_importance_plot(model, x_data, output_pth):
    '''
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            x_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    '''
    importances = model.best_estimator_.feature_importances_
    indices = np.argsort(importances)[::-1]
    names = [x_data.columns[i] for i in indices]

    plt.figure(figsize=(20, 5))
    plt.title("Feature Importance")
    plt.ylabel('Importance')
    plt.bar(range(x_data.shape[1]), importances[indices])
    plt.xticks(range(x_data.shape[1]), names, rotation=90)
    plt.savefig("images/%s/Feature_Importance.jpg" % output_pth)
    plt.close()


def train_models(x_train, x_test, y_train, y_test):
    '''
    train, store model results: images + scores, and store models
    input:
              x_train: x training data
              x_test: x testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    '''
    rfc = RandomForestClassifier(random_state=42)
    lrc = LogisticRegression(solver='lbfgs', max_iter=3000)

    param_grid = {
        'n_estimators': [200, 500],
        'max_features': ['auto', 'sqrt'],
        'max_depth': [4, 5, 100],
        'criterion': ['gini', 'entropy']
    }

    cv_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
    cv_rfc.fit(x_train, y_train)

    lrc.fit(x_train, y_train)

    y_train_preds_rf = cv_rfc.best_estimator_.predict(x_train)
    y_test_preds_rf = cv_rfc.best_estimator_.predict(x_test)

    y_train_preds_lr = lrc.predict(x_train)
    y_test_preds_lr = lrc.predict(x_test)

    # store ROC curves plot
    lrc_plot = plot_roc_curve(lrc, x_test, y_test)
    plt.figure(figsize=(15, 8))
    axis = plt.gca()
    _ = plot_roc_curve(cv_rfc.best_estimator_,
                       x_test, y_test, ax=axis, alpha=0.8)
    lrc_plot.plot(ax=axis, alpha=0.8)
    plt.savefig("images/results/Roc_Curves.jpg")
    plt.close()

    # store classification report image
    classification_report_image(y_train,
                                y_test,
                                y_train_preds_lr,
                                y_train_preds_rf,
                                y_test_preds_lr,
                                y_test_preds_rf)

    # store feature importance plot
    feature_importance_plot(cv_rfc, x_test, "results")

    # store models
    joblib.dump(cv_rfc.best_estimator_, "models/rfc_model.pkl")
    joblib.dump(lrc, "models/logistic_model.pkl")


if __name__ == "__main__":
    logger.info("Import data")
    DF_RAW = import_data("data/bank_data.csv")

    logger.info("Perform EDA")
    perform_eda(DF_RAW)

    logger.info("Encode categorical columns")
    DF_ENCODED = encoder_helper(DF_RAW,
                                category_lst=["Gender",
                                              "Education_Level",
                                              "Marital_Status",
                                              "Income_Category",
                                              "Card_Category"],
                                response="Churn")

    logger.info("Perform Feature Engineering and Split Train & Test data")
    X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = perform_feature_engineering(
        DF_ENCODED, response="Churn")

    logger.info("Train and store model and results")
    train_models(X_TRAIN, X_TEST, Y_TRAIN, Y_TEST)
