
# 🤖 **BuddyBot 🛠️** – Your Interactive Chat Companion

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-orange.svg)
![Ollama](https://img.shields.io/badge/Powered_by-Ollama-brightgreen.svg)

Welcome to **BuddyBot 🛠️**, an advanced, customizable chatbot designed to deliver engaging, real-time answers to all your questions. This project is powered by Streamlit for an interactive web UI and supports multiple language models, all running locally via Ollama for maximum flexibility and privacy. 

---

## 🚀 **Features**

- **Multi-Model Support**: Seamlessly switch between different language models, such as `Llama 3.2`, `GPT-Neo`, and others supported by Ollama.
- **Run Locally with Ollama**: No need for cloud infrastructure; ChatMate AI leverages the Ollama engine to run models locally, ensuring privacy and saving on server costs.
- **Dynamic Interaction**: Input user messages in real-time and receive responses instantly, complete with avatars and message streaming for a natural conversation flow.
- **Customizable UI**: The chatbot interface is crafted with Streamlit, allowing for a clean, modern design with avatar icons, color-coded messages, and an interactive sidebar for setting preferences.
- **User-Friendly Sidebar**: Easily enter your name, set your preferred model, and see personalized greetings with animated effects.
- **Persistent Conversations**: Maintains chat history, making it easy to refer back to previous exchanges within the same session.
- **Gradients & Animations**: Enjoy a visually pleasing experience with gradient backgrounds, animations, and smooth transitions.
  
---

## 🛠️ **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sriramkrish68/BuddyBot 🛠️.git
   cd ChatMate-AI
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Ollama Engine**
   - Download and install [Ollama](https://ollama.com/download) on your system.
   - Ensure models like `Llama 3.2` etc are accessible through Ollama by downloading them if necessary.

4. **Run the Chatbot**
   ```bash
   streamlit run mychatbot.py
   ```

5. **Access ChatMate AI**
   Open your browser and go to `http://localhost:8501` to start chatting!

---

## 💻 **Usage**

1. **Choose Your Model**: Use the sidebar dropdown to select the language model you want to interact with (e.g., `Llama 3.2`).
2. **Enter Your Name**: Personalize the experience by entering your name; ChatMate AI will greet you with a friendly message!
3. **Start Chatting**: Type your questions in the chat input, and watch the bot respond in real time.
4. **Switch Models Anytime**: Experiment with different models on the fly to get various perspectives and response styles.

---

## 📂 **Project Structure**

```plaintext
├── mychatbot.py               # Main Streamlit app code
├── requirements.txt            # Required dependencies
├── README.md                   # Project documentation
```

---

## 📝 **Key Notes**

- **Privacy-First Design**: Running models locally ensures that your data never leaves your machine, offering better privacy and security.
- **Real-Time Token Streaming**: Using Streamlit and Ollama's streaming API, messages are delivered token-by-token, providing a seamless and interactive conversation experience.
- **Flexible Model Switching**: Easily experiment with different models directly within the app to tailor responses to your needs.
- **Easy Setup**: With Ollama's local engine and Streamlit’s lightweight web UI, setup and deployment are hassle-free and don’t require heavy cloud infrastructure.

---

## 💡 **Advantages**

- **Cost Efficiency**: No cloud or API costs involved. Models run locally on your machine, saving on both money and bandwidth.
- **Enhanced Personalization**: Dynamic sidebar allows users to enter names and choose models, creating a tailored experience.
- **Visual Appeal**: Modern gradients, animations, and user avatars make the chatbot feel engaging and intuitive.
- **Complete Privacy**: All data processing happens locally, meaning no data is shared with external servers.
- **Streamlit Integration**: Streamlit allows for quick UI adjustments, making it easy to modify or expand features.

---

## 🌌 **Future Enhancements**

- **Voice Interaction**: Adding speech-to-text and text-to-speech for an even more interactive experience.
- **Session Persistence**: Allow users to save and reload conversations across sessions.
- **More Customization Options**: Enable custom themes, color schemes, and even customizable avatars.
- **Extended Model Library**: Incorporate more language models and support for model fine-tuning.
  
---

## 🤝 **Contributing**

Contributions are welcome! If you have ideas to make ChatMate AI even better, feel free to fork this repo, make changes, and submit a pull request.


---

### 🌈 **Thank You for Checking Out BuddyBot 🛠️!**

Enjoy exploring the world of language models with an intuitive, interactive chatbot at your fingertips! 😄

--- 
