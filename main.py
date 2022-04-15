import matplotlib.pyplot as plt
import wordcloud

with open('qh1.txt', 'r', encoding='utf-8') as f:
    text = ','.join(f.readlines() + ['我爱你'] * 100)

background_image = plt.imread('love.jpg')
a = wordcloud.WordCloud(background_color='pink',
                        font_path='C:\\Windows\\Fonts\\simkai.ttf',
                        width=900,
                        height=900,
                        mask=background_image,
                        max_words=10000).generate(text)

a.to_file('520.jpg')
