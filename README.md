# 学习 Agent 后端
## Day1 环境与项目初始化学习记录
日期：2026-07-06
今天主要完成了 Python 后端项目的基础环境搭建，并创建了第一个后端项目目录

### 今日完成内容
1.创建 `learning-backend` 项目目录
2.使用 VS Code 打开项目
3.创建 Python 虚拟环境 `.venv`
4.了解虚拟环境的作用：为当前项目隔离依赖，避免不同项目之间包版本冲突
5.创建基础项目文件，包括 `main.py`、`README.md` 等
6.初始化 Git 仓库，项目中生成 `.git` 目录
7.完成算法题「两数之和」

### 核心理解
`.venv` 是当前项目独立的 Python 环境，后续安装的依赖会放在虚拟环境中，而不是直接污染全局 Python 环境
Git 仓库通过 `.git` 目录保存项目版本历史。只要项目中有 `.git`，说明当前目录已经被 Git 管理

### 今日收获
今天完成了后端学习的第一步：把项目目录、Python 环境、编辑器和 Git 仓库准备好。后续可以在这个项目基础上继续安装依赖、编写接口和提交代码


## Day2 依赖管理与 FastAPI 启动学习记录
日期：2026-07-07
今天主要学习了 Python 项目的依赖管理，并成功启动了第一个 FastAPI 应用

### 今日完成内容
1.激活项目虚拟环境 `.venv`
2.使用 `pip` 安装 `fastapi` 和 `uvicorn`
3.使用 `pip freeze > requirements.txt` 生成项目依赖清单
4.理解 `requirements.txt` 的作用：记录项目依赖，方便别人复现运行环境
5.使用 `uvicorn main:app --reload` 启动 FastAPI 项目
6.访问 `http://127.0.0.1:8000/docs`，成功打开 Swagger 接口文档页面
7.确认 `/health` 接口已经出现在文档中
8.完成一次 Git 提交，保存当前项目状态

### 核心理解
`pip` 是 Python 的包管理工具，用来安装第三方库。
`requirements.txt` 是项目依赖清单，别人拿到项目后可以通过下面命令安装同样的依赖：
```cmd
pip install -r requirements.txt
```


## Day3 Git 学习记录
日期：2026-07-08
今天主要复习并练习了 Git 的本地版本管理流程，包括 `git status`、`git diff`、`git add`、`git commit` 和 `git log --oneline`。

### 今日完成内容
1.使用 `git status` 查看当前项目文件状态，判断文件是否被修改、是否进入暂存区、是否已经提交
2.使用 `git diff` 查看本次修改的具体内容，确认提交前知道自己改了什么
3.使用 `git add` 将修改加入暂存区
4.使用 `git commit` 将暂存区内容保存为一次本地提交
5.使用 `git log --oneline` 查看提交历史，确认提交记录是否生成
6.理解了工作区、暂存区、本地仓库之间的关系
7.了解 `.gitignore` 的作用，知道 `.venv/`、`__pycache__/`、`.env` 等文件通常不应该提交到 Git 仓库

### 核心理解
Git 的一次基本提交流程是：
```cmd
git status
git diff
git add README.md
git commit -m "docs: add day3 git learning notes"
git log --oneline
```


## Day4 学习总结：HTTP 与 Apifox 调试
日期：2026-07-09
今天学习了 HTTP 请求与响应的基本流程，并使用 Apifox 调试了本地 FastAPI 接口

### 完成内容
理解 HTTP 请求由请求方法、URL、请求头、请求体组成
理解 HTTP 响应由状态码、响应头、响应体组成
区分了 `GET` 和 `POST`：
`GET` 通常用于查询数据
`POST` 通常用于提交或创建数据。
认识了常见状态码：
`200`：请求成功
`201`：创建成功
`400`：请求参数错误
`404`：资源不存在
`500`：服务器内部错误

### 接口调试
使用 Apifox 请求本地接口：
请求方法：GET
请求地址：http://127.0.0.1:8000/health
状态码：200
响应时间：28ms
响应大小：140B
响应内容：{"status": "ok"}
结论：后端服务正常运行，Apifox 可以成功调用本地 FastAPI 接口


## Day5 学习总结：FastAPI 第一个接口
日期：2026-07-10
今天学习了 FastAPI 中接口的基本写法，并在 `main.py` 中新增了 `/ping` 接口
通过 `@app.get("/ping")` 可以把 URL 路径和 Python 函数绑定起来。当客户端访问 `/ping` 时，FastAPI 会执行对应函数，并返回 JSON 响应

### 本次接口调试结果：
```
GET http://127.0.0.1:8000/ping
```
返回
{
  "message": "pong"
}


## Day6 学习总结：FastAPI 路由与参数
日期：2026-07-11
今天学习了 FastAPI 的路由和接口参数，并使用 Apifox 调试接口

完成内容：
使用 `@app.get()` 创建多个 GET 接口
理解路由是 URL 路径与后端函数的对应关系
学习路径参数：`/hello/{name}`，例如访问 `/hello/Tom`
学习查询参数：`/items?limit=3`，用于向接口传递可选条件
在 Apifox 中配置本地前置 URL：`http://127.0.0.1:8000`
使用 Apifox 测试并保存接口请求

今日接口：
`GET /health`
`GET /ping`
`GET /hello/Tom`
`GET /items?limit=3`

今日收获：
我能创建多个 FastAPI 接口，并能区分路径参数和查询参数：路径参数属于 URL 路径的一部分，查询参数写在 `?` 后面


## 第一周学习总结
1. 本周完成了 Python 后端开发环境和 Git/GitHub 的基础配置，能够使用虚拟环境、VS Code 和终端完成简单项目的创建、运行与提交。
2. 在 FastAPI 方面，我完成了本地服务启动、接口文档访问，以及多个 GET 接口的编写和调试。现在能够使用 `@app.get()` 创建路由，并理解路径参数和查询参数的基本区别。
3. 在接口调试方面，我使用 Apifox 配置本地前置 URL，并测试了 `/health`、`/ping`、`/hello/Tom` 和 `/items?limit=3` 等接口。
4. 在 Git 方面，我掌握了 `status`、`add`、`commit`、`push`、`pull` 等常用命令，也处理过一次 README 合并冲突。
5. 算法方面，本周练习了数组和双指针相关题目，包括两数之和、移除元素、合并两个有序数组、有序数组的平方、移动零和删除有序数组中的重复项。