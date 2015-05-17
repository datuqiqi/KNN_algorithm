#encoding=utf-8
#__author__ = 'kangqi'
#2015/5/11
#--------------------------
#KNN algorithm
#--------------------------

from numpy import *
import operator
#读取文本文件并转化为矩阵，特征三维，加一列标签，标签离散值取0或1
def file2matrix(filename):
    fr=open(filename)
    numlines=len(fr.readlines())
    mat=zeros((numlines,3))
    label=[]
    index=0
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip()
        arr = line.split('\t')
        mat[index,:] = arr[0:3]
        label.append(int(arr[-1]))
        index += 1
    return mat,label
def KNN_algorithm(X,mat,label,K):
    mat_size=mat.shape[0]
    dis=tile(X,(mat_size,1))-mat
    dis_1=dis**2
    dis_2=dis_1.sum(axis=1)
    sort_dis_2=dis_2.argsort()
    count={}
    for i in range(K):
        vlabel=label[sort_dis_2[i]]
        count[vlabel]=count.get(vlabel,0)+1
    sortecount = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortecount[0][0]
#--------------------------
#main调用
#--------------------------
mat,label=file2matrix('test.txt')
X=[2,3,4]
return_label=KNN_algorithm(X,mat,label,3)
print return_label



