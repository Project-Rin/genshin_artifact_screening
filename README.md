基于<https://github.com/wormtql/genshin_artifact>的圣遗物狗粮筛选
从<https://www.mona-uranai.com/> 导出 artifacts_mona.json 文件(可能需要通过字典翻译成中文俗称)

在needs.json文件里面输入想要保存的

    1."setName":需要筛选的套装
    2."mainTag":主词条(可选多个)
    3."normalTags":副词条(可选多个)
    4.“num”：命中副词条数小于指定数值就纳入狗粮
    
然后运行artifacts_mona.py文件
