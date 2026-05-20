# 💊 Fast Dissolving Tablet (FDT) Prediction System

A **Machine Learning-powered web application** that predicts the **disintegration time of Fast Dissolving Tablets (FDTs)** based on pharmaceutical formulation parameters.  
Built using **Python, Scikit-learn, and Streamlit**, this project helps analyze tablet formulations and estimate tablet performance efficiently.

---

## 🚀 Live Demo
👉 https://your-streamlit-app-link.streamlit.app/

---

## 📌 Project Overview

Fast Dissolving Tablets (FDTs) are designed to dissolve quickly in the mouth without requiring water, improving patient convenience and compliance.

This project uses a **Machine Learning model** to predict the **disintegration time** of tablets using formulation ingredients and physical tablet properties.

The application provides:
- Real-time tablet prediction
- Interactive pharmaceutical dashboard
- Formulation analysis
- Quick and accurate predictions

---

## 🧠 Machine Learning Model

- **Algorithm Used:** Random Forest Regressor  
- **Preprocessing:** Feature Encoding & Data Cleaning  
- **Train-Test Split:** 80% / 20%  
- **Evaluation Metrics:**  
  - R² Score  
  - Mean Absolute Error (MAE)  
  - Mean Squared Error (MSE)  

---

## 📊 Input Features

The model uses the following pharmaceutical formulation parameters:

- Drug Amount (mg)  
- Type of Superdisintegrant  
- Concentration of Superdisintegrant (mg)  
- Binder Type  
- Binder Percentage (%)  
- Hardness (Kg/cm²)  
- Friability (%)  

---

## 🎯 Output

The application predicts:

- **Disintegration Time (seconds)**  

The app may also display:
- Formulation insights  
- Prediction confidence  
- Comparative analysis charts  

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Libraries:**  
  - Pandas  
  - NumPy  
  - Scikit-learn  
  - Joblib  
  - Matplotlib  

---

## 📂 Project Structure

```bash
FDT-Model/
│── Dataset/
│── Jupyter-Notebook/
│── app.py
│── fdt_model.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/Shoaib-72/FDT-Model.git
cd FDT-Model
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Add multiple ML model comparisons  
- Improve prediction accuracy  
- Add pharmaceutical analytics dashboard  
- Enable formulation optimization suggestions  
- Deploy advanced visualization features  

---

## 👨‍💻 Author

**Shoaib Chiplunkar**  

- GitHub: https://github.com/Shoaib-72  
- LinkedIn: https://www.linkedin.com/in/muhammad-shoaib-chiplunkar/ 

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
