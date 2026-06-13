#!/usr/bin/env python3
from __future__ import annotations

import json
import urllib.request


payload = {
    "model": "/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B",
    "messages": [
        {"role": "system", "content": "Return strict JSON only."},
        {"role": "user", "content": "Return {\"ok\": true, \"name\": \"ecoil\"}"},
    ],
    "max_tokens": 256,
    "temperature": 0,
    "extra_body": {
        "chat_template_kwargs": {"enable_thinking": False},
        "enable_thinking": False,
    },
}

request = urllib.request.Request(
    "http://127.0.0.1:8000/v1/chat/completions",
    data=json.dumps(payload).encode(),
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer EMPTY",
    },
)
with urllib.request.urlopen(request, timeout=120) as response:
    data = json.loads(response.read())
print(data["choices"][0]["message"]["content"])
