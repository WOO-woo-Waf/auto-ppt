
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
pip install -r requirements.txt
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
        // 以【插图】开头的内容会在图片目录中匹配并插入对应图片
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

使用命令行参数指定模板、样式、输出目录以及图片目录，例如：

```bash
python main.py --template slides/example.json \
               --style styles/style1.json \
               --output_dir output \
               --image_dir images
```

生成的文件将保存在 `output` 目录下，文件名由模板和样式名称组合而成。

---


## 🎨 提示词模板

在 bullet 文本中可以加入下列标签以实现更多效果：

- `【插图】关键词` 或 `【插图:关键词】描述`：在 `--image_dir` 指定的目录中匹配并插入对应图片。
- `【颜色:#FF0000】文本` 或 `【红色】文本`：将该 bullet 显示为指定颜色。
- `【重点】文本` 或 `【强调】文本`：使文本加粗以突出重点。
- 标签可以组合使用，例如 `【颜色:#ff0000】【重点】【插图】示意图`。



