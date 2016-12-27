import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data  
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

xs = tf.placeholder(tf.float32, [None,784])
ys = tf.placeholder(tf.float32,[None,10])
Weights = tf.Variable(tf.zeros([784,10]))
biases = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(xs,Weights) + biases)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(tf.mul(ys,tf.log(y)),reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(ys,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(3000):
	x,y = mnist.train.next_batch(300)
	sess.run(train_step,feed_dict={xs:x,ys:y})

print sess.run(accuracy,feed_dict = {xs:mnist.test.images,ys:mnist.test.labels})
