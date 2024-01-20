import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from wordcloud import WordCloud
import jieba
filepath = 'data0.csv'
df = pd.read_csv(filepath)
text_list = df['内容'].values.tolist()
text_str = ' '.join(text_list)
jieba_text = " ".join(jieba.lcut(text_str))
wc = WordCloud(
    scale=5,  # 清晰度
    margin=0,  # 边距
    background_color="white",  # 背景颜色
    max_words=1200,  # 最大字符数
    width=800,  # 图宽
    height=450,  # 图高
    font_path="C:\Windows\Fonts\simhei.ttf",  # WIndows字体文件路径
    stopwords = [k.strip() for k in open('stopwords.txt', encoding='utf8').readlines() if k.strip() != ''],  # 停用词
    random_state=800  # 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(jieba_text)  # 生成词云图
wc.to_file('文本内容关键字词云图.png')  # 保存图片
wc.to_image()  # 显示图片
