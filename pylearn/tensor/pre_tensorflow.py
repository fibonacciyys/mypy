# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:24:44 2018

@author: YY
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
#import subprocess

def test1():
    #创建数据
    x_data=np.random.rand(100).astype(np.float32)
    #print(x_data,len(x_data))
    y_data=x_data*0.1+0.3
    
    #搭建模型
    Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
    biases=tf.Variable(tf.zeros([1]))
    
    y=Weights*x_data+biases
    
    #计算误差
    loss=tf.reduce_mean(tf.square(y-y_data))
    a_loss=tf.reduce_mean(tf.reduce_sum(tf.square(y-y_data)))
    #误差传播
    optimizer=tf.train.GradientDescentOptimizer(0.5)
    train=optimizer.minimize(loss)
    
    #以上建立神经网络结构
    #训练
    #创建init对象
    init=tf.global_variables_initializer()
    
    #创建会话
    sess=tf.Session()
    sess.run(init)
    
    for step in range(201):
        sess.run(train)
        if step%20==0:
            print(step,sess.run(Weights),sess.run(biases),sess.run(loss),sess.run(a_loss))
            
def test2():
    matrix1=tf.constant([[3,3]])
    matrix2=tf.constant([[2],[2]])
    product=tf.matmul(matrix1,matrix2)
    #激活运算 method1
    sess=tf.Session()
    result=sess.run(product)
    print(result)
    sess.close()
    #激活运算 method2
    with tf.Session() as sess:
        result2=sess.run(product)
        print(result2)

def test3(): #计数器
    state=tf.Variable(0)
    one=tf.constant(1)
    
    new_value=tf.add(state,one)
    update=tf.assign(state,new_value)
    
    init=tf.global_variables_initializer()
    
    with tf.Session() as sess:
        sess.run(init)
        for _ in range(13):
            sess.run(update)
            print(sess.run(state))
#    sess=tf.Session()
#    sess.run(init)
#    for _ in range(13):
#        sess.run(update)
#        print(sess.run(state))
#    sess.close()
    
def test4():
    input1=tf.placeholder(tf.float32)
    input2=tf.placeholder(tf.float32)
    
    output=tf.multiply(input1,input2)
    init=tf.global_variables_initializer()
    
    with tf.Session() as sess:
        sess.run(init)
        print(sess.run(output,feed_dict={input1:[7.],input2:[8.]}))

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size])) #正态随机,in_size行,out_size列
    biases=tf.Variable(tf.zeros([1,out_size])+0.1) #biases一般不取0
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

def test5():
    x_data=np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
    noise=np.random.normal(0,0.05,x_data.shape).astype(np.float32)
#    print(x_data.shape)
    y_data=np.square(x_data)-0.5+noise
    #可视化
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x_data,y_data)
    plt.ion()#刷新lines spyder无效 cmd运行
    
    xs=tf.placeholder(tf.float32,[None,1])
    ys=tf.placeholder(tf.float32,[None,1])
    
    l1 = add_layer(xs,1,10,tf.nn.relu)
    prediction = add_layer(l1,10,1,None)
    
    init = tf.global_variables_initializer()
    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
    train=tf.train.GradientDescentOptimizer(0.1).minimize(loss)
    with tf.Session() as sess:
        sess.run(init)
        for i in range(1000):
            sess.run(train,feed_dict={xs:x_data,ys:y_data})
            if i % 50 == 0:
#                print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
                try:
                    ax.lines.remove(lines[0])
                except Exception:
                    pass
                prediction_value=sess.run(prediction,feed_dict={xs:x_data})
                lines = ax.plot(x_data,prediction_value,'r-',lw=5)
                plt.pause(0.1)
#    subprocess.call("pause",shell=True)
    plt.ioff()
    plt.show()
    
def mnist_test():
    #准备数据
    mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
    #搭建网络
    xs = tf.placeholder(tf.float32,[None,784]) #28*28图片像素
    ys = tf.placeholder(tf.float32,[None,10])
    prediction = add_layer(xs,784,10,activation_function=tf.nn.softmax)
    #loss
    cross_entry = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=1))
    init = tf.global_variables_initializer()
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entry)
    def compute_accuracy(v_xs, v_ys):
        y_pre = sess.run(prediction, feed_dict={xs: v_xs})
        correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(ys,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
        return result
    with tf.Session() as sess:
        sess.run(init)
        for i in range(1000):
            batch_xs,batch_ys = mnist.train.next_batch(100)
            sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
            if i % 50 == 0:
                print(compute_accuracy(mnist.test.images, mnist.test.labels))

        
    
if __name__=='__main__':
    mnist_test()

