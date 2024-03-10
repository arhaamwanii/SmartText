import streamlit as st
import streamlit.components.v1 as components
from auth0_component import login_button

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
    <style>
      body, html {{
        height: 100%;
        margin: 0;
      }}
      textarea {{
        height: 100%;
        width: 100%;
      }}
    </style>
    <script>
      document.addEventListener('DOMContentLoaded', function() {{

        tinymce.init({{
          selector: '#tinymce-editor',
          height: "500",
          plugins: 'ai',
          toolbar: 'aidialog aishortcuts',
          ai_request: (request, respondWith) => {{
            const openAiOptions = {{
              method: 'POST',
              headers: {{
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {openai_key}',
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
    <textarea id="tinymce-editor">Welcome! Ask me anything and let the AI magic begin...</textarea>
  </body>
  </html>
"""

from db_setup import MongoDBConnection

db_connection = MongoDBConnection()

db_connection.connect()

#example data
ai_prompt = "What is the future of AI?"
ai_response = "The future of AI is incredibly promising, with advancements leading to smarter technologies that will enhance our daily lives in numerous ways."

data_to_insert = {
    "prompt": ai_prompt,
    "response": ai_response
}

success = db_connection.insert_data("ai_prompts", data_to_insert)

if success:
    print("Successfully inserted AI prompt and response into MongoDB.")
else:
    print("Failed to insert data into MongoDB.")


def main():
    # Sidebar
    st.sidebar.title("Greetings, Explorer! 🌟")
    st.sidebar.write("""
    ## Embark on an AI Journey
    Welcome to an innovative space where your thoughts can unite with AI's potential. Your digital companion is ready to converse with you, craft stories, generate ideas, or even help with research. 📚✨

    **First Things First:**
    Please log in to unlock the full AI capabilities. Securely authenticate below and prepare to propel your creativity to new heights!
    """)

    # Login in Sidebar
    clientId = os.getenv("CLIENT_ID")
    domain = os.getenv("DOMAIN")
    user_info = login_button(clientId, domain=domain, container=st.sidebar)

    # Main Page Content
    if True:
        st.title("AI-Powered Creativity Awaits! 🎨")
        st.markdown("""
        ### Welcome Aboard!
        Dive into an interactive experience enhanced by the power of artificial intelligence. Here’s how you can make the most out of this AI editor:

        - **Ask Questions:** From trivial to complex ones, don't hesitate to seek answers.
        - **Craft Stories:** Unleash your inner storyteller and let the AI embellish your narratives.
        - **Generate Ideas:** Stuck in a creative rut? Seek AI's assistance for fresh perspectives.
        - **Research Assistance:** Whether you're writing an essay or exploring new topics, AI is here to help.

        Enjoy exploring endless possibilities where each inquiry opens a new path to discovery. Let's venture into the future, one question at a time! 🚀💡
        """)

        # Display the TinyMCE editor
        components.html(tinymce_ai_html, height=900, width=1000, scrolling=True)
    else:
        st.error("🔒 Please log in to access the AI editor.")

if __name__ == "__main__":
    main()
