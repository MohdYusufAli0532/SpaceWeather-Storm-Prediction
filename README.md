# Space Weather Storm Predictor

This project leverages machine learning to predict geomagnetic storms based on space weather features. The predictor uses various indices such as the Kp index, AE, AL, AU, Ap, and F10.7 solar flux to forecast potential space weather events that could impact Earth’s technology.

## Project Overview

Space weather, particularly geomagnetic storms, can have a significant impact on Earth’s technological infrastructure, including satellites, communication systems, and power grids. The **Space Weather Storm Predictor** uses a trained machine learning model to predict whether a storm is likely based on these space weather features.

The goal of this project is to provide early warnings to mitigate the impact of solar storms on technological systems and infrastructure.

## Features

- Predicts the likelihood of a geomagnetic storm occurring.
- Utilizes space weather indices like Kp, AE, AL, AU, Ap, and F10.7 solar flux.
- Offers predictions with associated confidence scores.

## Requirements

- Python 3.7 or higher
- Streamlit
- XGBoost
- joblib
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/SpaceWeather_StormPredictor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SpaceWeather_StormPredictor
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

   - For Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - For Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally, use the following command:

```bash
streamlit run storm_app.py
```
