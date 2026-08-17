# AI Roadmap

这是一个面向 2027 年暑期实习和 2028 届秋招的长期学习仓库，目标是一线互联网公司的大模型后训练、评测与应用算法岗位。

仓库既记录学习过程，也沉淀可以复习、复现和展示的技术成果。计划和日志按时间组织，知识与项目按主题组织，避免一年后出现几十个互相割裂的周目录。

## 快速入口

- [长期路线图](ROADMAP.md)
- [总进度面板](PROGRESS.md)
- [第一周计划](plans/2026/week-01.md)
- [第一周日志](logs/2026/08/week-01.md)
- [技能矩阵](career/skills-matrix.md)

## 仓库结构

```text
ai-roadmap/
├─ plans/              # 月度和每周计划：什么时候做
├─ logs/               # 每日记录与周复盘：实际做了什么
├─ learning/           # 可长期复习的知识与练习
├─ projects/           # 独立、可复现、可写入简历的项目
├─ practice/           # 算法题与面试训练
├─ papers/             # 论文清单、笔记与复现记录
├─ career/             # 技能矩阵、实习与面试材料
├─ templates/          # 可重复使用的计划与记录模板
├─ ROADMAP.md          # 一年方向与阶段验收
└─ PROGRESS.md         # 当前状态和量化指标
```

## 每周工作流

1. 周一前从模板创建本周计划，最多设置 3 个核心成果。
2. 每天只选择一个最小启动动作，完成后记录结果和障碍。
3. 学习笔记归入 `learning/`，项目代码归入 `projects/`，不要堆进日志。
4. 周日完成复盘，更新 `PROGRESS.md` 和技能矩阵。
5. 每四周做一次月度回顾，决定继续、调整或删除低价值任务。

## 完成定义

一个学习任务只有同时满足以下条件才算完成：

1. 代码或笔记已保存到正确目录。
2. 代码能够运行，关键结果已经记录。
3. 自己能够解释核心原理和常见失败原因。
4. 已更新日志或进度面板。

## 提交约定

推荐使用小而清晰的提交：

```text
study: finish autograd exercises
code: implement manual linear regression
experiment: compare two learning rates
docs: complete week 1 reflection
career: update skills matrix
```

大模型权重、数据集、虚拟环境和实验输出不提交到 Git。项目需要大文件时，在 README 中记录下载方式、版本和校验信息。

## 当前阶段

- 阶段：基础补齐
- 当前计划：[2026 年第一周](plans/2026/week-01.md)
- 当前项目：[线性回归](projects/linear-regression/README.md)
- 每日最低目标：完成 1 个 25 分钟专注块
