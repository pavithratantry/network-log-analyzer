📘 Network Log Analyzer (CLI + API + Web UI + AI)

The Network Log Analyzer is a full-stack project designed to parse router/switch logs, detect anomalies, and generate AI-powered recommendations.
It includes:

✔ Command-line tool (CLI)

✔ FastAPI backend

✔ JavaScript Web UI

✔ AI anomaly summarization using Groq

✔ Docker container support

✔ Expandable architecture for future additions (e.g., New Relic monitoring)

🚀 Features
🔍 1. Log Parsing

Supports syslogs from:

Cisco

Juniper

Arista

General router/switch logs

⚠️ 2. Anomaly Detection

Detects:

Interface flaps

OSPF neighbor changes

High CPU

Link state changes

Authentication failures

(Extensible via core/anomalies.py)

🤖 3. AI-Generated Summary

Uses Groq’s LLM:

Explains the problem

Recommends next actions

Summarizes all anomalies

🖥 4. Web UI

Simple frontend to:

Upload log files

View detected anomalies

Get AI recommendations

🧪 5. CLI Tool

Run via:

python -m cli.netwatch --file samples/cisco_sample.log

🐳 6. Docker Support

Build:

docker build -t netwatch .


Run:

docker run -p 8000:8000 --env-file .env netwatch

📦 Project Structure
network-log-analyzer/
│
├── cli/                 # CLI interface
│   └── netwatch.py
│
├── core/                # Core logic
│   ├── parser.py        # Log parsing
│   ├── anomalies.py     # Anomaly detection rules
│   └── llm.py           # Groq AI summarization
│
├── api/                 # FastAPI backend
│   └── server.py
│
├── web/                 # Web UI (HTML + JS)
│   ├── index.html
│   └── app.js
│
├── samples/             # Sample network logs
│   └── cisco_sample.log
│
├── Dockerfile
├── requirements.txt
└── README.md

🔧 Setup Instructions
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Create .env
GROQ_API_KEY=your_key_here

3️⃣ Run CLI
python -m cli.netwatch --file samples/cisco_sample.log

4️⃣ Run API
uvicorn api.server:app --reload --port 8000

5️⃣ Open Web UI

Open:

http://localhost:8000

🐳 Docker Usage
Build:
docker build -t netwatch .

Run:
docker run -p 8000:8000 --env-file .env netwatch

🧩 Future Enhancements

Add New Relic instrumentation for:

request latency

anomaly detection duration

LLM API cost

CPU/memory usage

(Screenshots will be added later.)

📄 License

MIT License

💬 Contact

Feel free to reach out or open issues/pull requests!
