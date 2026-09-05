import requests
import json
def ai(prompt,ask):
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "Bearer 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",
      "Content-Type": "application/json",
      "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
      "model": "google/gemma-3-27b-it:free",
      "messages": [{"role": "system","content":prompt+" і ніколи не веди себе і не згадуй що ти штучний інтелект"},
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": ask
            }
          ]
        }
      ]
    })
  )
  data=response.json()
  print(data)
  answer=data["choices"][0]["message"]["content"]
  print(answer)
  return answer