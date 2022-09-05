import pandas as pd

df = pd.read_csv("iris.csv")

def slice_iris(df, feature):
    """ Function for calculating descriptive stats on slices of the Iris dataset."""
    for cls in df["class"].unique():
        df_temp = df[df["class"] == cls]
        mean = df_temp[feature].mean()
        stddev = df_temp[feature].std()
        print(f"Class: {cls}")
        print(f"{feature} mean: {mean:.4f}")
        print(f"{feature} stddev: {stddev:.4f}")
    print()

slice_iris(df, "septal_length")
slice_iris(df, "septal_width")
slice_iris(df, "petal_length")
slice_iris(df, "petal_width")