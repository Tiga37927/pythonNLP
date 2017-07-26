#!/usr/bin/env python  
# encoding: utf-8

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: nltkShell1.py 
@time: 2017/7/26 10:19
使用nltk包学习数据处理
"""
# import nltk
# download会打开一个图形界面，选择book下载学习所需要的数据
# nltk.download()
# 加载学习所需要的数据
from nltk.book import *

# 在text1中使用concordance方法搜索“monstrous”
# text1.concordance("monstrous")

# 使用similar方法查询相似的词出现的上下文
# text1.similar("monstrous")
# text2.similar("monstrous")

# common_contexts允许研究两个或两个以上的词共同的上下文
# text2.common_contexts(["monstrous", "very"])

# 自动检测出现在文本中特定的词，计算在他前面出现了多少词，用离散图表示
# text4.dispersion_plot(["citizens", "young", "freedom", "duties"])

# set()方法去重，获得词汇表
# sorted(set(text3))

# FreqDist()查找出现频率最高的词汇, hapaxes()用于查看低频词汇
# fdist1 = FreqDist(text1)
# print len(text1)
# print fdist1
# vocabulary1 = fdist1.keys()
# print vocabulary1[:50]

# 查看长度大于15的词汇
# V = set(text1)
# long_words = [w for w in V if len(w) > 15]
# print sorted(long_words)

# 找出出现过7次以上并且长度大于7的词汇
fdist5 = FreqDist(text5)
# vcab = set(text5)
# long_words = [word for word in vcab if len(word) > 7 and fdist5[word] > 7]
# print sorted(long_words)
# 绘制频率分布表
# fdist5.tabulate()
# 绘制频率分布图 cumulative=True绘制累积频率分布图
fdist5.plot(cumulative=True)

# collocations()返回基于单个词的频率的双连词
# colloctions4 = text4.collocations()
# print colloctions4

