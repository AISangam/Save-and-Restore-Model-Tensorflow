# Save-and-Restore-Model-Tensorflow  
This code is to used when one want to save and restore model created using tensorflow. Question is why restoring of the model is a need.    
## Why restore is important  
Restoring model is a need when you want to optimize the code as well as use the memory efficiency. Suppose you are creating a deep neural network and you need to perform prediction part. It is not convenient to train the data every time. Other solution is to save the model and load the saved model. It will help in saving a lot of time as well as memory.   
Consider the another case when you need to run the model for <em><strong>20000 iterations</em></strong> and light goes off when you are at <em><strong>19000 iterations</em></strong>. How do you feel about it. If you know how to restore the model from the last checkpoint you can continue your training from that part. It would work charm for you. This is the reason this repository is created.    

## Different functions and modules used in this code  
<strong>tf.tensordot</strong> = This is used to add two tensor along the dimension.    
<strong>tf.assign</strong> = Assigning the value to another value.   
<strong>tf.placeholder</strong> = When you want to provide different values, this function is used.    
<strong>tf.train.Saver()</strong>= Create a Saver with tf.train.Saver() to manage all variables in the model.  
<strong>tf.global_variables_initializer()</strong>= Returns an Op that initializes global variables.    

## Code to save + restore model  
<strong>Saving model</strong>
Have a look at this code.  
```
save_path = saver.save(sess, 'dir/my_model')
```  
<strong>Restore Model</strong>
Have a look at this code.  
```
saver = tf.train.import_meta_graph('dir/my_model.meta')
saver.restore(sess,tf.train.latest_checkpoint('dir/'))
```
## Some references to study  
I also suggest readers to look at the below links to get good knowledge of tensorflow and its functions.  
https://www.aisangam.com/blog/tensorflow-tutorials-from-basic-for-beginners-part-1-ai-sangam/  
https://www.aisangam.com/blog/optimize-parameters-tensorflow-tutorial-part-2-ai-sangam/  
https://www.aisangam.com/blog/low-level-introduction-of-tensorflow-simple-way-part-3-ai-sangam/  
https://www.aisangam.com/blog/tensorflow-control-practice-live-codes-graphs-sessions-part-4-ai-sangam/  
https://www.aisangam.com/blog/create-save-load-model-with-graph-part-5-tensorflow-mnist/    

## Diagram showing the graph for this model in tensorboard   
![graph_tensorboard](https://user-images.githubusercontent.com/35392729/54069810-a1d74e80-4280-11e9-8380-07f5a1a22577.png)  

## How to run this code  
Since this is the python code and both <strong>restore_model_tensorflow.py</strong> and <strong>save_model_tensorflow.py</strong> are independent of each other. This is because model is saved in the dir directory which is retrieved in the file restore_model_tensorflow.py.  

<strong>Running python file to save the model</strong>  
```
python/python3 save_model_tensorflow.py
```
<strong>Running python file to restore model.</strong>  
```
python/python3 restore_model_tensorflow.py  
```   

## Some External Links to be used to remove the errors while creating the code.  
https://stackoverflow.com/questions/40430186/tensorflow-valueerror-cannot-feed-value-of-shape-64-64-3-for-tensor-uplace  
https://stackoverflow.com/questions/33759623/tensorflow-how-to-save-restore-a-model











