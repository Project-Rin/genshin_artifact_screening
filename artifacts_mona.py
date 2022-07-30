import json

artifacts_mona = json.load(open("artifacts_mona.json", "r", encoding='utf-8'))
needs = json.load(open("needs.json", "r", encoding='utf-8'))
output = []

# flower
flower = []
for i in artifacts_mona["flower"]:
    flower.append(i)

flower_append = []
flower_level = needs["flower"]["level"]
flower_setName = needs["flower"]["setName"]
flower_mainTag = needs["flower"]["mainTag"]
flower_normalTags = needs["flower"]["normalTags"]
flower_num = needs["flower"]["num"]
for i in flower:
    if i["level"] < flower_level:
        if i["setName"] == flower_setName:
            if i["mainTag"]["name"] not in flower_mainTag:
                flower_append.append(i)
            n = 0
            if len(i["normalTags"]) == 3:
                for a in i["normalTags"]:
                    if a["name"] in flower_normalTags:
                        n += 1
                if n < flower_num-1:
                    flower_append.append(i)
            elif len(i["normalTags"]) == 4:
                for a in i["normalTags"]:
                    if a["name"] in flower_normalTags:
                        n += 1
                if n < flower_num:
                    flower_append.append(i)
output.append(flower_append)

# sand
sand = []
for i in artifacts_mona["sand"]:
    sand.append(i)

sand_append = []
sand_level = needs["sand"]["level"]
sand_setName = needs["sand"]["setName"]
sand_mainTag = needs["sand"]["mainTag"]
sand_normalTags = needs["sand"]["normalTags"]
sand_num = needs["sand"]["num"]
for i in sand:
    if i["level"] < sand_level:
        if i["setName"] == sand_setName:
            if i["mainTag"]["name"] not in sand_mainTag:
                sand_append.append(i)
            n = 0
            if len(i["normalTags"]) == 3:
                for a in i["normalTags"]:
                    if a["name"] in sand_normalTags:
                        n += 1
                if n < sand_num-1:
                    sand_append.append(i)
            elif len(i["normalTags"]) == 4:
                for a in i["normalTags"]:
                    if a["name"] in sand_normalTags:
                        n += 1
                if n < sand_num:
                    sand_append.append(i)
output.append(sand_append)

# feather
feather = []
for i in artifacts_mona["feather"]:
    feather.append(i)

feather_append = []
feather_level = needs["feather"]["level"]
feather_setName = needs["feather"]["setName"]
feather_mainTag = needs["feather"]["mainTag"]
feather_normalTags = needs["feather"]["normalTags"]
feather_num = needs["feather"]["num"]
for i in feather:
    if i["level"] < feather_level:
        if i["setName"] == feather_setName:
            if i["mainTag"]["name"] not in feather_mainTag:
                feather_append.append(i)
            n = 0
            if len(i["normalTags"]) == 3:
                for a in i["normalTags"]:
                    if a["name"] in feather_normalTags:
                        n += 1
                if n < feather_num-1:
                    feather_append.append(i)
            elif len(i["normalTags"]) == 4:
                for a in i["normalTags"]:
                    if a["name"] in feather_normalTags:
                        n += 1
                if n < feather_num:
                    feather_append.append(i)
output.append(feather_append)

# cup
cup = []
for i in artifacts_mona["cup"]:
    cup.append(i)

cup_append = []
cup_level = needs["cup"]["level"]
cup_setName = needs["cup"]["setName"]
cup_mainTag = needs["cup"]["mainTag"]
cup_normalTags = needs["cup"]["normalTags"]
cup_num = needs["cup"]["num"]
for i in cup:
    if i["level"] < cup_level:
        if i["setName"] == cup_setName:
            if i["mainTag"]["name"] not in cup_mainTag:
                cup_append.append(i)
            n = 0
            if len(i["normalTags"]) == 3:
                for a in i["normalTags"]:
                    if a["name"] in cup_normalTags:
                        n += 1
                if n < cup_num-1:
                    cup_append.append(i)
            elif len(i["normalTags"]) == 4:
                for a in i["normalTags"]:
                    if a["name"] in cup_normalTags:
                        n += 1
                if n < cup_num:
                    cup_append.append(i)
output.append(cup_append)

# head
head = []
for i in artifacts_mona["head"]:
    head.append(i)

head_append = []
head_level = needs["head"]["level"]
head_setName = needs["head"]["setName"]
head_mainTag = needs["head"]["mainTag"]
head_normalTags = needs["head"]["normalTags"]
head_num = needs["head"]["num"]
for i in head:
    if i["level"] < head_level:
        if i["setName"] == head_setName:
            if i["mainTag"]["name"] not in head_mainTag:
                head_append.append(i)
            n = 0
            if len(i["normalTags"]) == 3:
                for a in i["normalTags"]:
                    if a["name"] in head_normalTags:
                        n += 1
                if n < head_num-1:
                    head_append.append(i)
            elif len(i["normalTags"]) == 4:
                for a in i["normalTags"]:
                    if a["name"] in head_normalTags:
                        n += 1
                if n < head_num:
                    head_append.append(i)
output.append(head_append)


with open("output.json", "w", encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
    f.close()
print(u'圣遗物筛选完毕...')
