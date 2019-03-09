#deep learning library is imported
import tensorflow as tf
sess=tf.Session()
#First let's load meta graph and restore weights
saver = tf.train.import_meta_graph('dir/my_model.meta')
saver.restore(sess,tf.train.latest_checkpoint('dir/'))
print(sess.run('variable:0'))
graph = tf.get_default_graph()
x = graph.get_tensor_by_name("x1:0")
y = graph.get_tensor_by_name("x2:0")
feed_dict ={x:[1,2,3],y:[6,7,8]}
op_to_restore = graph.get_tensor_by_name("addtion:0")
print(sess.run(op_to_restore,feed_dict))
