from wordcloud import WordCloud
import re
import numpy as np
import matplotlib.pyplot as plt
import wordcloud

# text = ','.join(dir(re) + dir(np))
with open('qh.txt', 'r', encoding='utf-8') as f:
    text = ','.join(
        [i for i in
         [line.split('、')[1].replace('。', '').strip()
          for line in f.readlines() if not line == '\n']
         if i not in ["没有啊", '不', '为什么']] + ['我爱你'] * 100)

background_image = plt.imread('0.jpg')
a = wordcloud.WordCloud(background_color='pink',
                        # font_path='C:\\Windows\\Fonts\\SHOWG.TTF',
                        font_path='C:\\Windows\\Fonts\\simkai.ttf',
                        width=900,
                        height=900,
                        mask=background_image,
                        max_words=10000).generate(text)

a.to_file('302.jpg')
