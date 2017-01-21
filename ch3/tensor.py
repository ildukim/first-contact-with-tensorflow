import tensorflow as tf

vectors = tf.constant([[1,2,3,1,2,3],[4,5,6,4,5,6]])
expanded_vectors = tf.expand_dims(vectors, 1)

print expanded_vectors.get_shape()
