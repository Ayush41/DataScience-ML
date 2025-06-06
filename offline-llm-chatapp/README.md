# TRY NOT TO RUN THIS CODE AS IT IS IN DEVELOPMENT PERIOD

# Features
* Chat functionality using an online LLM
* Offline mode: allows users to chat with the model without an internet connection

# Technical Details
| Feature | Description |
| --- | --- |
| Node.js 14.x | Used for offline training of the LLM |
| TensorFlow.js 3.13.0 | Used for offline training of the LLM |
| JavaScript, HTML5, CSS3 | Used to create the chat interface and generate text |

# How it Works
1. User interacts with the chat interface and inputs text or prompts to be generated by the model.
2. The user's input is sent to an online server (localhost:8080) where it is processed using the trained LLM.
3. The LLM returns a response, which is then displayed to the user in real-time.

<!-- # Code Structure
```markdown
public/
index.html
styles.css
node_modules/
tensorflow.js/
express/
package.json

src/
main.js
chatInterface.js
generateText.js -->
