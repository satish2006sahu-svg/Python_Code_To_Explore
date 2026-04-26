import random
import math
import pandas as pd
import numpy as np


def generate_data(roll):
    n_students = 10 + (roll % 10)
    data = []
    seen = set()

    while len(data) < n_students:
        sid = random.randint(1000, 9999)
        if sid not in seen:
            seen.add(sid)

            m = random.randint(0, 100)
            att = random.randint(0, 100)
            assign = random.randint(0, 50)

            data.append((sid, m, att, assign))

    return data


def classify_students(data):
    classes = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for row in data:
        sid, m, att, _ = row

        # Check Top Performer first to prevent logical overlap
        if m > 90 and att > 80:
            classes["Top Performer"].append(sid)
        elif m < 40 or att < 50:
            classes["At Risk"].append(sid)
        elif 40 <= m <= 70:
            classes["Average"].append(sid)
        elif 71 <= m <= 90:
            classes["Good"].append(sid)

    return classes


def analyze_data(data):
    df = pd.DataFrame(data, columns=["id", "marks", "attendance", "assignment"])

    df["perf_idx"] = [
        round((m * 0.6 + a * 0.4) * math.log(att + 1), 2)
        for m, att, a in zip(df["marks"], df["attendance"], df["assignment"])
    ]

    m_arr = df["marks"].values
    att_arr = df["attendance"].values

    mean_val = np.mean(m_arr)
    med_val = np.median(m_arr)
    std_val = np.std(m_arr)

    # Robust correlation handling to prevent division by zero or NaN issues
    if len(m_arr) > 1 and np.std(m_arr) > 0 and np.std(att_arr) > 0:
        corr = np.corrcoef(m_arr, att_arr)[0, 1]
    else:
        corr = 0

    min_m = np.min(m_arr)
    max_m_np = np.max(m_arr)
    if max_m_np > min_m:
        norm_m = (m_arr - min_m) / (max_m_np - min_m)
    else:
        norm_m = np.zeros_like(m_arr, dtype=float)

    df["norm_marks"] = np.round(norm_m, 2)

    max_m = m_arr[0]
    for m in m_arr:
        if m > max_m:
            max_m = m

    stats = {
        "mean": mean_val,
        "median": med_val,
        "std": std_val,
        "corr": corr,
        "max": max_m
    }

    return df, stats


def main():
    name = "Satish"
    roll = 620

    print("Academic Intelligence System")
    print(f"Student: {name}")
    print(f"Roll: {roll}")

    raw = generate_data(roll)
    df, stats = analyze_data(raw)
    categories = classify_students(raw)

    print(f"\nGenerated {len(raw)} students based on 10 + (Roll % 10)")

    print("\nData:")
    print(df.to_string(index=False))

    # Demonstrating Set Requirement Explicitly
    active_categories = set(k for k, v in categories.items() if len(v) > 0)
    print(f"\nActive Categories (Set representation): {active_categories}")

    print("\nCategories:")
    for k, v in categories.items():
        print(f"  {k}: {v}")

    # Normalized Marks Sample
    print(f"\nNormalized Marks Sample (first 5): {df['norm_marks'].head().tolist()}")

    print("\nStats:")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Median: {stats['median']:.2f}")
    print(f"  Std Dev: {stats['std']:.2f}")
    print(f"  Correlation: {stats['corr']:.2f}")
    print(f"  Manually Calculated Max Marks: {stats['max']}")

    summary = (round(float(stats['mean']), 2), round(float(stats['std']), 2), int(stats['max']))
    print(f"\nSummary Tuple: {summary}")

    is_consistent = stats['std'] < 15
    at_risk_count = len([x for x in df["attendance"] if x < 50])
    high_achievers = len(categories["Top Performer"])

    status = "Moderate Performance"
    if at_risk_count > 3:
        status = "Critical Attention Required"
    elif is_consistent and high_achievers >= 2:
        status = "Stable Academic System"

    print(f"\nFinal Insight: {status}")

    print("\nWhy the perf_idx formula works:")
    print("It gives more weight to marks (60%) than assignments (40%) and uses a log scale for attendance.")
    print("This means missing a lot of classes hurts your score badly, but having perfect attendance")
    print("won't completely save you if your marks are terrible.")


main()
