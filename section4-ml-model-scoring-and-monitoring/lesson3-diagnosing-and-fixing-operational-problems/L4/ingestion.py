import pandas as pd

ingested=pd.read_csv('samplefile.csv')

ingested.to_csv('samplefileingested.csv')
