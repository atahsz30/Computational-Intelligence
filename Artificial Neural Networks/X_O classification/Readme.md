# Project File Description and Model Overview

This repository contains the implementation and comparison of several **classification models**.  
The main focus of the project is to **evaluate and compare the performance of different machine learning models** on a classification task.

---

## 📁 Project Structure

### `models_comparison/`
This folder contains:
- The **classification code** (`x_o classification`)
- Evaluation and comparison of different models’ performance

---

### Contents

#### 1. Data Generator
- A class written to **generate the required dataset** for training and testing the models.

#### 2. Linear Models (Python)
The following models are implemented in Python:
- **Adaline**
- **Perceptron**
- **Multi-Category Perceptron**

Each model:
- Is trained on the dataset
- Computes and stores its **final learned weights**

---

#### 3. MLP Model
- The **Multi-Layer Perceptron (MLP)** model is implemented separately.
- This model is written in **C++** and located in the `cpp/` folder.

---

#### 4. Model Weights Storage
- The final weights of each trained model are stored in **individual text files**.
- These files are used later for inference and prediction.

---

#### 5. Prediction Classes
The following classes are responsible for computing the output of each model:
- `Pred_MLP`
- `Pred_MultiCategory`
- `Pred_Others`

These classes load the saved weights and calculate the output for a given input sample.

---

## ▶️ Program Execution

- The **main execution** is handled in the `main` class.
- After running the program, a **GUI window** appears.
- The user is prompted to:
  1. Enter the desired input pattern
  2. Select the model number to be used for prediction

---

## 🔢 Model Selection Mapping

Each model is selected using the following numeric identifiers:

| Model | Number |
|------|--------|
| Hebb | 1 |
| Perceptron | 2 |
| Adaline | 3 |
| Multi-Category Perceptron | 4 |
| MLP | 5 |

---

## 🎯 Purpose of the Project

- Compare different classification models
- Analyze learning behavior and output accuracy
- Demonstrate both **Python-based** and **C++-based** implementations

---


## 📜 License

