import json
dic_raw = json.load(open("dic_raw.json", "r", encoding='utf-8'))
dic_ex = dict()
for i in dic_raw:
    dic_ex[dic_raw[i]] = i

with open("dic_ex.json", "w", encoding='utf-8') as f:
    json.dump(dic_ex, f, ensure_ascii=False, indent=4)
    f.close()
print(u'dic_ex写入完成...')
