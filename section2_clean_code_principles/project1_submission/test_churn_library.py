"""
Testing module that will check the churn_library.py procedure.
Artifact produced will be in logs folders.

Author: HuyenVTK1
Date: April 30, 2022
"""

import os
import logging
import sys
import glob

import pytest
import joblib

from churn_library import import_data, perform_eda, encoder_helper, \
    perform_feature_engineering, train_models

os.environ["QT_QPA_PLATFORM"] = "offscreen"

logging.basicConfig(
    filename="logs/churn_library.log",
    level=logging.INFO,
    filemode='w',
    format="%(asctime)s: %(name)s - %(levelname)s - %(message)s",
    force=True)


@pytest.fixture(scope="module")
def df_raw():
    """
    raw dataframe fixture - returns the raw dataframe from initial dataset file
    """
    try:
        df_raw = import_data("data/bank_data.csv")
        logging.info("Raw dataframe fixture creation: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Raw dataframe fixture creation: The file wasn't found")
        raise err

    return df_raw


@pytest.fixture(scope="module")
def df_encoded(df_raw):
    """
    encoded dataframe fixture - returns the encoded dataframe on some specific column
    """
    try:
        df_encoded = encoder_helper(df_raw,
                                    category_lst=["Gender",
                                                  "Education_Level",
                                                  "Marital_Status",
                                                  "Income_Category",
                                                  "Card_Category"],
                                    response="Churn")
        logging.info("Encoded dataframe fixture creation: SUCCESS")
    except KeyError as err:
        logging.error(
            "Encoded dataframe fixture creation: Not existent column to encode")
        raise err

    return df_encoded


@pytest.fixture(scope="module")
def df_fe(df_encoded):
    """
    dataframe feature engineering fixtures - returns X_train, X_test, y_train, y_test
    """
    try:
        x_train, x_test, y_train, y_test = perform_feature_engineering(
            df_encoded, response="Churn")
        logging.info("Dataframe feature engineering fixture creation: SUCCESS")
    except BaseException:
        logging.error(
            "Dataframe feature engineering fixture creation: Sequences length mismatch")
        raise

    return x_train, x_test, y_train, y_test


def test_import(df_raw):
    """
    test import function - test initial dataset import for raw data
    """
    try:
        assert df_raw.shape[0] > 0
        assert df_raw.shape[1] > 0
        logging.info("Testing import_data: SUCCESS")
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err


def test_eda(df_raw):
    """
    test perform eda function - test creation of images related eda
    """
    perform_eda(df_raw)

    for image_name in ["Churn",
                       "Customer_Age",
                       "Marital_Status",
                       "Total_Trans_Ct",
                       "Heatmap"]:
        try:
            with open("images/eda/%s.jpg" % image_name, "r"):
                logging.info("Testing perform_eda: SUCCESS")
        except FileNotFoundError as err:
            logging.error("Testing perform_eda: generated images missing")
            raise err


def test_encoder_helper(df_encoded):
    """
    test encoder helper function - test dataset encoding
    """
    try:
        assert df_encoded.shape[0] > 0
        assert df_encoded.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing encoder_helper: The df doesn't appear to have rows and columns")
        raise err

    try:
        for column in ["Gender_Churn",
                       "Education_Level_Churn",
                       "Marital_Status_Churn",
                       "Income_Category_Churn",
                       "Card_Category_Churn"]:
            assert column in df_encoded
    except AssertionError as err:
        logging.error(
            "Testing encoder_helper: The df doesn't have the right encoded columns")
        raise err
    logging.info("Testing encoder_helper: SUCCESS")

    return df_encoded


def test_perform_feature_engineering(df_fe):
    """
    test feature engineering - test feature engineering of the df
    """
    try:
        x_train = df_fe[0]
        x_test = df_fe[1]
        y_train = df_fe[2]
        y_test = df_fe[3]
        assert len(x_train) == len(y_train)
        assert len(x_test) == len(y_test)
        logging.info("Testing feature_engineering: SUCCESS")
    except AssertionError as err:
        logging.error("Testing feature_engineering: Sequences length mismatch")
        raise err

    return df_fe


def test_train_models(df_fe):
    """
    test train_models - check result of training process
    """
    train_models(df_fe[0], df_fe[1], df_fe[2], df_fe[3])

    try:
        joblib.load("models/rfc_model.pkl")
        joblib.load("models/logistic_model.pkl")
        logging.info("Testing testing_models: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing train_models: The files waeren't found")
        raise err

    for image_name in ["Logistic_Regression",
                       "Random_Forest",
                       "Feature_Importance",
                       "Roc_Curves"]:
        try:
            with open("images/results/%s.jpg" % image_name, 'r'):
                logging.info(
                    "Testing testing_models (report generation): SUCCESS")
        except FileNotFoundError as err:
            logging.error(
                "Testing testing_models (report generation): generated images missing")
            raise err


if __name__ == "__main__":
    for directory in ["logs", "images/eda", "images/results", "models"]:
        files = glob.glob("%s/*" % directory)
        for file in files:
            os.remove(file)
    sys.exit(pytest.main(["-s"]))
