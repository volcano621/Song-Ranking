import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import pandas as pd
import csv

ASSETS_PATH = '../client/src/assets'


def data_keyword(data: pd.DataFrame, region: str):
    # 读取Track Name列名
    key = data[data['Region'] == region]
    key = key['Track Name']

    # 创建txt，删除索引和列名
    key.to_csv(ASSETS_PATH+'/keyword.txt', index=False, header=False)

    # 读取刚刚保存的txt
    with open(ASSETS_PATH+'/keyword.txt', "r", encoding='gbk', errors='ignore') as f:
        text = f.read()
    f.close()
    # 这些可有可无，主要是分割
    cut = jieba.cut(text)
    text = ' '.join(cut)

    # 创建词云图，很简单
    wc = WordCloud(
        background_color="white",
        repeat=True,
        font_path='msyh.ttc',
    )
    wc.generate(text)
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    wc.to_file(ASSETS_PATH+'/keyword_'+region+'.png')

