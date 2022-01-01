import pandas as pd


def load_postings(data_path):
    postings_1 = pd.read_csv(data_path + '/Postings_01052019_15052019.csv', sep=';')
    postings_2 = pd.read_csv(data_path + '/Postings_16052019_31052019.csv', sep=';')
    postings = pd.concat([postings_1, postings_2])
    postings['PostingCreatedAt'] = postings.PostingCreatedAt.astype('datetime64')
    postings['ArticlePublishingDate'] = postings.ArticlePublishingDate.astype('datetime64')
    postings['UserCreatedAt'] = postings.UserCreatedAt.astype('datetime64')
    return postings