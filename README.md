# 🧱 Concrete Strength Prediction Web Application

This project is a Machine Learning–based web application designed to predict the **compressive strength of concrete** using user-defined mix proportions. The application provides an interactive interface for engineers and students to analyze concrete mix behavior before actual casting.

---

## 📌 Project Overview

Concrete strength depends on multiple factors such as cement content, water ratio, aggregates, and curing age. This application allows users to input these parameters and obtain an estimated concrete strength using a trained regression model.

---

## ⚙️ Features

- Interactive web interface built using **Flask**
- Sliders and manual input for concrete mix parameters
- Real-time mix insights:
  - Water–Cement Ratio
  - Concrete Age Category
  - Workability Indicator
- Machine Learning model for strength prediction
- Clean, responsive UI with modern design
- Reset functionality to clear inputs
- Background image–based professional layout

---

## 🧪 Input Parameters

The model predicts concrete strength using the following features (per cubic meter):

- Cement
- Blast Furnace Slag
- Fly Ash
- Water
- Superplasticizer
- Coarse Aggregate
- Fine Aggregate
- Age (days)

---

## 🧠 Machine Learning Model

- Model Type: **Gradient Boosting Regressor**
- Training Platform: **Scikit-learn**
- Hyperparameter tuning using **RandomizedSearchCV**
- Evaluation Metric: **R² Score**
- Achieved accuracy: **~94%**

---

## 🌐 Web Application Workflow

1. User enters concrete mix proportions
2. Inputs are preprocessed and passed to the ML model
3. The model predicts compressive strength
4. The result is displayed with strength category

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **NumPy**
- **Pandas**
- **HTML / CSS / JavaScript**

---

## 📁 Project Structure

