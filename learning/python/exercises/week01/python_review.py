"""Day 1: Python 基础练习。

完成 TODO 后运行本文件。不要直接删除断言，它们用来检查结果。
"""


def summarize_study_time(minutes: list[int]) -> dict[str, float | int]:
    """返回总时长、平均时长和最长时长。"""
    # TODO: 在这里实现，不调用第三方库。
    raise NotImplementedError


if __name__ == "__main__":
    study_minutes = [25, 30, 40, 25]
    summary = summarize_study_time(study_minutes)

    assert summary["total"] == 120
    assert summary["average"] == 30
    assert summary["maximum"] == 40
    print(summary)
