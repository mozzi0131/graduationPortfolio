import tensorflow as tf

x = tf.Variable(tf.random_normal([784, 200], stddev=0.35))
y = tf.Variable(x.initialized_value() + 3.)

init_op = tf.global_variables_initializer()

saver = tf.train.Saver(write_version=tf.train.SaverDef.V1)

sess = tf.Session()
sess.run(init_op)
save_path = saver.save(sess, "./model/model.ckpt")
