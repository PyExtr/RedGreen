import os

BEST_MODEL_PATH = "../back_end/ecapa_best_model.pth"
BEST_SCORE_FILE = "best_score.txt"

all_time_best_val_acc = 0.0
all_time_best_f1 = 0.0

if os.path.exists(BEST_SCORE_FILE):
    with open(BEST_SCORE_FILE, "r") as f:
        score_data = f.read().strip().split(",")
        try:
            all_time_best_val_acc = float(score_data[0])
            all_time_best_f1 = float(score_data[1]) if len(score_data) > 1 else 0.0
        except ValueError:
            print("⚠️ Could not parse BEST_SCORE_FILE. Resetting scores.")


