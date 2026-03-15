# 🛰️ Nusantara Trade Sentinel
*Intelligence for the Future of Southeast Asian Trade*

An Intelligent Multi-Agent System designed to analyze Malaysia's economic health by bridging the gap between **Structured Data** (BigQuery), **Unstructured Knowledge** (BNM/MIDA Reports), and **Visual Intelligence** (Trade Charts).

## 🚀 Key Features
- **Multimodal Orchestration**: Uses Gemini 2.5 Flash to interpret visual trade balance charts and cross-reference them with live databases.
- **Heterogeneous RAG**: Combines a SQL-based Data Warehouse (BigQuery) with a Document-based Knowledge Base (Vertex AI Search).
- **Agentic Firewall Architecture**: Implements an `AgentTool` pattern to isolate specialized toolsets, preventing API conflicts and ensuring high-precision reasoning.

## 🏗️ System Architecture (A2A Flow)
[![](https://mermaid.ink/img/pako:eNqNU02PmzAQ_SuWT0RNUvJBWDhUSoNarbrRbpa2h5I9uDAl1oKN_FFtGvLfOwalQVtVKofBtua953kzPtFcFkBjWirWHMjnZC8Ifl80KM9z8e2DrHh-rNkzqNGITCbv2p0FdSRvyG3NSmhJahtQP7mWKktBGC6gIvcqP4A2ihmpnnrKPmr7vVfa03XpsnPyCExLwUVJ7qRsiLdOPo32tE9335W_U__KNZeCrAWrjprrlmwOTBmded2f3AoDqlFgmMG00dM_eRKooGQGNEl3dy3ZWSZM1kWSNpBzVnFt_gf-uP7YYhEamCtaZVumnsEMTgYk11Wv5JhQnjhLOWAx73nZ2Zt5lxWZkIQZpsEMi7mydxx4B5J2By15SD5knoOkaD44uMxtjV7rCwGIYtiTwVWMsrmxCopOc9jbPvWV7Eai2y_Gsqrzvao49jSHv3F9fGXh1laG17JAdHoUBgfGtdMNHR3jPPKCxngfGNMaVM3clp4c0Z5ibg17GuMSJQ_GjcsZQQ0T36SsLzglbXmg8Q9WadzZpsB-JZzhANZ_ThWaAWojrTA0Dm6ijoTGJ_pC49liPg1Ws2jmL4IgihbRfEyPNA6noR_5y_nKvwnn0WwZncf0VyfrT6PFPIyCmR8uVstVsAzGFAqOfdj2r6x7bOffW_kgRw?type=png)](https://mermaid.live/edit#pako:eNqNU02PmzAQ_SuWT0RNUvJBWDhUSoNarbrRbpa2h5I9uDAl1oKN_FFtGvLfOwalQVtVKofBtua953kzPtFcFkBjWirWHMjnZC8Ifl80KM9z8e2DrHh-rNkzqNGITCbv2p0FdSRvyG3NSmhJahtQP7mWKktBGC6gIvcqP4A2ihmpnnrKPmr7vVfa03XpsnPyCExLwUVJ7qRsiLdOPo32tE9335W_U__KNZeCrAWrjprrlmwOTBmded2f3AoDqlFgmMG00dM_eRKooGQGNEl3dy3ZWSZM1kWSNpBzVnFt_gf-uP7YYhEamCtaZVumnsEMTgYk11Wv5JhQnjhLOWAx73nZ2Zt5lxWZkIQZpsEMi7mydxx4B5J2By15SD5knoOkaD44uMxtjV7rCwGIYtiTwVWMsrmxCopOc9jbPvWV7Eai2y_Gsqrzvao49jSHv3F9fGXh1laG17JAdHoUBgfGtdMNHR3jPPKCxngfGNMaVM3clp4c0Z5ibg17GuMSJQ_GjcsZQQ0T36SsLzglbXmg8Q9WadzZpsB-JZzhANZ_ThWaAWojrTA0Dm6ijoTGJ_pC49liPg1Ws2jmL4IgihbRfEyPNA6noR_5y_nKvwnn0WwZncf0VyfrT6PFPIyCmR8uVstVsAzGFAqOfdj2r6x7bOffW_kgRw)

## 👤 Agent Profiles
|Agent Name|Role|Core Responsibility|
|--|--|--|
|The Sentinel|Orchestrator & Vision Expert|Analyzes user intent, performs **multimodal interpretation of trade charts**, delegates tasks to specialists, and synthesizes all sources into policy briefs.|
|Quant Specialist|Data Engineer|Connects to **Google BigQuery** to pull real numbers (GDP, CPI, Trade Data) from **publicly available datasets**.|
|Market Researcher|Knowledge Expert|Uses **Discovery Engine** to perform **RAG** (Retrieval-Augmented Generation) across **documents** of trade performance and annual reports.|

## 🛠️ Setup Instructions
**Prerequisites:**
- Python 3.10+
- Google Cloud Project with BigQuery and Vertex AI API enabled.
- Google ADK installed.

### Installation:

**Clone the repository**

    git clone https://github.com/vaiyud/nusantara-trade-sentinel.git
    cd nusantara-trade-sentinel

**Setup virtual environment**

    python -m venv .venv

Windows

    .venv\Scripts\activate

Mac/Linux

    source .venv/bin/activate

**Install dependencies**

    pip install google-adk google-cloud-bigquery google-cloud-aiplatform qdrant-client pandas

**Environment variables**

Create a .env file and add your Google Cloud credentials:

    GOOGLE_CLOUD_PROJECT="your-project-id"

**Running the sentinel**

To launch the interface you see in the demo:

    adk web

## 💻 Tech Stack
- **Framework**: Google ADK (Agent Development Kit)
- **Model**: Gemini 2.5 Flash
- **Cloud Infrastructure**: Google Cloud Platform (GCP)
- **Database**: Google BigQuery
- **Search**: Vertex AI Search & Conversation (Agent Builder)

## 📊 Data Provenance
To ensure high-fidelity analysis, the Sentinel was trained on official, publicly available Malaysian economic data:

### Unstructured Data (retrieved from [BNM Publications](https://www.bnm.gov.my/web/guest/bnm-annual-report) & [MIDA Archives](https://www.mida.gov.my/report/))
- *Bank Negara Malaysia (BNM) Annual Report and Economic and Monetary Review from 2022-2024*
- *Malaysian Investment Development Authority (MIDA) Investment Performance Report from 2022-2024*

### Structured Data (retrieved from [Malaysia's Official Open Data Portal](https://data.gov.my/))
- *Monthly Trade Data by Standard International Trade Classification (SITC) Section*
- *Annual Gross Domestic Product (GDP) Data by Economic Sector*
- *Monthly Consumer Price Index (CPI) Data by Division*
