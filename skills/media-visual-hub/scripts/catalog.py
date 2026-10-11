#!/usr/bin/env python3
"""Query a portable image reference library; does not call image or publishing APIs."""
import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def category(style_id):
    prefixes = {'cover': ('4-C', '6-C'), 'article': ('4-I', '7-I'),
                'carousel': ('4-X',), 'info': ('4-F',), 'comic': ('4-M',),
                'avatar': ('6-A',), 'slides': ('4-S',)}
    return next((key for key, values in prefixes.items() if style_id.startswith(values)), 'layout')

def samples():
    catalog = json.loads((BASE / 'references/samples.json').read_text(encoding='utf-8'))
    return [dict(item, use=category(item['id']), group=group['title'], source=group['source'])
            for groups in catalog.values() for group in groups for item in group.get('items', [])]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    listing = sub.add_parser('list')
    listing.add_argument('--use', choices=['all', 'cover', 'article', 'carousel', 'info', 'comic', 'avatar', 'slides', 'layout'], default='all')
    listing.add_argument('--query', default='')
    show = sub.add_parser('show'); show.add_argument('style')
    sub.add_parser('projects')
    brief = sub.add_parser('brief')
    brief.add_argument('--style', required=True)
    brief.add_argument('--content-file', type=Path, required=True)
    brief.add_argument('--ratio', default='请结合发布位置确认')
    brief.add_argument('--platform', default='待确认')
    brief.add_argument('--text', default='待确认；不要沿用参考图文字')
    args = parser.parse_args()
    if args.command == 'projects':
        print((BASE / 'references/projects.json').read_text(encoding='utf-8')); return
    entries = samples()
    if args.command == 'list':
        for entry in entries:
            if (args.use == 'all' or entry['use'] == args.use) and args.query.casefold() in (entry['id'] + entry['name'] + entry['group']).casefold():
                print(f"{entry['id']}\t{entry['name']}\t{entry['use']}\t{entry['original']}")
        return
    entry = next((item for item in entries if item['id'] == args.style), None)
    if entry is None: parser.error(f'没有样片编号 {args.style}，请用 list 查询')
    if args.command == 'show':
        print(json.dumps(entry, ensure_ascii=False, indent=2)); return
    try: content = args.content_file.read_text(encoding='utf-8').strip()
    except (OSError, UnicodeError) as exc: parser.error(str(exc))
    if not content: parser.error('内容文件不能为空')
    print(f'''请使用当前可用的 GPT 图片生成工具制作图片。
参考：{entry['id']} · {entry['name']}
样片：{entry['original']}
来源：{entry['source']}
用途：{entry['use']}（参考目录：{entry['group']}）
发布位置：{args.platform}
比例：{args.ratio}
图上文字：{args.text}
内容：
{content}

先实际查看样片，提取配色、构图、质感、留白和字体层级，再用于本次内容。
若无法查看链接且没有收到样片，请先索取图片，不要凭名称猜测。
不要沿用参考图的无关文案、商标、水印或数据；解释图需保持逻辑准确。
主题、比例或文案缺失且会影响成图时先补齐。没有图片生成工具时说明限制并给出提示词。
这是对参考视觉语言的重新设计，不代表运行了原项目或已经复现官方效果。
保留参考编号、实际提示词与实际生成参数，供后续归档。''')

if __name__ == '__main__': main()
