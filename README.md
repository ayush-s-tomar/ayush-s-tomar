<div align="center">

![Ayush Singh Tomar — AI Engineer](doc/banner.svg)

### AI Agent & RAG Developer — LangGraph · FastAPI · Live Deployed

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=650&lines=Building+real+AI+systems%2C+not+wrappers.;Multi-agent+orchestration+%7C+RAG+with+citations;LangGraph+%7C+FastAPI+%7C+Groq+%7C+MCP;Open+to+full-time+AI+Developer+roles." alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ayushsinghtomar)
[![Dev.to](https://img.shields.io/badge/Dev.to-Blog-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/ayushsinghtomar)
[![Upwork](https://img.shields.io/badge/Upwork-Hire_Me-6FDA44?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/ayushtomar)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ayushsinghtomar22@gmail.com)

<br/>

<table>
<tr>
<td align="center"><b>9+</b><br/><sub>Deployed AI systems</sub></td>
<td align="center"><b>1</b><br/><sub>Model published on Hugging Face</sub></td>
<td align="center"><b>5.0★</b><br/><sub>Freelance client rating</sub></td>
<td align="center"><b>Top 5%</b><br/><sub>NPTEL, IIT Kanpur</sub></td>
</tr>
</table>

</div>

---

## 👨‍💻 About Me

Final-year B.Tech IT student building AI systems that **ship** — not tutorials, not localhost demos. Five live, deployed projects prove five distinct capabilities: multi-agent orchestration, RAG with real citations and eval harnesses, model fine-tuning, protocol-compliant tool serving (MCP), and voice AI.

- 🎓 B.Tech IT, MITS Gwalior (Final Year, 2023–2027) · CGPA 7.87
- 🔭 Specializing in multi-agent systems, RAG pipelines & LLM infrastructure
- 🚀 Everything below is deployed — architecture, backend, frontend, and CI, live on Render / Vercel / Streamlit
- 🏆 NPTEL (IIT Kanpur) — Elite, Top 5%, Cloud Computing & Distributed Systems (90%)
- 💼 Freelance AI Developer on Upwork (5.0/5.0 client rating) · Open to full-time AI Developer roles

---

## 🏆 Top 5 Projects

<table>
<tr>
<td width="70%">

### 1. [SalesAgent](https://github.com/ayush-s-tomar/salesagent) — Autonomous B2B Sales Agent
[Live Demo](https://salesagent-ai.streamlit.app/) · [Writeup](https://dev.to/ayushsinghtomar/i-got-tired-of-writing-cold-emails-so-i-built-an-ai-agent-to-do-it-for-me-2m4h)

Paste a LinkedIn URL — a LangGraph research node pulls real signal, a Random Forest model scores the lead (84/100), and Groq drafts a hyper-personalized cold email referencing actual company events. End to end in under 45 seconds. A self-built eval harness caught two production bugs before they shipped — uniform lead scores and a missing sender identity in generated emails.

`LangGraph` `FastAPI` `React` `scikit-learn` `Groq` `Tavily`

</td>
<td width="30%"><b>9.3 / 10</b><br/><sub>Full agentic loop + ML scoring + a real eval harness that caught real bugs — the most complete system here.</sub></td>
</tr>
<tr>
<td>

### 2. [AgentLoop](https://github.com/ayush-s-tomar/agentloop) — Multi-Step Research Agent
[Live Demo](https://agentloop.streamlit.app/)

Not a chatbot — a research agent that decomposes a question into sub-questions, searches the live web, reflects on gaps in its own notes, loops back, and delivers a fully cited report. Two-tier memory (short-term run state + long-term SQLite recall) streams live trace events to the UI as it reasons.

`FastAPI` `LangGraph` `Groq` `SQLite` `Tavily`

</td>
<td><b>9.0 / 10</b><br/><sub>Genuine plan → act → reflect → loop architecture with visible reasoning traces — rare at this stage.</sub></td>
</tr>
<tr>
<td>

### 3. [AskMyDocs](https://github.com/ayush-s-tomar/intellect-docs-ai) — RAG Document Q&A
[Live Demo](https://intellect-docs-ai.vercel.app/)

Answers questions over 50-page PDFs in under 3 seconds, returning the exact source chunk and cosine similarity score behind every answer — and withholds an answer instead of hallucinating when the document doesn't cover it. Ships with an LLM-as-judge + keyword-validation eval pipeline wired into CI to catch retrieval regressions before deploy.

`Next.js` `Supabase (pgvector)` `Cohere` `Groq`

</td>
<td><b>8.8 / 10</b><br/><sub>Grounded citations plus CI-gated eval is the detail that separates this from a weekend RAG demo.</sub></td>
</tr>
<tr>
<td>

### 4. [LoRA Fine-Tuned Resume Screener](https://github.com/ayush-s-tomar/resume-screener-lora) — Published on Hugging Face
[Try it](https://resume-screener-lora.streamlit.app/) · [Hugging Face](https://huggingface.co/Kus-hal/resume-screener-lora)

Fine-tuned a LoRA adapter (r=16, just 0.44% of parameters trained) on Qwen2.5-0.5B so structured JSON resume-fit verdicts are the model's default output — not something coaxed out with prompting. Validation loss tracked training loss across 3 epochs with no divergence, confirming no overfitting. Published for reproducible, framework-agnostic inference.

`Qwen2.5-0.5B` `LoRA (PEFT)` `PyTorch` `Hugging Face Transformers`

</td>
<td><b>8.7 / 10</b><br/><sub>The only project here that touches training, not just inference — and it's published, reproducible work.</sub></td>
</tr>
<tr>
<td>

### 5. [Portfolio MCP Server](https://github.com/ayush-s-tomar/portfolio-mcp-server) — Protocol-Compliant Tool Server
Local only (Claude Desktop)

A working MCP server exposing 5 tools — project search, stack filtering, resume summary — so any MCP client queries this portfolio as live, structured, callable data instead of a static page. Implements real client-side permission gating and tool-call routing: a protocol-compliant server, not a wrapper around an API.

`Python` `MCP (FastMCP SDK)` `stdio transport` `Claude Desktop`

</td>
<td><b>8.5 / 10</b><br/><sub>Niche by design, but it's real protocol work — most portfolios don't have anything like it.</sub></td>
</tr>
</table>

---

<details>
<summary><b>▶ More projects</b> (voice AI, automation agents, additional RAG systems & more)</summary>
<br>

**[LLM Cost Router](https://github.com/ayush-s-tomar/llm-cost-router)** — [Live Demo](https://llm-cost-router.streamlit.app/)
Heuristic query-complexity classifier that routes requests between a cheap and a far more expensive Groq model, cutting cost significantly on simple queries with no quality loss on complex ones. Live dashboard tracks real spend vs. a same-model baseline.
`FastAPI` `Groq (Llama 3.1 8B / 3.3 70B)` `Streamlit`

**[Self-Healing RAG](https://github.com/ayush-s-tomar/self-healing-rag)** — [Live Demo](https://rag-critic-loop.streamlit.app/)
RAG pipeline that critiques its own answers — if a response isn't grounded in the retrieved documents, it reformulates the query and retries instead of hallucinating.
`LangGraph` `Chroma` `Groq` `Streamlit`

**[AI Interview Coach](https://github.com/ayush-s-tomar/ai-interview-coach)** — [Live Demo](https://mockinterview-ai.streamlit.app/)
Real-time voice interview simulator — answers scored on relevance, clarity, technical accuracy, and confidence via Groq LLaMA 3.3, with a downloadable PDF report.
`Streamlit` `Faster-Whisper` `Groq` `PDF Generation`

**[Agentic RAG Research Assistant](https://github.com/ayush-s-tomar/agentic-rag-research-assistant)** — [Live Demo](https://agentic-rag-groq.streamlit.app/) | [API Docs](https://agentic-rag-research-assistant-jjch.onrender.com/docs)
LangGraph tool-routing RAG system — retrieves grounded answers from uploaded PDFs via Chroma, refuses out-of-scope questions instead of guessing, and routes queries between a cheap and large model based on complexity.
`LangGraph` `FastAPI` `Streamlit` `Chroma` `Groq`

**[AI Data Analyst Agent](https://github.com/ayush-s-tomar/ai-data-analyst)** — [Live Demo](https://askthedata-ai.streamlit.app/)
Upload CSV, Excel, PDF, Parquet, XML, SQLite, ODS, or Feather files — ask questions in plain English, get instant charts and insights.
`Streamlit` `Groq` `pandas`

**[Email Agent](https://github.com/ayush-s-tomar/Email-agent)** — [Live Demo](https://ai-inbox-agent.streamlit.app/)
AI Gmail agent that classifies emails and drafts context-aware replies you can approve or edit before sending.
`IMAP` `SMTP` `Groq` `LLaMA 3.3` `Streamlit`

**[ARIA – Voice AI Assistant](https://github.com/ayush-s-tomar/aria-voice-assistant)** — [Live Demo](https://aria-bot.streamlit.app/)
Speech-to-speech AI assistant with 99-language support and conversation memory. Speak in any language — ARIA transcribes, thinks, and talks back.
`FastAPI` `Faster-Whisper` `Groq` `LLaMA` `gTTS`

**[ResumeIQ](https://github.com/ayush-s-tomar/ResumeIQ)** — [Live Demo](https://resume-iq-screener.streamlit.app/)
AI resume screener that scores ATS compatibility, identifies gaps, and exports detailed PDF reports.
`Python` `Flask` `Groq`

**[North Star Support Chatbot](https://github.com/ayush-s-tomar/northstar-chatbot)** — Local only
AI-powered customer support chatbot for a North Star outdoor gear store, with full conversation handling and escalation logic.
`React` `FastAPI` `Groq` `LLaMA`

</details>

<details>
<summary><b>▶ In progress / archived</b></summary>
<br>

**[StartupScope](https://github.com/ayush-s-tomar/startupscope)** — 🚧 *Demo temporarily offline, redeploying*
Multi-agent CrewAI crew — Researcher, Analyst, and Writer agents collaborate to search the web and generate structured startup intelligence reports.
`CrewAI` `Groq` `Streamlit`

**[JobHunt](https://github.com/ayush-s-tomar/jobhunt)** — 🚧 *Demo temporarily offline, redeploying*
AI-powered Telegram job aggregator — scores every post and auto-applies via email or form-fill. Watches job channels 24/7 so you don't have to.
`FastAPI` `PostgreSQL` `Groq`

**[n8n Email → Slack](https://github.com/ayush-s-tomar/n8n-email-slack)** — *Archived, hosting suspended*
No-code AI automation pipeline: fetches unread Gmail → summarizes with Groq LLaMA → detects priority → pushes digest to Slack.
`n8n` `Groq` `Gmail` `Slack`

</details>

---

## 💼 Experience & Achievements

**Freelance AI Developer** — Self-Employed, Remote · *May 2026 – Present*
Design and ship deployed AI systems end-to-end for clients — agentic workflows, RAG pipelines, LLM tooling.

**AI Chatbot Developer — Upwork Talent Accelerator** · *Jun 2026*
Delivered a chatbot contract end-to-end in 3 days. Client rated **5.0/5.0**.

**Cloud Computing and Distributed Systems** — NPTEL (IIT Kanpur)
Elite + Top 5% Topper, 90% (Jan–Mar 2026).

---

## 🛠 Stack

**Core — used across most projects**
`Python` `LangGraph` `FastAPI` `Groq` `LLaMA 3.3` `Streamlit` `Git`

**AI / LLM**
`LangChain` `CrewAI` `MCP` `LoRA/PEFT` `PyTorch` `Hugging Face Transformers` `Whisper` `Prompt Engineering` `scikit-learn`

**Frontend & Data**
`React` `Next.js` `JavaScript/TypeScript` `SQL` `Supabase (pgvector)` `PostgreSQL` `Chroma` `pandas`

**Infra & Deployment**
`Docker` `Vercel` `Render` `Flask`

---

## 📊 GitHub Stats

<div align="center">

![Ayush's GitHub Stats](https://github-readme-stats.vercel.app/api?username=ayush-s-tomar&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=6366f1&icon_color=6366f1&text_color=ffffff&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=ayush-s-tomar&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=6366f1&text_color=ffffff)

![GitHub Streak](https://streak-stats.demolab.com/?user=ayush-s-tomar&theme=tokyonight&hide_border=true&background=0D1117)

</div>

---

## 🐍 Contribution Snake

<div align="center">

![Snake animation](https://raw.githubusercontent.com/ayush-s-tomar/ayush-s-tomar/output/github-snake-dark.svg)

</div>

---

## 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
- [My LLM App Was Charging Rent-Controlled Tenants Penthouse Prices — So I Built a Router to Fix It](https://dev.to/ayushsinghtomar/my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it-38cl)
- [Two Bugs That Almost Shipped in My Agentic RAG Assistant](https://dev.to/ayushsinghtomar/two-bugs-that-almost-shipped-in-my-agentic-rag-assistant-2fm0)
- [I Got Tired of My Portfolio Looking Like a List of Links. So I Built an MCP Server for It.](https://dev.to/ayushsinghtomar/i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it-440o)
- [I Got Tired of Writing Cold Emails. So I Built an AI Agent to Do It for Me.](https://dev.to/ayushsinghtomar/i-got-tired-of-writing-cold-emails-so-i-built-an-ai-agent-to-do-it-for-me-2m4h)
<!-- BLOG-POST-LIST:END -->

---

<div align="center">

### 📬 Let's Build Something

Have a problem worth an agent, a RAG pipeline, or an LLM integration? Reach out on [LinkedIn](https://linkedin.com/in/ayushsinghtomar), read the build logs on [Dev.to](https://dev.to/ayushsinghtomar), or [start a contract on Upwork](https://www.upwork.com/freelancers/ayushtomar).

</div>
