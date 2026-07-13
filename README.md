<div align="center">

![Ayush Singh Tomar — AI Engineer](doc/banner.svg)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Building+real+AI+tools%2C+not+wrappers.;Multi-agent+systems+%7C+RAG+pipelines;LLMs+%7C+FastAPI+%7C+LangGraph+%7C+Groq;Open+to+freelance+%26+full-time+roles." alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ayushsinghtomar)
[![Dev.to](https://img.shields.io/badge/Dev.to-Blog-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/ayushsinghtomar)
[![Upwork](https://img.shields.io/badge/Upwork-Hire_Me-6FDA44?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/ayushtomar)

</div>

---

## 👨‍💻 About Me

Final-year B.Tech IT student at MITS Gwalior, building deployed AI systems that go beyond API wrappers — multi-agent pipelines, RAG systems, a protocol-compliant MCP server, and a LoRA fine-tuned model published on Hugging Face.

- 🎓 B.Tech IT, MITS Gwalior (Final Year) · CGPA 7.87
- 🔭 Specialising in multi-agent systems, RAG pipelines & LLM infrastructure
- 🤖 10 self-shipped, deployed AI projects — each solving a real problem
- 🏆 NPTEL (IIT Kanpur) Elite + Top 5%, Cloud Computing & Distributed Systems
- 💼 Open to AI Developer roles & freelance contracts

---

## 🤖 Projects

> ★ Start here: **SalesAgent · Portfolio MCP Server · LLM Cost Router · AgentLoop**

**[SalesAgent](https://github.com/ayush-s-tomar/salesagent)** — [Live Demo](https://salesagent-theta.vercel.app) | [📝 Writeup](https://dev.to/ayushsinghtomar/i-got-tired-of-writing-cold-emails-so-i-built-an-ai-agent-to-do-it-for-me-2m4h)
Autonomous B2B sales agent. Paste a LinkedIn URL — it researches the lead, scores them with ML (84/100), and drafts a hyper-personalized cold email referencing real company events. In 45 seconds.
`LangGraph` `FastAPI` `React` `scikit-learn` `Groq` `Tavily`

**Portfolio MCP Server**
A working MCP server exposing five tools (project search, stack filtering, resume summary) so any MCP client queries this portfolio as live structured data instead of a static page. Implements real client-side permission gating and tool-call routing — a protocol-compliant server, not a wrapper.
`Python` `MCP (FastMCP SDK)` `stdio transport` `Claude Desktop`

**LLM Cost Router**
A heuristic query-complexity classifier that routes requests between a cheap and an 11x-more-expensive Groq model, cutting cost ~90% on simple queries with no quality loss on complex ones. Includes a live dashboard tracking real spend vs. a same-model baseline.
`FastAPI` `Groq (Llama 3.1 8B / 3.3 70B)` `Vanilla JS`

**LoRA Fine-Tuned Resume Screener** — [Hugging Face](https://huggingface.co/Kus-hal/resume-screener-lora)
Fine-tuned a LoRA adapter on Qwen2.5-0.5B to classify resume-job fit — moving beyond prompt-engineered API calls into parameter-efficient model training on custom labeled data. Published for reproducible, framework-agnostic inference.
`Qwen2.5-0.5B` `LoRA (PEFT)` `PyTorch` `Hugging Face Transformers`

**[AgentLoop](https://github.com/ayush-s-tomar/agentloop)** — [Live Demo](https://agentloop.onrender.com)
Not a chatbot. A multi-step research agent that breaks your question into sub-questions, searches the live web, reflects on gaps, loops back, and delivers a fully cited report.
`FastAPI` `LangGraph` `Groq` `Tavily`

**[AskMyDocs](https://github.com/ayush-s-tomar/intellect-docs-ai)** — [Live Demo](https://intellect-docs-ai.vercel.app)
RAG pipeline that answers questions over 50-page PDFs in under 3 seconds — with source citations and cosine similarity scores. No SQL, no code.
`Next.js` `Supabase` `pgvector` `Cohere`

**[Agentic RAG Research Assistant](https://github.com/ayush-s-tomar/agentic-rag-research-assistant)** — [Live Demo](https://agentic-rag-groq.streamlit.app) | [API Docs](https://agentic-rag-research-assistant-jjch.onrender.com/docs)
Agentic RAG system with LangGraph tool-routing: retrieves grounded answers from uploaded PDFs via a Chroma vector store, refuses out-of-scope questions instead of guessing, and routes queries between a cheap and large model based on complexity.
`LangGraph` `FastAPI` `Streamlit` `Chroma` `Groq`

**[AI Data Analyst Agent](https://github.com/ayush-s-tomar/ai-data-analyst)** — [Live Demo](https://ai-data-analyst-six-sooty.vercel.app)
Upload any CSV, ask questions in plain English, get instant charts and insights. No SQL. No code. Powered by Groq's Llama 3.3 70B.
`FastAPI` `React` `Groq` `pandas` `matplotlib`

**[JobHunt](https://github.com/ayush-s-tomar/jobhunt)** — [Live Demo](https://jobhunt-demo.vercel.app)
Multi-user Telegram job aggregator — AI scores every post and auto-applies via email or form-fill. Watches job channels 24/7 so you don't have to.
`FastAPI` `PostgreSQL` `Groq` `Playwright`

**[Email Agent](https://github.com/ayush-s-tomar/Email-agent)** — [Live Demo](https://email-agent-xi-drab.vercel.app)
AI agent that reads Gmail, classifies emails, drafts context-aware replies, and lets you approve or edit before sending.
`FastAPI` `React` `LLaMA 3.3`

**[ARIA – Voice AI Assistant](https://github.com/ayush-s-tomar/aria-voice-assistant)** — [Live Demo](https://ayush-s-tomar.github.io/aria-voice-assistant)
Speech-to-speech AI assistant with 99-language support and conversation memory. Speak in any language — ARIA transcribes, thinks, and talks back.
`FastAPI` `Faster-Whisper` `Groq` `LLaMA` `gTTS`

**[StartupScope](https://github.com/ayush-s-tomar/startupscope)** — [Live Demo](https://startupscope-ephq.onrender.com)
Multi-agent CrewAI crew — Researcher, Analyst, and Writer agents collaborate to search the web and generate structured startup intelligence reports.
`CrewAI` `Groq` `SerperDev`

**[n8n Email → Slack](https://github.com/ayush-s-tomar/n8n-email-slack)** — [Live Demo](https://ayush22.app.n8n.cloud)
No-code AI automation pipeline: fetches unread Gmail → summarizes with Groq LLaMA → detects priority → pushes digest to Slack.
`n8n` `Groq` `Gmail` `Slack`

**[ResumeIQ](https://github.com/ayush-s-tomar/ResumeIQ)** — [Live Demo](https://resumeiq-55h8.onrender.com)
AI resume screener that scores ATS compatibility, identifies gaps, and exports detailed PDF reports.
`Python` `Flask` `Groq`

---

## 🏆 Achievements

- **Cloud Computing and Distributed Systems** — NPTEL (IIT Kanpur), Elite + Top 5% Topper, 90% (Jan–Mar 2026).

---

## 🛠 Stack

`Python` `JavaScript/TypeScript` `FastAPI` `Flask` `LangGraph` `CrewAI` `MCP` `Groq` `LLaMA 3.3` `LoRA/PEFT` `PyTorch` `Whisper` `React` `Next.js` `Supabase` `PostgreSQL` `Chroma` `n8n` `Docker` `Git` `Render` `Vercel`

---

## 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
- [Two Bugs That Almost Shipped in My Agentic RAG Assistant](https://dev.to/ayushsinghtomar/two-bugs-that-almost-shipped-in-my-agentic-rag-assistant-2fm0)
- [I Got Tired of My Portfolio Looking Like a List of Links. So I Built an MCP Server for It.](https://dev.to/ayushsinghtomar/i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it-440o)
- [I Got Tired of Writing Cold Emails. So I Built an AI Agent to Do It for Me.](https://dev.to/ayushsinghtomar/i-got-tired-of-writing-cold-emails-so-i-built-an-ai-agent-to-do-it-for-me-2m4h)
<!-- BLOG-POST-LIST:END -->

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

## 📬 Let's Build Something

Open to AI Developer roles and freelance contracts — reach out on [LinkedIn](https://linkedin.com/in/ayushsinghtomar), read more on [Dev.to](https://dev.to/ayushsinghtomar), or [hire me on Upwork](https://www.upwork.com/freelancers/ayushtomar).
