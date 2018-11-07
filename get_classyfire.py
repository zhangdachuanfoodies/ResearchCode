# author: zdc time: 2018/4/8
# -*- coding:utf-8 -*-
import json

with open(r'C:\Users\zdc00\PycharmProjects\python_test_2\FRCD\data\new_data\4_8301_combine_classyfire.json', 'r')as f:
    contents = json.load(f)

# 不要Alternative Parents 和 External Descriptors 了
def clean_data():
    lst = list()
    lst2 = list()

    for key, value in contents.items():
        print key

        index = ['id', 'Kingdom', 'Superclass', 'Class', 'Subclass', 'Intermediate_Tree_Nodes', 'Direct_Parent',
                 'Kingdom_url',
                 'Molecular_Framework', 'Substituents', 'Description', 'Class_url', 'Subclass_url', 'Superclass_url']
        zd = dict().fromkeys(index)

        content_lst = value
        if content_lst[0].get("Class"):
            zd['id'] = key
            zd['Class'] = content_lst[0].get("Class")
            zd['Description'] = content_lst[0].get("Description")
            zd['Direct_Parent'] = content_lst[0].get("Direct Parent")
            zd['Intermediate_Tree_Nodes'] = content_lst[0].get("Intermediate Tree Nodes")
            zd['Kingdom'] = content_lst[0].get("Kingdom")
            zd['Molecular_Framework'] = content_lst[0].get("Molecular Framework")
            zd['Subclass'] = content_lst[0].get("Subclass")
            zd['Substituents'] = content_lst[0].get("Substituents")
            zd['Superclass'] = content_lst[0].get("Superclass")
            zd['Class_url'] = content_lst[1].get("Class")
            zd['Kingdom_url'] = content_lst[1].get("Kingdom")
            zd['Subclass_url'] = content_lst[1].get("Subclass")
            zd['Superclass_url'] = content_lst[1].get("Superclass")
            lst.append(zd)

            AP = content_lst[1]
            for key1, value1 in AP.get('Alternative Parents').items():
                zd2 = {'id': '', 'name': '', 'url': ''}
                '''可选择的父类，多爬取了几项class4 class5 class6...'''
                if key1 in content_lst[0].get('Alternative Parents'):
                    zd2['id'] = key
                    zd2['name'] = key1
                    zd2['url'] = value1
                    lst2.append(zd2)

    print len(lst)
    print len(lst2)

    # with open('./data/classfiredata1.json', 'w') as f1:
    #     json.dump(lst, f1, indent=2, sort_keys=True)
    with open(r'C:\Users\zdc00\PycharmProjects\python_test_2\FRCD\data\new_data\4_8301_combine_classyfire_1.json', 'w') as f2:
        json.dump(lst, f2, indent=2, sort_keys=True)

