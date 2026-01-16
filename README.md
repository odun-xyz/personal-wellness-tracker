# 🌸 Personal Period & Wellness Tracker

**Private Console-Based Menstrual Cycle & Wellness Tracker** – A Python application for tracking cycles, symptoms, mood, and predictions.

**Student Information**  
- **Name**: Odunaya Esther Blessing 
- **Department**: Computer Science  
- **Matriculation Number**: [24/13963]  

**Course**:(SEN201) Assignment  

## Project Overview

This is a private, local-only console application designed to help users track:
- Menstrual cycle start dates
- Daily symptoms, flow, mood, and notes
- Predicted next period and ovulation window
- Monthly summaries
- All data is stored securely on the user's device (no internet, no cloud)

The application uses only Python's standard library (`datetime`, `json`, `os`).

## Names and Nomenclatures (Design matches Implementation 100%)

The following names are used consistently in both the system design and the actual code:

- **Class**: `CycleTracker`  
  - Attributes:  
    - `cycles` → list of `datetime.date` objects (cycle start dates)  
    - `symptoms` → dictionary with keys as "YYYY-MM-DD" strings and values as dicts  
    - `average_cycle_length` → integer (calculated or default 28)

  - Key methods (exact names in code):  
    - `add_cycle_start(date)`  
    - `log_symptoms(date, flow, mood, symptoms_list, notes)`  
    - `calculate_average_cycle()`  
    - `predict_next_period()`  
    - `predict_ovulation()`  
    - `view_history()`  
    - `view_monthly_summary(year, month)`

- **Global instance**: `tracker` → Single instance of `CycleTracker`

- **Data file**: `wellness_data.json` (persistent storage)

- **Key functions** (exact names used in code):
  - `load_data()`
  - `save_data()`
  - `add_new_cycle()`
  - `log_daily_symptoms()`
  - `view_cycle_history()`
  - `view_predictions()`
  - `view_monthly_summary()`
  - `display_menu()`
  - `main()`

- **Symptoms dictionary keys**: `"flow"`, `"mood"`, `"symptoms"`, `"notes"`

## Features

- Record new cycle start dates
- Log daily wellness data (flow level, mood, symptoms, notes)
- Calculate average cycle length from history
- Predict next period and approximate ovulation
- View full cycle history
- View monthly symptom summaries
- Automatic data saving/loading

## How to Run

1. Make sure you have Python 3 installed
2. Run the application:
   ```bash
   python period_tracker.py
