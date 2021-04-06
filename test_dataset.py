# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:35:31 2021

@author: clark

"""
import tensorflow as tf
def getThreshold1(x):
    x = x / 255
    if x > 0.6:
        return 1
    else:
        return 0
# def getThreshold2(x):
#     for item in x:
#         item = item / 255
#         if item > 0.6:
#            item = 1
#         else:
#            item = 0
x = tf.constant([100, 200, 150, 250, 255])

#print('type(z)=',type(z), 'shape()=', z.shape)
y = x
for idx, item in enumerate(x,0):
    print(type(item))
    #y[idx] = tf.data.Dataset.from_generator(getThreshold1, args=item, output_types=tf.int32, output_shapes = ()) 

#z = tf.data.Dataset.from_generator(getThreshold2, args=x, output_types=tf.float32, output_shapes = (5,))
print('y:', y) 
for item in y:
    print('item:{0}'.format(item))
#print('z:{0}'.format(z)) 
ds = tf.range(5)
print('1. type:', type(ds))
print('2.',ds)  #display dataset information
print('3. dataset:{0}'.format(ds))   #display value of dataset
for idx, item in enumerate(ds,0):   #display each item in dataset
    print('4. idx:{0}, content:{1}'.format(idx, item))
print('- - - - - - - - - ')
for idx, item in enumerate(ds,0):   #display each item in dataset
    print('5. item information:',idx ,  item)
    
print('-----------------')

dset1 = tf.data.Dataset.from_tensors(ds)
dset2 =  tf.data.Dataset.from_tensor_slices(ds)
print('6. data set1:', dset1)
print('7. data set2:', dset2)
print('==================')

a = tf.constant([1,2,3])
b = tf.constant([4,5,6])
# 1. build by  from_tensors
dataset1 = tf.data.Dataset.from_tensors(a)
print('dataset1:', dataset1)           #顯示dataset1的資訊
dataset2 = tf.data.Dataset.from_tensors(a+b)
print('dataset2:', dataset2)
# 2. build by zip :將反覆運算的tensor為參數, 將對應的元素打包成一個位元組, 傳回這些位元組組成的List
z = zip(a, b)
for item1, item2 in zip(a,b):
    print('item1:{0}, item2:{1}'.format(item1, item2))
print('-----')
for item1, item2 in z:                 #讀取資料'
    print(item1, item2)
print('----take:----')
# 3. take 指定讀取資料的數量; used for limiting number of items in dataset. 
data1 = tf.constant([100,200,3,4,5,6,7])
data2 = tf.constant(['albert','bill','clark','danel','eva','frank','gik'])
dataset1 = tf.data.Dataset.from_tensor_slices(data1)
dataset2 = tf.data.Dataset.from_tensor_slices(data2)
#print(dataset3.take(1))
for item in dataset1.take(2):
    print('-->',item)
for item1, item2 in zip(dataset1.take(3), dataset2.take(3)):
    print('==>',item1, item2)
for item1, item2 in zip(dataset1.take(3), dataset2.take(3)):
    print('raw data:{0}:{1}'.format(item1, item2))
