import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

sound_names = ["siren", "fire alarm", "boiling water", "dog bark"]
sound_data = np.load('sound_test.npz')
X_test= sound_data['X']
y_test = sound_data['y']

print(X_test.shape)
print(y_test.shape)

training_epochs = 5000
n_dim = 193
n_classes = 4
learning_rate = 0.001

g1 = tf.Graph()
with g1.as_default():
    X = tf.placeholder(tf.float32, [None, n_dim])
    Y = tf.placeholder(tf.float32, [None, n_classes])

    c1 = tf.layers.conv2d(tf.reshape(X, [-1, 1, n_dim, 1]), 50, (1, 5), padding='same', 
                          activation=tf.nn.sigmoid, name="c1")
    p1 = tf.layers.max_pooling2d(inputs=c1, pool_size=[1, 2], strides=2)
    c2 = tf.layers.conv2d(tf.reshape(p1, [-1, 1, 96, 50]), 100, (1, 5), padding='same', 
                          activation=tf.nn.sigmoid, name="c2")
    p2 = tf.layers.max_pooling2d(inputs=c2, pool_size=[1, 2], strides=2)

    h_p = tf.reshape(p2, [-1, 48*100])

    h_1 = tf.layers.dense(inputs=h_p, units=1000, activation=tf.nn.sigmoid,
                          kernel_initializer=tf.contrib.layers.xavier_initializer(),
                          name="fc1")

    y_hat = tf.layers.dense(inputs=h_1, units=n_classes,
                            kernel_initializer=tf.contrib.layers.xavier_initializer(), 
                            name="h4")

    correct_prediction = tf.equal(tf.argmax(y_hat,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

with tf.Session(graph=g1) as sess:
    sess.run(init)
    saver.restore(sess, './Newmodel_LSH.ckpt')
    print('Test accuracy: ',round(sess.run(accuracy, feed_dict={X: X_test, Y: y_test}) , 3))
