当然可以！下面是你这个 PowerPoint 自动生成项目的完整 `README.md` 文档草稿，内容包含：

* ✅ 项目简介与功能亮点
* ✅ 使用说明（依赖项、文件结构、运行方法）
* ✅ 样式与内容模板的编写指南
* ✅ 高级功能（动态字体、自定义背景图、插图占位）
* ✅ 支持的提示词模板

---

# Auto-PPT


---

## 项目结构

```
auto-ppt/
├── main.py                        # 主程序入口
├── output/                        # 输出生成的 PPT 文件   
├── slides/                        # 内容结构 JSON 文件
│   └── 示例：项目介绍.json
├── styles/                        # 样式模板 JSON 文件
│   └── 示例：tech_dark.json
├── assets/
│   └── backgrounds/               # 背景图像文件（用于 image/mixed 背景）
├── tools/                         # 工具模块
│   ├── font_utils.py             # 字体与动态字号设置
│   ├── slide_types.py            # 各种幻灯片类型的生成函数
│   ├── insert_placeholder.py     # 插图留白处理
│   ├── background_utils.py       # 背景设置工具（支持图层置底）
```

---

## 使用说明

### 1. 安装依赖

```
pip install python-pptx
```

### 2. 准备内容文件和样式模板

#### 内容结构（`slides/*.json`）

```json
{
  "slides": [
    {
      "type": "title",
      "title": "我的PPT标题",
      "subtitle": "副标题"
    },
    {
      "type": "section",
      "title": "第一部分"
    },
    {
      "type": "content",
      "title": "技术原理",
      "bullets": [
        "系统设计思路",
        "【插图】整体架构图"
      ]
    },
    {
      "type": "closing",
      "title": "感谢聆听",
      "subtitle": "欢迎提问"
    }
  ]
}
```

#### 样式模板（`styles/*.json`）

支持如下结构（每类页面的标题/副标题/bullet 分别定义）：

```json
{
  "style": {
    "title": {
      "title_text": {...},
      "subtitle_text": {...}
    },
    "content": {
      "title_text": {...},
      "bullet_text": {...}
    },
    "closing": {
      "title_text": {...},
      "subtitle_text": {...}
    },
    "background": {
      "title": {
        "type": "image",
        "image": "assets/backgrounds/tech_dark.png"
      }
    }
  }
}
```

### 3. 运行程序

程序将自动生成如下输出路径：

```
output/项目介绍_tech_dark.pptx
```

---


## 🎨 提示词模板
```
/prompt_template/ 内容可以使用
```


