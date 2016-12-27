import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data  
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

def Weights_Variable(shape):
	initial = tf.truncated_normal(shape,stddev=0.1)
	return tf.Variable(initial)
def biases_Variable(shape):
	initial = tf.constant(0.1,shape = shape)
	return tf.Variable(initial)
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')

xs = tf.placeholder(tf.float32, [None,784])
ys = tf.placeholder(tf.float32,[None,10])
x_image = tf.reshape(xs,[-1,28,28,1])

Weights_conv1 = Weights_Variable([5,5,1,32])
b_conv1 = biases_Variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image,Weights_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

Weights_conv2 = Weights_Variable([5,5,32,64])
b_conv2 = biases_Variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1,Weights_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

Weights_fc1 = Weights_Variable([7*7*64,1024])
b_fc1 = biases_Variable([1024])

h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,Weights_fc1) + b_fc1)
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

Weights_fc2 = Weights_Variable([1024,10])
b_fc2 = biases_Variable([10])
y_conv = tf.matmul(h_fc1_drop,Weights_fc2) + b_fc2

correct_prediction = tf.equal(tf.argmax(y_conv,1),tf.argmax(ys,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

saver = tf.train.Saver()
with tf.Session() as sess:
  load_path = saver.restore(sess,"tf_con/tf_con.ckpt")
  accuracyResult = list(range(20))
  for i in range(20):
    batch = mnist.test.next_batch(1000)
    accuracyResult[i] = accuracy.eval(feed_dict={xs:batch[0],ys:batch[1],keep_prob:1.0})
  print "Test accuracy:", np.mean(accuracyResult)
