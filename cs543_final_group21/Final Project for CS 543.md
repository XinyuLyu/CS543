# Final Project for CS 543

#### By Xinyu Lyu, Tong Wu
* Environments:
  1. Python 3.6
  2. Keras 2.0.9
  3. TensorFlow 1.3.0
  4. sklearn 0.19.1
  5. numpy 1.15.3
  6. scipy 1.1.0
* Hardware:
  1. Our model was trained on a GTX 1080 GPU with 32GB RAM.
* Codes: 

  1. load_final_data_2.py: Load data for our model.

  2. train_final_5.py: Our whole model. 

  3. word2vec.py: Help to extract texture features.

  4. audio_preprocessing.py : Audio preprocessing to audio data.

  5. self_attention.py: Define self-attention layer.

  6. data_normalization.py: normalize data.

  7. build_dictionary.py: Build the dictionary for preprocessing on texture data.

* Models:

  1. final model: fusion model

  2. audio model: audio branch model
     

  3. text audio: texture model.

* data:

  1. audio: For audio data takes up 7 GB, we just put some samples in the filder.

  2. label_output_new.txt : The emotion labels for dataset.

  3. text_output_new.txt : Texture data. 

  4. glove.6B.50d: The embedding matrix for texture features. Actually, we use glove.6B.200d, but it is too large to put here.

  For the audio dataset is too large, we can't provide a demo for you to make. We have included our test results in the report with the models included in this folder. And we promise the result is real ! And if you have any questions about the project, please be free to email us.
