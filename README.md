# 💬 GenAI Customer Service Platform

[![Daily Interactions](https://img.shields.io/badge/Daily%20Interactions-50K%2B-blue)](.)
[![Resolution Rate](https://img.shields.io/badge/Auto%20Resolution-78.3%25-green)](.)
[![CSAT](https://img.shields.io/badge/CSAT-4.6%2F5.0-orange)](.)
[![Languages](https://img.shields.io/badge/Languages-8-purple)](.)

> Production GenAI customer service platform handling **50,000+ daily interactions** across 8 languages. **78.3% autonomous resolution rate**, reducing human agent workload by 4x and improving CSAT from 3.2 to 4.6.

## 🏆 Business Impact
- **78.3% autonomous resolution** — 4x fewer human agents needed
- **CSAT improved: 3.2 → 4.6** (44% improvement in 6 months)
- **R$15M/year savings** in customer service operational costs
- **< 2 second** first response time (vs 4-8 min average wait time)

## 🏗️ Architecture
```
Customer Message ──▶ Intent Classifier ──▶ ┌─ FAQ/KB (RAG)      ─▶ Response
                     (BERT fine-tuned)      ├─ Policy Engine     ─▶ + Citation
                     + Sentiment            ├─ CRM Tool Use      ─▶ + Action
                                            └─ Human Handoff     ─▶ + Escalation
```
