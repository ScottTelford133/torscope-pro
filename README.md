# TorScope Pro 🛡️
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Advanced Tor Hidden Service Research & Monitoring Suite**

🔍 Scrape | 🌐 Verify | 📊 Track | 🧠 AI-Analyze | 📱 Mobile

This tool helps researchers **ethically discover and monitor `.onion` links** found on the clearnet (e.g., GitHub, Reddit, Hidden Wiki). It does **not access** the dark web directly.

## 🚀 Features
- Scrape `.onion` links from public sites
- Verify reachability over Tor
- AI-powered summaries (via Ollama)
- Uptime tracking & alerts
- Web & mobile dashboards
- Plugin system
- Ethical use by design

## 🛠️ How to Run

```bash
git clone https://github.com/yourusername/torscope-pro.git
cd torscope-pro
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
pip install -r requirements.txt
python main.py