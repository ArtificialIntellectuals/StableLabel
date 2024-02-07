# StableLabel: Dataset Cleaning for Image Classification

## Overview

This repository contains code and resources for a project focused on automated cleaning of datasets for image classification tasks. The project employs various techniques, including prompt engineering, feature engineering, and supervised machine learning, to enhance the quality of labeled datasets used for training image classification models.

## Key Features

- **Prompt Engineering:** Utilize the multi-modal capabilities of ALIGN [1] or CLIP [2] to judge the correspondence between text labels and images. The experiments focus on addressing challenges in representing "not a" cases.
- **Similarity Analysis:** Leverage and analyse the encoded similarities in the image embeddings of the datasets to clean.
- **Supervised Learning:** Train classifiers to predict whether an image is polluted or not, leveraging labeled datasets subject to highly automated construction.
- **Ensemble Learning:** Combine multiple models to improve recall and enhance the robustness of dataset cleaning.
- **Feature Engineering:** Train on feature vectors with features such as average pairwise similarity of dataset image embeddings and similarities of image embeddings to textual embeddings to enhance dataset cleaning and model training.

## Repository Structure

- `results/`: Contains the results of the different experiments.

- `datasets/`: Includes all dataset related information, e.g. indices of mislabelled instances or produced embeddings (both of textual descriptions and of images).

  Please, note that we do not publish the dataset we use for the experiments directly, but it can be accessed through https://www.kaggle.com/c/dogs-vs-cats .

- `helper_scripts/`: Miscellaneous. Used as assistance during the development phase of the solutions.

## Getting Started

1. Clone this repository to your local machine.
2. Download the dataset from https://www.kaggle.com/c/dogs-vs-cats
3. Explore the notebooks in the main directory to understand the available scripts.
4. Use the provided datasets or replace them with your own data as needed.
5. Run the different notebooks  to perform dataset cleaning using the chosen strategy. Each notebook offers a set of settings to adjust the script to the specific case at hand.

## Contribution Guidelines

Contributions to this project are welcome! If you have ideas for improvements, new features, or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a new pull request and describe the changes you've made.

## Contact

For any questions or inquiries about the project, feel free to contact us at ...



## References

[1] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal,
Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual
models from natural language supervision. In International conference on machine learning, pp.
8748–8763. PMLR, 2021

[2] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc V. Le, Yun-Hsuan
Sung, Zhen Li, and Tom Duerig. Scaling up visual and vision-language representation learning
with noisy text supervision. CoRR, abs/2102.05918, 2021. URL https://arxiv.org/abs/
2102.0591