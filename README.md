# Dependency Parsing as Sequence Labeling with Multi-Task Learning (MTL)

This code is an upgraded version that runs on:

* ```Python 3.6```
* ```PyTorch 1.2.0```

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

#### Train a model

 ```bash
python main.py --config x 
```

* ```--train-config``` an example of a [config file for training](https://github.com/balthamel/dep2label-up/blob/master/config/train.config)
#### Parse with a pre-trained model

 ```bash
python decode.py --test x --gold x --model x/mod --status decode --gpu True --output x --ncrfpp x
```
where:

```Python
test=...  # file with encoded dependency trees as labels
gold=...    # file with depedencies in the CONLL format
model=... # path to the model directory ending with /mod
output=...   # output file with predicted dependencies in CONLL format
ncrfpp=... # path to the NCRF++ directory
```

