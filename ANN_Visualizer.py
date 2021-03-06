!pip3 install keras
!pip3 install ann_visualizer
!pip install graphviz

from keras.models import Sequential  
from keras.layers import Dense  
from ann_visualizer.visualize import ann_viz  

network = Sequential()  
#Hidden Layer#1  
network.add(Dense(units=8, activation='relu',  kernel_initializer='uniform', input_dim=4))  
network.add(Dense(units=8, activation='relu',  kernel_initializer='uniform',))  
#Output Layer  
network.add(Dense(units=4, activation='sigmoid', kernel_initializer='uniform'))
ann_viz(network, view=True, title="test", filename="visualized")
