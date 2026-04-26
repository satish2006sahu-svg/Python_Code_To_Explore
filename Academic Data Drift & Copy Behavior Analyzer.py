import random
import math
import copy
import pandas as pd
import numpy as np


def build_data(n=12):
    res = []
    seen = set()
    while len(res) < n:
        sid = random.randint(100, 999)
        if sid not in seen:
            seen.add(sid)
            res.append({
                "id": sid,
                "marks": random.randint(40, 100),
                "attendance": random.randint(50, 100),
                "scores": [random.randint(10, 30), random.randint(10, 20)]
            })
    return res


def get_mean(data, key):
    return sum(x[key] for x in data) / len(data)


def apply_mutations(data, roll):
    mod = roll % 3
    if mod == 0:
        mod = 1

    mutated_idx = []
    for i in range(len(data)):
        if i % mod == 0:
            data[i]['marks'] = data[i]['marks'] + math.sqrt(data[i]['marks'])
            data[i]['scores'][0] += 5
            data[i]['attendance'] = min(100, data[i]['attendance'] + 10)
            mutated_idx.append(i)
    return mutated_idx


def check_status(drift, fail, threshold):
    if fail:
        return "Copy Failure Detected"
    if drift > threshold * 2:
        return "Critical Drift"
    if drift > threshold:
        return "Minor Drift"
    return "Stable System"


def main():
    name = "Satish"
    roll = 620

    print("Data Drift Analyzer")
    print(f"Student: {name}")
    print(f"Roll: {roll}\n")

    base_data = build_data(12)
    pure = copy.deepcopy(base_data)

    start_mean = get_mean(base_data, 'marks')

    shallow_copy = copy.copy(base_data)
    deep_copy = copy.deepcopy(base_data)

    mutated_indexes = apply_mutations(shallow_copy, roll)
    apply_mutations(deep_copy, roll)

    print(f"Personalization Applied: Roll Number {roll} % 3 = {roll % 3}")
    print(f"Because of this, we only mutated indexes: {mutated_indexes}\n")

    df_base = pd.DataFrame(base_data)
    df_shallow = pd.DataFrame(shallow_copy)
    df_deep = pd.DataFrame(deep_copy)

    deep_marks = np.array([x['marks'] for x in deep_copy])
    arr_std = np.std(deep_marks)
    arr_median = np.median(deep_marks)

    normalized = (deep_marks - np.min(deep_marks)) / (np.max(deep_marks) - np.min(deep_marks))

    end_mean = get_mean(deep_copy, 'marks')
    drift_val = abs(start_mean - end_mean)

    thresh = 4.5

    failed_copy = False
    if base_data != pure:
        failed_copy = True

    status = check_status(drift_val, failed_copy, thresh)

    print("Original DataFrame:")
    print(df_base.head())
    print("\nShallow Copy DataFrame:")
    print(df_shallow.head())
    print("\nDeep Copy DataFrame:")
    print(df_deep.head())

    print(f"\nCalculated Drift: {drift_val:.4f}")

    print(f"Normalized Marks (first 5): {np.round(normalized[:5], 2)}")
    print("Note: The Mean below was calculated manually without using NumPy.")

    stats_tuple = (round(end_mean, 2), round(drift_val, 2), round(float(arr_std), 2), round(float(arr_median), 2))
    print(f"Stats (Manual Mean, Drift, Std, Median): {stats_tuple}")

    print(f"Status: {status}")

    print("\nWhy did shallow copy cause drift?")
    print("When we use shallow copy, the outer list is duplicated but the dictionaries inside are just referenced.")
    print("This means modifying a dictionary in the shallow copy also changes it in the original data.")
    print("That's why the original data was altered unexpectedly, triggering a copy failure.")


main()