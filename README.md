# diabetes-prediction-STREAMLIT
# 🩺 Diabetes Prediction

This project uses a machine learning model to predict diabetes based on various health parameters. The model is deployed using a Streamlit web application, allowing users to input health data and receive a diabetes prediction.

## 📁 Project Structure

- `📄 diabetes.csv`: The dataset used for training the machine learning model.
- `📄 train_model.py`: Script to train the machine learning model and save it as a pickle file.
- `📄 app.py`: Streamlit application script for the diabetes prediction web app.
- `📄 diabetes_model.pkl`: The trained machine learning model saved as a pickle file.

## 📦 Requirements

- Python 3.x
- Pandas
- Scikit-learn
- Streamlit

## ⚙️ Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/himanshun3gi/diabetes-prediction-STREAMLIT.git
    cd diabetes-prediction
    ```

2. **Install the required packages:**

    ```sh
    pip install pandas scikit-learn streamlit
    ```

## 🚀 Usage

### 🏋️‍♂️ Train the Model

If you need to train the model (optional if `diabetes_model.pkl` is provided):

1. Ensure `diabetes.csv` is in the project directory.
2. Run the training script:

    ```sh
    python train_model.py
    ```

    This will generate `diabetes_model.pkl` in the project directory.

### 💻 Run the Streamlit App

To start the Streamlit web application:

```sh
streamlit run app.py
