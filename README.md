# Breast Cancer Survival Prediction [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://breast-cancer-survival-pred.streamlit.app/)

This project aims to predict the survival rate of breast cancer patients based on various features. It utilizes a CatBoost model trained on a dataset containing information about patients such as age, gender, tumor stage, protein levels and treatment history.

## Repository Structure

- **model:** Contains saved pickle files of the CatBoost model and the preprocessing pipeline.
- **src:** Includes scripts for different purposes:
  - *hyperparameters.py:* Defines hyperparameters used in the model.
  - *logger.py:* Logging functionalities for tracking the training process.
  - *preprocessing.py:* Preprocessing methods and functions.
  - *train.py:* Script for training the breast cancer survival prediction model.
  - *ingest_data.py:* Data ingestion and processing script.
- **notebook:** Experimental notebooks used for analysis and development.
- *run_pipeline.py:* Script to initiate the training process using the source code present in the src directory.
- *streamlit_app.py:* Streamlit application for demonstrating the functionality of the trained model.

## Usage

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/hardikjp7/Breast-Cancer-Survival-Prediction.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Breast-Cancer-Survival-Prediction
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Training

To train the model, use the `run_pipeline.py` script:
```sh
python run_pipeline.py
```

### Demo

To run the Streamlit app for demo purposes, use the following command:
```sh
streamlit run st.py
```
This will launch a local server where you can interact with the trained model through a user-friendly interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to add more sections or details based on your project's specific needs and requirements.
