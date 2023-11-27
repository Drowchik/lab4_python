import pandas as pd


def read_csv_in_data_frame(path: str) -> pd.core.frame.DataFrame:
    df_csv = pd.read_csv(path)
    texts = []
    for absolute_path, rating in zip(df_csv['absolute_path'], df_csv['rating']):
        with open(absolute_path, 'r', encoding='utf-8') as file:
            text = file.read()
            texts.append((text, rating))

    df = pd.DataFrame(texts, columns=['review', 'rating'])
    return df


def delete_none(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    print(df.isnull().sum())
    df.dropna()
    return df


def count_word(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df['count_word'] = df['review'].apply(lambda word: len(word.split()))
    return df


def filter_by_words(df: pd.core.frame.DataFrame, count_words: int) -> pd.core.frame.DataFrame:
    return df[df.count_word >= count_words]


def filter_by_rating(df: pd.core.frame.DataFrame, count_rating: int) -> pd.core.frame.DataFrame:
    return df[df.rating == count_rating]


if __name__ == '__main__':
    path = r"C:\Users\natal\lab_2_python\annotation1.csv"
    df = read_csv_in_data_frame(path)
    df = delete_none(df)
    df = count_word(df)
    print(df.head())
    print('----')
    print(df.describe())
    ab = filter_by_words(df, 1600)
    print(ab)
    cd = filter_by_rating(df, 3)
    print(cd)
    # stats_rating = df['rating'].describe()
    # str = df.loc[df['count_word'] == 8]
