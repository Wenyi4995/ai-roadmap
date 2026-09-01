"""Day 1: Python 基础练习。

完成 TODO 后运行本文件。不要直接删除断言，它们用来检查结果。
"""


def summarize_study_time(minutes):
    total = sum(minutes)
    average = total / len(minutes)
    maximum = max(minutes)

    return {
        "total": total,
        "average": average,
        "maximum": maximum,
    }

def summarize_study_time_manually(minutes):
    total = 0
    maximum = minutes[0]

    for minute in minutes:
        # TODO 1：把 minute 累加到 total
        total += minute
        # TODO 2：如果 minute 比 maximum 大，更新 maximum
        if minute > maximum:
            maximum = minute

    average = total / len(minutes)

    return {
        "total": total,
        "average": average,
        "maximum": maximum,
    }


if __name__ == "__main__":
    study_minutes = [20, 35, 45]
    summary = summarize_study_time(study_minutes)

    assert summary["total"] == 100
    assert summary["average"] == 100 / 3
    assert summary["maximum"] == 45
    print(summary)

    manual_summary = summarize_study_time_manually(study_minutes)
    assert manual_summary["total"] == 100
    assert manual_summary["average"] == 100 / 3
    assert manual_summary["maximum"] == 45
    print(manual_summary)
    

