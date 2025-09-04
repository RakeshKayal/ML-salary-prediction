# 💼 Salary Prediction Model (ML + API Integration)

This project predicts salaries based on features like **experience, age, and education level** using machine learning.  
The trained model is saved and also exposed through an API (via `api_create.ipynb`) so that it can be consumed by a **Spring Boot backend**.

---

## 🚀 Features
- Data preprocessing and training with **scikit-learn**
- Model persistence using **joblib**
- Accuracy evaluation with metrics
- API file (`api_create.ipynb`) for backend integration
- Dataset included (`regression_dataset.csv`)

---

## 📂 Repository Structure
- `Salary-Prediction.ipynb` → Main ML workflow (EDA, training, evaluation, saving model)  
- `api_create.ipynb` → API creation file (Spring Boot can call this to use the model)  
- `model.pkl` → Saved trained ML model  
- `regression_dataset.csv` → Dataset used for training/testing  
- `.ipynb_checkpoints/` → Jupyter auto-saves (not needed in production)  

---

## 🛠️ Installation & Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/RakeshKayal/ML-salary-prediction.git
   cd ML-salary-prediction
