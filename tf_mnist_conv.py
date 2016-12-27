import tensorflow as tf
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

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv,ys))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1),tf.argmax(ys,1))
accuracyResult = list(range(20))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
saver = tf.train.Saver()

sess = tf.InteractiveSession()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(20000):
  batch = mnist.train.next_batch(100)
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={xs:batch[0], ys: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={xs: batch[0], ys: batch[1], keep_prob: 0.5})
save_path = saver.save(sess,"tf_con/tf_con.ckpt")

for i in range(20):
    batch = mnist.test.next_batch(1000)
    accuracyResult[i] = accuracy.eval(feed_dict={xs:batch[0],ys:batch[1],keep_prob:1.0})
print "Test accuracy:", np.mean(accuracyResult)
