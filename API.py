import requests

API_KEY = "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"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://yourdomain.com",
    "X-Title":      "MyAppName",
}

# 验证 API Key
r = requests.get("https://openrouter.ai/api/v1/key", headers=HEADERS)
print(r.status_code, r.json())  # 应返回 200 和 key 信息，否则检查 Key 状态

# 调用 Chat Completion
body = {
    "model": "qwen/qwen3-235b-a22b:free",
    "messages": [{"role":"user","content":"测试一下"}]
}
r2 = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=HEADERS,
    json=body
)
print(r2.status_code, r2.json())
