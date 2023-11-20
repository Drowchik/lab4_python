import pandas as pd


df = pd.read_csv(r"C:\Users\natal\lab_2_python\annotation1.csv", sep=',')

if __name__ == '__main__':
    print(df.head(9))
