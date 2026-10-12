#!/usr/bin/env python3
"""Wrap fairway-fundraisers.html (artifact source) in a full HTML document as index.html for static hosting."""
import re
src = open("fairway-fundraisers.html", encoding="utf-8").read()
m = re.match(r"(.*?</style>\s*)(.*)", src, re.S)
head_bits, body = m.group(1), m.group(2)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Nonprofit golf tournaments in Lancaster and Chester counties, PA, October and November 2026.">
{head_bits.strip()}
<style>body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""
open("index.html", "w", encoding="utf-8").write(html)
print("wrote index.html", len(html), "bytes")
