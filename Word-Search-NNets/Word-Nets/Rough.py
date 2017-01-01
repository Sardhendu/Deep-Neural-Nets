import numpy as np
import matplotlib.pyplot as plt
import time
import os
import urllib.request
from six.moves import cPickle as pickle
import tensorflow as tf
from tensorflow.models.rnn.ptb import reader

from model import dynamic_RNN_model


train_batch_dir = '/Users/sam/All-Program/App-DataSet/Deep-Neural-Nets/Word-Search-NNets/Word-Nets/training_batch/'

def accuracy(predictions, labels, labels_one_hot = None):
    # The input labels are a One-Hot Vector
    if labels_one_hot:
        return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1))
              / predictions.shape[0])
    else:
        return (100.0 * np.sum(np.argmax(predictions, 1) == np.reshape(labels, [-1]))
              / predictions.shape[0])
    

def train_network(graph_dict):
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        
#         x_new = np.array([[1,4,2,2],[1,4,3,0]])
#         y_new = np.array([[4,2,2,5],[4,3,0,5]])
        
        training_data = np.array([[1,2,3,4], [1,3,4,0], [1,4,2,2], [1,4,3,0]])
        training_labels = np.array([[2,3,4,5], [3,4,0,5], [4,2,2,5], [4,3,0,5]])
        epochs = 1
        for epoch in np.arange(epochs):
            new_hid_layer_state = None
            print (graph_dict)
            for i in [2,4]:#np.arange(2):
                # with open(train_batch_dir+'batch'+str(i)+'.pickle', 'rb') as f:
                #     batch_dataset = pickle.load(f)

                #     batch_train_dataset = (batch_dataset['batch_train_dataset'])
                #     batch_train_labels = (batch_dataset['batch_train_labels'])
                #     batch_train_lenarr = (batch_dataset['batch_train_lenarr'])

                # print (batch_train_dataset[43])
                # print (batch_train_labels)
                # print (np.where(batch_train_lenarr == np.max(batch_train_lenarr)))

                
                print (training_data[i-2:i,:])
                batch_train_dataset = training_data[i-2:i,:]
                batch_train_labels = training_labels[i-2:i,:]

                batch_size=len(batch_train_dataset)
                num_hidden_layer = 3
                num_classes = 6, 
                num_sequences = 4

    #             print (batch_data)
    #             print (batch_labels)

    #             print (batch_size)
                if not new_hid_layer_state: 
                    feed_dict= {graph_dict['x']: batch_train_dataset, 
                                graph_dict['y']: batch_train_labels}
                else:
                    print ('Using the new RNN State')
                    feed_dict= {graph_dict['x']: batch_train_dataset, 
                                graph_dict['y']: batch_train_labels, 
                                graph_dict['init_state'] : new_hid_layer_state}

                a, b, c, e, j, k, prediction= sess.run([graph_dict['embed_to_hid_wghts'],
                                        graph_dict['hid_to_output_wght'],
                                        graph_dict['init_state'],
                                        graph_dict['new_state'],
                                        graph_dict['loss_CE'],
                                        graph_dict['optimizer'],
                                        graph_dict['training_prediction']], feed_dict=feed_dict)
                new_hid_layer_state = e

                acc = accuracy(prediction, batch_train_labels)

               
                # print ('batched_x \n', p)
                # print ('')
                # print ('loss_CE \n', j)
                # print ('')
                # print ('optimizer \n', k)
                # print ('')
                # print ('training_prediction \n', prediction)
                # print ('')
                print ('accuracy \n', acc)
                print ('')
                print ('')
                print ('popopopopopopopoop')
                print ('')
                print ('')




        
graph_dict = dynamic_RNN_model()
train_network(graph_dict)
