# Dependency Parsing as Sequence Labeling with Multi-Task Learning (MTL)

This code runs on:

* ```Python 3.6```
* ```PyTorch 1.2.0```

This  repository  is  a  clone of the repository by Strzyz et al. (Original repository is available [here](https://github.com/mstrise/dep2label-up)) with a few slight modifications to suit our needs. In the neural model while concatenating the word, character and POS tag embeddings for the word representation, we also concatenate the gaze features at this step. Depending on the parser setup, sometimes we exclude the POS tag embeddings or the word and character embeddings.  We also add the gaze features while encoding the dependency tree to sequence labels and added a proper decode mode to the parser when it loads an already trained model to parse new sentences. In addition to these changes, there are also some simple data-processing scripts for normalizing and averaging the data.

 Dependency trees can be encoded into labels by:
 
 ```bash
python encode_dep2labels.py --file_to_encode x --output x --task x --enc x
```
 where:
 
```Python
file_to_encode=...  # file with dependencies in the CONLL format
output=...    # output with encoded trees as labels
task=... # single or multitask learning of labels [single, combined, multi] *combined only applicable for encoding 3
enc=...   # type of encoding [2,3,4]
```

#### Training a model and parsing with a pre-trained model

 ```bash
python main.py --config x 
```

* ```--train-config``` an example of a [config file for training](https://github.com/balthamel/dep2label-up/blob/master/config/train.config)
* For training, make sure to set status=train in the config file.
* For parsing with a pre-trained model, set status=decode and make sure you set the dset_dir, load_model_dir, decode_dir and result_dir variables with the correct data, saved model, decode and final result directories respectively in the config file.


