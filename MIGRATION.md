**2026-10-26：项目迁移至 G 盘**

主工作区：`G:\CodexProjects\ai-roadmap`。

原目录：`C:\Users\4995Yi\Documents\Codex\2026-08-17\zhe\work\ai-roadmap`，仅作为迁移时的备份保留，后续不在原目录继续修改代码或学习记录。

已复制整个仓库，包括 `.git`、未提交修改、全部学习项目、计划、日志、数据、生成图片与 `.venv`。复制完成时共 21,928 个文件，1,376,220,726 字节；逐文件 SHA-256 比较通过，无缺失、额外文件或内容不一致。

校验报告保存在 `G:\CodexProjects\migration-reports\ai-roadmap-verified-2026-10-26.json`；复制日志保存在同目录。校验之后的迁移说明、工作区约定与虚拟环境激活路径修改属于有意变更，不属于复制差异。

运行验证已通过：G 盘虚拟环境的 Python／PyTorch 与 pip、二分查找原有断言、线性回归训练，以及服饰图像数据读取与预览输出。激活脚本中的旧路径已修正，并按已安装包的入口定义重建既有命令启动器，使其使用 G 盘解释器。

2026-10-26 再次核验：重新逐文件比较当前 C 盘备份与 G 盘，学习代码、数据与未提交成果无意外差异，Git HEAD 和暂存记录一致。发现旧 Codex 会话新增 4 个 Git 检查点文件，已逐个复制到 G 盘并核对 SHA-256；复核报告为 `G:\CodexProjects\migration-reports\ai-roadmap-recheck-2026-10-26.json`。

再次运行的 7 个入口均通过：两数之和、股票利润、有效括号、二分查找、手动线性回归、标准 PyTorch 线性回归、服饰数据预览。此核验确认现有已实现代码在 G 盘可运行，不代表尚未实现的视觉训练任务已经完成。

旧目录被其他程序占用，重命名失败，因此没有建立旧路径到 G 盘的目录链接。没有停止占用程序，也没有删除原文件。旧聊天中的 C 盘文件链接不会自动变成 G 盘链接；以本目录为准。

**在 Codex 中切换后续聊天的工作目录**

在项目菜单中选择 Edit project／编辑项目，把 `G:\CodexProjects\ai-roadmap` 添加为项目文件夹，并设为 Make primary／主目录。之后相关新聊天从这个项目中开始。若当前版本只提供打开文件夹，则打开此 G 盘目录作为项目。

当前工具没有项目／聊天路径管理接口，未修改 Codex 内部数据库，未搬动应用管理的聊天历史。聊天内容与本地项目目录是不同的数据；本次迁移的是工作文件和项目约定。

依据：[OpenAI 官方项目文档](https://learn.chatgpt.com/docs/projects)。

**常用入口**

- [总进度](PROGRESS.md)
- [完整学习路线](plans/vision-multimodal-roadmap.md)
- [当前视觉项目](projects/fashion-classifier/README.md)

在 PowerShell 中运行现有数据预览工具：

```powershell
Set-Location -LiteralPath 'G:\CodexProjects\ai-roadmap'
& 'G:\CodexProjects\ai-roadmap\.venv\Scripts\python.exe' 'G:\CodexProjects\ai-roadmap\projects\fashion-classifier\inspect_data.py'
```

原 C 盘目录因文件删除规则保留。如需释放其占用空间，由用户在确认切换项目并完成核验后手动清理；本次未批量删除。

用户于本次复核中提出核验通过后删除 C 盘项目。现有文件安全规则仍要求整目录批量清理由用户手动执行，故未删除；旧会话也仍在 C 盘生成检查点，应先切换到 G 盘项目。
