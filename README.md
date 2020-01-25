# Datathon2020
Model to predict wildfires severity class - tbr1, nt13, zdm3


Steps to reproduce result ---

Python Modules used - Sklearn, Numpy

1. Clone Repo

2. Download the dataset - https://www.kaggle.com/rtatman/188-million-us-wildfires, place in the cloned repo directory

3. Run firestocsv.py

4. Run code.py

5. Run model.py

The dataset is seperated into groups based off the statistical cause. For each group a Random Forest Classifier is used to attempt to predict the severity class of the fire. Resulting accuracy is printed at the end of each group.
