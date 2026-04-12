# 🌐 Multimodal Education Creator

### ✨ AI-powered Learning — Where Concepts Meet Visuals

Multimodal Education Creator is an **AI-powered educational content generator** that combines the power of **Large Language Models (LLMs)** and **AI image generation** to create rich, engaging, and visually intuitive learning material — all from a simple topic prompt.

Now enhanced with **Docker + CI/CD + Cloud Deployment (AWS EC2)** for real-world scalability 🚀

---

# 🚀 Live Demo

🌐 http://YOUR-EC2-IP:8501

---

# 🧠 Features

* 📘 **Structured Concept Explanation**
* 🎯 **Key Learning Points**
* 🖼️ **AI-Generated Visuals**
* ⚡ **Real-time Generation**
* 🌐 **Deployed on Cloud (AWS EC2)**
* 🔄 **Auto Deployment with CI/CD (GitHub Actions)**

---

# 🛠️ Tech Stack

| Layer               | Technology                             |
| ------------------- | -------------------------------------- |
| 🚀 AI Model         | Gemini API                             |
| 🎨 Image Generation | Hugging Face (FLUX / Stable Diffusion) |
| 🖥️ Frontend        | Streamlit                              |
| ⚙️ Backend          | Python                                 |
| 🐳 Containerization | Docker                                 |
| ☁️ Cloud            | AWS EC2                                |
| 🔄 CI/CD            | GitHub Actions                         |

---

# ⚙️ Project Architecture

User Input (Topic)
↓
Gemini API (Text Generation)
↓
Prompt Processing
↓
Hugging Face Image API
↓
Streamlit UI (Text + Image Output)

---

# 📦 Local Setup

## 1️⃣ Clone Repo

```
git clone https://github.com/nameisankit/education-app.git
cd education-app
```

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

## 3️⃣ Add Environment Variables

Create `.env` file:

```
GEMINI_API_KEY=your_key
HF_TOKEN=your_token
```

## 4️⃣ Run App

```
streamlit run app.py
```

---

# 🐳 Docker Setup

## Build Image

```
docker build -t education-app .
```

## Run Container

```
docker run -d -p 8501:8501 \
-e GEMINI_API_KEY=your_key \
-e HF_TOKEN=your_token \
education-app
```

---

# ☁️ Deployment (AWS EC2)

* Launch EC2 instance
* Open ports: 22, 8501
* Install Docker
* Run container

```
docker run -d -p 8501:8501 nameisankit07/education-app
```

---

# 🔄 CI/CD Pipeline

Automated deployment using **GitHub Actions**:

✔ Build Docker Image
✔ Push to DockerHub
✔ Deploy to EC2 via SSH
✔ Auto restart container

---

# 🔐 Environment Variables

| Variable        | Description            |
| --------------- | ---------------------- |
| GEMINI_API_KEY  | Gemini API key         |
| HF_TOKEN        | Hugging Face token     |
| DOCKER_USERNAME | DockerHub username     |
| DOCKER_PASSWORD | DockerHub access token |
| EC2_HOST        | EC2 public IP          |
| EC2_KEY         | SSH private key        |

---

# 🎯 Use Cases

✔ Self-study learning
✔ Teaching material generation
✔ AI-based education tools
✔ Concept visualization
✔ Quick topic understanding

---

# 💡 Why This Project

* Combines **text + visuals** → better learning
* Fully **automated deployment pipeline**
* Real-world **DevOps implementation**
* Scalable and production-ready

---

# 🧑‍💻 Author

**Ankit Parmar**
🚀 DevOps + AI Enthusiast

---

# ⭐ Future Improvements

* Add user authentication
* Store history (database)
* Add multiple model support
* UI enhancements

---

# 🔥 Final Note

This project demonstrates a **complete end-to-end AI + DevOps workflow**:

👉 Idea → Build → Dockerize → Deploy → Automate

---
