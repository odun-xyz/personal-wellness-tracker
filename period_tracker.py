import json
import os
from datetime import datetime, timedelta

DATA_FILE = "wellness_data.json"

class CycleTracker:
    def __init__(self):
        self.cycles = []  # list of datetime.date
        self.symptoms = {}  # { "2026-01-05": { "flow": "heavy", "mood": "irritable", "symptoms": ["cramps"], "notes": "" } }
        self.average_cycle_length = 28  # default

    def add_cycle_start(self, date):
        if date not in self.cycles:
            self.cycles.append(date)
            self.cycles.sort()
            self.calculate_average_cycle()
            print(f"New cycle started on {date.strftime('%B %d, %Y')} recorded.")

    def log_symptoms(self, date, flow, mood, symptoms_list, notes):
        date_str = date.strftime("%Y-%m-%d")
        self.symptoms[date_str] = {
            "flow": flow,
            "mood": mood,
            "symptoms": symptoms_list,
            "notes": notes
        }
        print(f"Symptoms logged for {date.strftime('%B %d, %Y')}.")

    def calculate_average_cycle(self):
        if len(self.cycles) < 2:
            self.average_cycle_length = 28
            return
        diffs = [(self.cycles[i+1] - self.cycles[i]).days for i in range(len(self.cycles)-1)]
        self.average_cycle_length = round(sum(diffs) / len(diffs))

    def predict_next_period(self):
        if not self.cycles:
            return None
        last_cycle = self.cycles[-1]
        return last_cycle + timedelta(days=self.average_cycle_length)

    def predict_ovulation(self):
        next_period = self.predict_next_period()
        if next_period:
            return next_period - timedelta(days=14)  # Approx ovulation
        return None

    def view_history(self):
        if not self.cycles:
            print("No cycles recorded yet.")
            return
        print("\nCycle Start Dates:")
        for c in self.cycles:
            print(f"• {c.strftime('%B %d, %Y')}")

    def view_monthly_summary(self, year, month):
        print(f"\nSummary for {datetime(year, month, 1).strftime('%B %Y')}")
        for date_str, data in self.symptoms.items():
            d = datetime.strptime(date_str, "%Y-%m-%d")
            if d.year == year and d.month == month:
                print(f"{d.strftime('%d')}: Mood: {data['mood']}, Flow: {data['flow']}, Symptoms: {', '.join(data['symptoms'])}")

tracker = CycleTracker()

def load_data():
    global tracker
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                tracker.cycles = [datetime.strptime(d, "%Y-%m-%d").date() for d in data.get("cycles", [])]
                tracker.symptoms = data.get("symptoms", {})
                tracker.calculate_average_cycle()
        except:
            print("Could not load data. Starting fresh.")

def save_data():
    data = {
        "cycles": [d.strftime("%Y-%m-%d") for d in tracker.cycles],
        "symptoms": tracker.symptoms
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("Your data has been saved safely.")

def add_new_cycle():
    date_str = input("\nEnter cycle start date (YYYY-MM-DD): ").strip()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        tracker.add_cycle_start(date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def log_daily_symptoms():
    date_str = input("\nEnter date to log (YYYY-MM-DD): ").strip()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        flow = input("Flow (none/light/medium/heavy): ").strip().lower()
        mood = input("Mood (happy/calm/anxious/irritable/sad): ").strip().lower()
        symps = input("Symptoms (comma-separated, e.g. cramps, bloating): ").strip()
        symptoms_list = [s.strip() for s in symps.split(",") if s.strip()]
        notes = input("Additional notes (optional): ").strip()
        tracker.log_symptoms(date, flow, mood, symptoms_list, notes)
    except ValueError:
        print("Invalid date format.")

def view_cycle_history():
    tracker.view_history()
    print(f"\nAverage cycle length: {tracker.average_cycle_length} days")

def view_predictions():
    next_period = tracker.predict_next_period()
    ovulation = tracker.predict_ovulation()
    if next_period:
        print(f"\nPredicted next period: {next_period.strftime('%B %d, %Y')}")
        print(f"Predicted ovulation window: around {ovulation.strftime('%B %d, %Y')}")
    else:
        print("\nAdd at least one cycle to see predictions.")

def view_monthly_summary():
    try:
        year = int(input("\nEnter year (e.g., 2026): "))
        month = int(input("Enter month (1-12): "))
        tracker.view_monthly_summary(year, month)
    except ValueError:
        print("Invalid input.")

def display_menu():
    print("\n" + "🌸 " * 20)
    print("    PERSONAL PERIOD & WELLNESS TRACKER")
    print("🌸 " * 20)
    print("1. Add New Cycle Start")
    print("2. Log Daily Symptoms")
    print("3. View Cycle History")
    print("4. View Predictions")
    print("5. View Monthly Summary")
    print("6. Exit")
    print("🌸 " * 20)

def main():
    print("Welcome to your private wellness tracker 💕")
    load_data()
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_new_cycle()
        elif choice == "2":
            log_daily_symptoms()
        elif choice == "3":
            view_cycle_history()
        elif choice == "4":
            view_predictions()
        elif choice == "5":
            view_monthly_summary()
        elif choice == "6":
            save_data()
            print("\nTake care of yourself! See you soon 🌸")
            break
        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()