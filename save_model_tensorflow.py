#creating the model
import tensorflow as tf
#x and y are to be feeded with the help of dictionary and hence are chosen as the placeholders
x = tf.placeholder(dtype=float,shape=(3,),name="x1")
y = tf.placeholder(dtype=float,shape=(3,),name="x2")
#z is the varaible whose value will change and hence is declared as variable
z = tf.Variable(2.0,dtype=float,name='variable')
# multiplication along the dimension
dot = tf.tensordot(x, y,1,name="operation_multiplication")
#updating the value of variable
z1 = tf.assign(z, z+1)
#adding the sum achieved above
addition=tf.add(dot,z1,name="addtion")
#Create a Saver with tf.train.Saver() to manage all variables in the model
saver = tf.train.Saver()
#Model is saved inside the session
#session is created as result in the tensorflow is viewed inside the session
with tf.Session() as sess:
#loop for single iteration is run
     for _ in range(1):
         #this is used as we have used the variable
         #Returns an Op that initializes global variables.
         sess.run(tf.global_variables_initializer())
         writer = tf.summary.FileWriter('session_tensorflow', sess.graph)
         output= sess.run([addition],feed_dict={x:[1,2,4],y:[4,5,7]})
         save_path = saver.save(sess, 'dir/my_model')
         print("dd",sess.run(z1))
         print("Model saved in path: %s" % save_path)
         print(output)
