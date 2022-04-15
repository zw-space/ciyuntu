with open('qh.txt', 'r', encoding='utf-8') as f:
    d = f.readlines()
with open('qh1.txt', 'w', encoding='utf-8') as f:
    for i in d:
        if i in ['\n']:
            continue
        i = i.split('、')[1].replace('。', '').replace('”', '').strip()
        f.write(i+'\n')
