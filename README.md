# ML Project 2

### A New 1D CNN Method to detect Sleep Apnea using a single-lead ECG signal
This project aims to find the best classification model to detect sleep apnea from ECG signal recordings of different subjects. The best results were obtained with 1D convolutional neural network.

Files Description:

1. ```1D_CNN.ipynb``` This notebook implements, trains and evaluates a 1D CNN model to detect apnea from 1 minute signal segments.
2. ```1D_CNN.ipynb``` This notebook implements, trains and evaluates a 1D CNN model with LSTM to detect apnea from 1 minute signal segments thus leveraging the time dependencies between segments.
3. ```base_model.ipynb``` In this notebook we are training and evaluating the base model of our project which is a logistic regression on two features related to heart beats, bpm (beats per minute) and sdnn (standard deviation of the NN (R-R) intervals)
3. ```base_model_test_set.csv``` Test dataset for the baseline model, it consists of labels (apnea or not) and two features(bpm and sdnn).
4. ```base_model_train_set.csv``` Train dataset for the baseline model, it consists of labels (apnea or not) and two features(bpm and sdnn).
5. ```create_dataset_base_model.ipynb``` In this notebook we create the datasets used in our base model
6. ```create_recurrence_plots.ipynb``` In this notebook we create the recurrence plot images, and mapping to labels in a csv, that are used for the google_net model
7. ```create_spectrograms.ipynb``` In this notebook we create the spectrogram images, and mapping to labels in a csv, that are used for the google_net model
8. ```rp_CNN_google_net.ipynb``` This notebook uses google-net for transfer learning to make predictions of apnea on the spectrograms images generated from 1 minute signal segments
9. ```spect_2D_CNN.ipynb``` This notebook implements, trains and evaluates a 2D CNN to detect apnea from spectrogram images generated from 1 minute signal segments
10. ```spect_CNN_google_net.ipynb``` This notebook uses google-net for transfer learning to make predictions of apnea on the recurrence plot images generated from 1 minute signal segments
11. ```utils.py``` Diverse utility functions

How to: 

Simply run the ```run.py``` in the cloned repository, making sure that the ```data``` folder sits in the folder of the ```run.py```. Make sure to add ```test.csv``` in the ```data``` folder. This will create a ```submission.csv``` in the ```data``` folder.
Note that it takes a few minutes to generate the file (2-3 minutes)
