# sna_topic_11

Exercise regarding link prediction on a data set of "Der Standard".

Authors:
* Steindl Bernhard (01529136)
* Maliakel Paul Joe (12012422)
* Louis-Alexandre Dit Petit-Frere Judith (12024728)
* Bauernfeind Florian(11775814)

## Dataset files

Make sure you copy the dataset files to the `data` directory.
Do NOT commit the dataset files because they are large in size.
You should have the following dataset files in place:

```
./data/Votes_16052019_31052019.csv
./data/Votes_01052019_15052019.csv
./data/Postings_16052019_31052019.csv
./data/Postings_01052019_15052019.csv
./data/Following_Ignoring_Relationships_01052019_31052019.csv
```

## Setup workspace

Make sure you have installed `conda` and `pip`.
Run the following commands to create a new conda environment "SNS_2021W" using Python 3.9 and the libraries defined in `"requirements4pip.txt"`.

```bash
conda create -n "SNS_2021W" python=3.9 -y
conda activate SNS_2021W
pip install -r requirements4pip.txt
```

## Project structure

The next table explains what the Jupyter notebooks are doing and how the project structure looks like.

| File or Folder | Description |
|--------------|-----------|
| `sna_preprocessing_commented.ipynb` | Contains code for pre-processing, feature extraction (graph-based and node-based TF-IDF features) and result serialization for the **Commented relation**. |
| `sna_preprocessing_common_interest.ipynb` | Contains code for pre-processing, graph-based feature extraction and result serialization for the **Common-Interest relation**. |
| `sna_preprocessing_like.ipynb` | Contains code for pre-processing, graph-based feature extraction and result serialization for the **Like relation**. |
| `link_prediction.ipynb` | This notebook implements the machine learning pipeline for predicting links in our social networks. It loads features of the three relations (like, commented and common-interest), pre-processes the data (downsampling, resampling, train-test split etc.), trains and evaluates using machine learning classifiers. |
| `data/` | Folder used for storing *derStandard* datasets (see Dataset files). Also used for storing serializations of graph-based features by the notebooks `sna_preprocessing_like.ipynb` and `sna_preprocessing_common_interest.ipynb`. |
| `output/` | Folder used by `sna_preprocessing_commented.ipynb` for serialization of graph-based and node-based features, as well as intermediate outputs from NLP operations. |
| `data/engineered_features` | Folder is used by `link_prediction.ipynb` containing only those feature serializations (either as csv or pickle files) necessary for running experiments with our machine learning pipeline. |