# sna_topic_11

Exercise regarding link prediction on a data set of "Der Standard"

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
