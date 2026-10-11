# David 的自媒体封面与配图合集

给自己使用的图片项目合集：9 个上游项目、186 张官方样片/版式/界面参考，以及一个可独立安装的 `media-visual-hub` 统一入口。按用途看图选风格，交给 GPT 制作，满意成品再归档复用。

**快速开始：** 克隆本仓库，打开 [样片库](skills/media-visual-hub/assets/gallery.html)（本地双击此文件；GitHub 文件页面不会执行交互界面）。先选用途，再收藏或选择样片。联网才能加载远程图片。

```bash
git clone https://github.com/David-code-tang/david-media-visual-skills.git
cd david-media-visual-skills
```

私有仓库需要有读取权限的 GitHub 登录。

## 在 Codex 中调用

在克隆后的仓库目录打开 Codex 新对话，可通过项目的 `.agents/skills` 入口发现本 Skill；要在其他项目使用，再按下面方式安装。

将本仓库链接交给 Codex：

> 请安装这个仓库里的 skills/media-visual-hub：https://github.com/David-code-tang/david-media-visual-skills

也可以将 `skills/media-visual-hub` 整个目录复制到自己的 skills 目录。它包含完整样片索引和选样页，不依赖这台电脑的绝对路径。安装完成后在新对话使用：

> $media-visual-hub 这篇文章需要一张封面，从我的样片库里挑 3 个方向，展示样片让我选。

> $media-visual-hub 按 4-C03 做一张 16:9 封面，标题是「一个人怎么做好自媒体」，使用当前可用的 GPT 生图能力。

> $media-visual-hub 按 7-I09 的白底手绘感觉，把这一段内容做成解释图。

未安装时，也可以让助手直接读取 [SKILL.md](skills/media-visual-hub/SKILL.md) 执行。实际生图需要宿主提供图片生成工具；单独运行目录脚本不会调用生图 API。

## 从命令行查样片与整理提示词

Python 3，无第三方依赖，可从任意工作目录调用：

```bash
python3 skills/media-visual-hub/scripts/catalog.py list --use cover
python3 skills/media-visual-hub/scripts/catalog.py list --query 手绘
python3 skills/media-visual-hub/scripts/catalog.py show 4-C03
python3 skills/media-visual-hub/scripts/catalog.py projects
python3 skills/media-visual-hub/scripts/catalog.py brief --style 4-C03 --content-file article.txt --ratio 16:9 --platform 公众号 --text "一个人怎么做好自媒体" > brief.txt
```

生成要求与真实参考图一起交给 GPT。新对话无法仅凭编号知道画风，需要安装本 Skill 或提供参考图和来源。

## 上游项目

代码使用 Git 子模块保留在 `upstream/`，每个项目固定到收录时的 commit，来源、许可证标识和 Skill 路径见 [项目索引](catalog/projects.json)。普通克隆只下载合集；有需要时再取原项目。

| 原文编号 | 项目 | 主要用途 |
| --- | --- | --- |
| 1 | [Self Media Skills](https://github.com/yanhua1010/self-media-content-workflow) | 文章配图工作流 |
| 2 | [Creator Buddy](https://github.com/SpaceZephyr/creator-buddy) | 封面、组图、图表与逻辑图 |
| 4 | [baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 封面、配图、信息图、漫画、组图 |
| 5 | [Guizang Social Card Skill](https://github.com/op7418/guizang-social-card-skill) | 图文卡片、封面排版 |
| 6 | [Punk Skill](https://github.com/adrianpunk/Punk-Skill) | 封面、真人 IP、头像 |
| 7 | [小黑配图](https://github.com/helloianneo/ian-xiaohei-illustrations) | 白底手绘解释图 |
| 8 | [Write Then Publish](https://github.com/fxyadela/write-then-publish) | 已有内容排版应用；当前索引未发现 SKILL.md |
| 14 | [xiaohongshu-ops](https://github.com/Xiangyu-CAS/xiaohongshu-ops-skill) | 小红书封面 |
| 15 | [WeWrite](https://github.com/imraywang/wewrite) | 文章封面、插图和排版 |

例如只获取 Punk：

```bash
git submodule update --init upstream/Punk-Skill
```

获取全部原项目：

```bash
git submodule update --init --recursive
```

原项目未自动安装，也未自动配置 API 或运行安装脚本。原项目完整用法以各自 README 与具体 SKILL.md 为准，部分能力需要额外 API、CLI 或渲染工具；制作图片不包含自动发布。

## 怎么管理风格

- 全部样片：按用途查，保留稳定编号与来源。
- 我的收藏：先挑 6—10 个自己喜欢的；收藏编号可在界面备份/恢复。
- 我的成品：实际 GPT 生成后，记录参考编号、提示词、尺寸、模型信息（可获取时）与满意程度。只有自己确认满意的成品才作为标准样片。

对话内收藏和本地独立页面的收藏不保证同步。浏览器数据清理后可用编号恢复；个人文章和偏好默认不进入 Git。

186 张参考不是 186 种独立风格，其中包含同一风格不同题材、版式和应用界面。没有对应公开样片的目录单独列出；官方示例与本地 GPT 试作分开。字体密集或严格排版场景可能需要后续排版，GPT 效果需实测。

样片链接已固定到收录版本，避免跟随 main 改动；它们依旧依赖原仓库与 CDN 可用性。本仓库没有重新托管第三方图片。

## 版本与许可

收录时间：2026-10-11。这里是聚合索引与独立统一入口，各原项目、图片、字体与品牌素材保持原权利与许可，详见 [第三方来源](THIRD_PARTY.md)。不提供覆盖所有上游项目的统一开源授权。
