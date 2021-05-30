# Instructions
In this assignment you will build the following elements :

1. A custom dataloader
1. A custom CNN
1. A custom training and evaluation function

The data can be found at the following address:
<https://drive.google.com/file/d/1c9R_WO0ttNFSYXLG7Zap0ToBASLLq6Rb/view?usp=sharing>
For the description of the data please read this manual:


you are to take the data and build a CNN and train it to classify the input records according to the 'scene' (located at index 1 of each sample). Index starts at 0.

 The biggest difficulty that you are to overcome is the following. The dataset is cotained in one file.  In the __init__ function of your dataset class, you should break the file into individual records and save each of the record in an individual file. Then during the __getitem__ function you should read the proper file and return the features and the label as shown in the class. 
