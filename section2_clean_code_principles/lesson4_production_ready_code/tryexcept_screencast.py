import pandas as pd
import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("SUCCESS: There are {} rows in your dataframe".format(df.shape))
        logging.info("SUCCESS: Your file was successfully read in.")
        return df
    except FileNotFoundError:
        logging.error("ERROR: We were not able to find that file")

    df = read_data('./data/a.csv')