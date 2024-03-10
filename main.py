import streamlit as st
import streamlit.components.v1 as components

# get env variables
import os
from dotenv import load_dotenv

load_dotenv()

tinymce_key = os.getenv("tiny")
openai_key = os.getenv("openai")

tinymce_ai_html = f"""
  <!DOCTYPE html>
  <html>
  <head>
    <script src="https://cdn.tiny.cloud/1/{tinymce_key}/tinymce/6/tinymce.min.js" referrerpolicy="origin"></script>
    <script>
      document.addEventListener('DOMContentLoaded', function() {{

        tinymce.init({{
          selector: '#tinymce-editor',
          plugins: 'ai',
          toolbar: 'aidialog aishortcuts',
          ai_request: (request, respondWith) => {{
            const openAiOptions = {{
              method: 'POST',
              headers: {{
                'Content-Type': 'application/json',
                'api-key': '{openai_key}',
              }},
              body: JSON.stringify({{
  messages: [{{
  role: 'user',
  content: request.prompt
  }}],
  "temperature": 0.7,
  "top_p": 0.95,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "max_tokens": 800,
  "stop": null
}})
            }};
            respondWith.string((signal) => window.fetch('https://north-chill-lol.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview', {{ signal, ...openAiOptions }})
              .then(async (response) => {{
                if (response) {{
                  const data = await response.json();
                  if (data.error) {{
                    throw new Error(`${{data.error.type}}: ${{data.error.message}}`);
                  }} else if (response.ok) {{
                    return data?.choices[0]?.message?.content?.trim();
                  }}
                }} else {{
                  throw new Error('Failed to communicate with the ChatGPT API');
                }}
              }})
            );
          }}
        }});
      }});
    </script>
  </head>
  <body>
    <textarea id="tinymce-editor">Welcome! Ask me something...</textarea>
  </body>
  </html>
"""


def main():
    st.title("Streamlit with TinyMCE AI Assistant")

    # Use the `components.html` method to embed the TinyMCE with AI Assistant feature
    components.html(tinymce_ai_html, height=500, scrolling=True)


if __name__ == "__main__":
    main()
