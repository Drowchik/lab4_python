import pandas as pd


if __name__ == '__main__':
    path = r"C:\Users\natal\lab_2_python\annotation1.csv"
    df_csv = pd.read_csv(path)

    texts = []
    for absolute_path, rating in zip(df_csv['absolute_path'], df_csv['rating']):
        with open(absolute_path, 'r', encoding='utf-8') as file:
            text = file.read()
            texts.append((text, rating))

    df = pd.DataFrame(texts, columns=['Рецензия', 'Оценка'])

    cas = df.isnull().sum()
    print(cas)
    df.dropna()
    print('------')
    df['CountWord'] = df['Рецензия'].apply(lambda word: len(word.split()))
    print(df.head())
