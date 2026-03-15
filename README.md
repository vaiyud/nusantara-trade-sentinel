
# 🛰️ Nusantara Trade Sentinel
*Intelligence for the Future of Southeast Asian Trade*

An Intelligent Multi-Agent System designed to analyze Malaysia's economic health by bridging the gap between **Structured Data** (BigQuery), **Unstructured Knowledge** (BNM/MIDA Reports), and **Visual Intelligence** (Trade Charts).

## 🚀 Key Features
- **Multimodal Orchestration**: Uses Gemini 2.5 Flash to interpret visual trade balance charts and cross-reference them with live databases.
- **Heterogeneous RAG**: Combines a SQL-based Data Warehouse (BigQuery) with a Document-based Knowledge Base (Vertex AI Search).
- **Agentic Firewall Architecture**: Implements an `AgentTool` pattern to isolate specialized toolsets, preventing API conflicts and ensuring high-precision reasoning.

## 🏗️ System Architecture (A2A Flow)
[![](https://mermaid.ink/img/pako:eNqNU1tv0zAU_iuWn1LRlSRtWpIHpNIINLFJ6zJ4IN2DSQ6JRWJHvqB1Tf87x8lKqyEk_HB80fm-79x8oIUsgSa0UqyryUO6EwTXFw3K85x9eycbXuxb9hPUZEKurt73WwtqT96Q65ZV0JPMdqB-cS1V_qBYCSQDYbiA5nHkGq2230eJHV1XzqEg98C0FFxU5EbKjnjr9PNkR0d3t87Eg-xXrrkUZC1Ys9dc92RTM2V07g07uRYGVKfAMINuk8d_8qTQQMUMaJJtb3qytUyYfLAk66DgrOHa_A_8fv2pxyQ0MFXUoPJUFrbF1F5CvOQ4n0YhR4TqxJWSA-bygVdDWXPvdCJXJGWGaTCXuZzlBg4MAcvtHnpyl37MPQfJjFTg4C_x6BMBiPKyJRehGGULYxWUg-ZlT0fXV7IbicV-MpY1Q9mbhmNLC_gbN9pXFby1jeGtLBGd7YWpYeimGzY6xTnkJU0wHpjSFlTL3JUeHNGOom8LO5rgESVr46bliKCOiW9StieckraqafKDNRpvtiuxXSlnOH_tn1eFxQC1kVYYmqzCYCChyYE-0SSYh7NoGcSBP4-iOJ7H4ZTu0Wu28mN_ES79d6swDhbxcUqfB1l_Fs_DVRwF_mq-XCyjRTSlUHLsw-34u4ZPdvwN8Jgc3g?type=png)](https://mermaid.live/edit#pako:eNqNU1tv0zAU_iuWn1LRlSRtWpIHpNIINLFJ6zJ4IN2DSQ6JRWJHvqB1Tf87x8lKqyEk_HB80fm-79x8oIUsgSa0UqyryUO6EwTXFw3K85x9eycbXuxb9hPUZEKurt73WwtqT96Q65ZV0JPMdqB-cS1V_qBYCSQDYbiA5nHkGq2230eJHV1XzqEg98C0FFxU5EbKjnjr9PNkR0d3t87Eg-xXrrkUZC1Ys9dc92RTM2V07g07uRYGVKfAMINuk8d_8qTQQMUMaJJtb3qytUyYfLAk66DgrOHa_A_8fv2pxyQ0MFXUoPJUFrbF1F5CvOQ4n0YhR4TqxJWSA-bygVdDWXPvdCJXJGWGaTCXuZzlBg4MAcvtHnpyl37MPQfJjFTg4C_x6BMBiPKyJRehGGULYxWUg-ZlT0fXV7IbicV-MpY1Q9mbhmNLC_gbN9pXFby1jeGtLBGd7YWpYeimGzY6xTnkJU0wHpjSFlTL3JUeHNGOom8LO5rgESVr46bliKCOiW9StieckraqafKDNRpvtiuxXSlnOH_tn1eFxQC1kVYYmqzCYCChyYE-0SSYh7NoGcSBP4-iOJ7H4ZTu0Wu28mN_ES79d6swDhbxcUqfB1l_Fs_DVRwF_mq-XCyjRTSlUHLsw-34u4ZPdvwN8Jgc3g)

## 👤 Agent Profiles
|Agent Name|Role|Core Responsibility|
|--|--|--|
|Trade Sentinel|Orchestrator & Vision Expert|Analyzes user intent, performs **multimodal interpretation of trade charts**, delegates tasks to specialists, and synthesizes all sources into policy briefs.|
|Quant Specialist|Data Engineer|Connects to **Google BigQuery** to pull real numbers (GDP, CPI, Trade Data) from **publicly available datasets**.|
|Document Analyst|Knowledge Expert|Uses **Discovery Engine** to perform **RAG** (Retrieval-Augmented Generation) across **documents** of trade performance and annual reports.|

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

To launch the interface seen in the demo:

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

![NotebookLM Functional Diagram](https://github.com/vaiyud/nusantara-trade-sentinel/blob/main/NotebookLM%20Mind%20Map.png)
*Functional Mind Map generated via NotebookLM, illustrating the structured intelligence used by the Document Analyst agent.*
