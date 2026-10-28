<div align="center">

<a href="https://github.com/akashvenkey/Business-Analytics.3">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=78350F,D97706,FBBF24&height=220&section=header&text=Superstore%20BI%20Analytics&fontSize=40&fontColor=ffffff&fontAlignY=38&desc=Enterprise%20Performance%20Dashboards%2C%20DAX%20Measures%20%26%20KPI%20Diagnostics&descSize=16&descAlignY=60&descAlign=50" alt="Superstore BI Analytics Banner" width="100%" />
</a>



### 🔗 **Project Source Link:** [https://github.com/akashvenkey/Business-Analytics.3](https://github.com/akashvenkey/Business-Analytics.3)

[![Source Code](https://img.shields.io/badge/Source_Code-github.com%2Fakashvenkey%2FBusiness-Analytics.3-blue?style=for-the-badge&logo=github)](https://github.com/akashvenkey/Business-Analytics.3)
[![Clone URL](https://img.shields.io/badge/Clone-git_clone-success?style=for-the-badge&logo=git)](https://github.com/akashvenkey/Business-Analytics.3.git)

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![DAX](https://img.shields.io/badge/DAX-Data_Analysis_Expressions-22C55E?style=for-the-badge)](https://learn.microsoft.com/en-us/dax/)
[![Power Query](https://img.shields.io/badge/Power_Query-M_Engine-0284C7?style=for-the-badge)](https://powerquery.microsoft.com/)
[![Dataset](https://img.shields.io/badge/Dataset-9%2C994_Records-EA580C?style=for-the-badge)](https://www.kaggle.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

</div>

---

## 📌 Executive Summary & Overview

Modern retail enterprises manage vast omnichannel transactions where raw transactional logs must be converted into strategic, actionable business intelligence. Without automated KPI metrics and multidimensional slice-and-dice capabilities, business leaders cannot swiftly diagnose margin leaks, regional underperformance, or discount cannibalization.

The **Superstore BI Analytics** repository provides an enterprise-grade business intelligence reporting suite developed in Microsoft Power BI Desktop. Utilizing the benchmark **Sample Superstore** dataset (9,994 transaction records across 13 core dimensions), this project features end-to-end data modeling, ETL data hygiene in Power Query, custom DAX measures, and multi-page interactive executive dashboards. The reports diagnose gross sales performance, segment-wise profitability, geographical shipping velocity, and the direct correlation between promotional discounts and net operating margins.

---

## 📑 Interactive Table of Contents

- [📌 Executive Summary & Overview](#-executive-summary--overview)
- [✨ Key Features & Capabilities](#-key-features--capabilities)
- [📊 Analytical Metrics & DAX KPI Engine](#-analytical-metrics--dax-kpi-engine)
- [🏗 System Architecture & ETL Pipeline](#-system-architecture--etl-pipeline)
- [🛠 Tech Stack Breakdown](#-tech-stack-breakdown)
- [🚀 Reproducible Quickstart & Setup](#-reproducible-quickstart--setup)
- [📂 Project Directory Layout](#-project-directory-layout)
- [👨‍💻 Author & Contributions](#-author--contributions)

---

## ✨ Key Features & Capabilities

- **📈 Executive Sales & Profitability Diagnostics:** Dynamic card visualizers and time-series line charts tracking total revenue, aggregate cost of goods, and net profit margins across fiscal intervals.
- **🗺 Regional & Geographic Decomposition:** Geospatial drill-downs dissecting performance across Central, East, South, and West territories to uncover regional margin discrepancies.
- **👥 Customer Segment Stratification:** Comparative analysis evaluating contribution margins across **Consumer**, **Corporate**, and **Home Office** buyer personas.
- **🏷 Discount vs. Profit Elasticity Analysis:** Scatter-plot distributions and correlation models demonstrating how excessive discounting in specific sub-categories (e.g., Tables, Binders) triggers net negative profit yields.
- **⚡ Interactive Slicers & Tooltip Drillthroughs:** Cross-filtering enabling stakeholders to dynamically isolate results by Order Date, Region, Ship Mode, and Product Category (Technology, Furniture, Office Supplies).

---

## 📊 Analytical Metrics & DAX KPI Engine

The reporting models implement structured Data Analysis Expressions (DAX) to dynamically calculate core business indicators:

| KPI Metric | Conceptual DAX Formulation | Business Interpretation |
| :--- | :--- | :--- |
| **Total Sales** | `SUM(Superstore[Sales])` | Aggregate top-line gross revenue generated across all transactions. |
| **Total Profit** | `SUM(Superstore[Profit])` | Net bottom-line earnings after product costs and recorded expenses. |
| **Profit Margin %** | `DIVIDE([Total Profit], [Total Sales], 0)` | Overall efficiency ratio representing earnings per dollar of gross sales. |
| **Order Volume** | `DISTINCTCOUNT(Superstore[Order ID])` | Total unique orders processed through logistics fulfillment. |
| **Average Discount** | `AVERAGE(Superstore[Discount])` | Mean promotional rate applied across individual order line items. |

---

## 🏗 System Architecture & ETL Pipeline

The following architectural flowchart outlines the end-to-end data transformation from raw CSV to executive dashboard consumption:

```mermaid
flowchart TD
    subgraph Ingestion_Layer["Data Ingestion & Extraction"]
        A1["Raw Superstore Dataset<br/>(9,994 Rows x 13 Columns)"]
        A2["Metadata Validation<br/>(Order ID, Dates, Segment, Region)"]
    end

    subgraph ETL_Transformation["Power Query ETL Pipeline"]
        B1["Type Casting & Null Auditing"]
        B2["Column Normalization & Categorization"]
        B3["Data Model Schema Building<br/>(Fact & Dimensional Attributes)"]
    end

    subgraph DAX_Calculation["DAX & Analytics Engine"]
        C1["Core Measures<br/>(Total Sales, Profit, Margin %)"]
        C2["Calculated Columns<br/>(Delivery Time, Profit Buckets)"]
        C3["Time Intelligence & Elasticity Ratios"]
    end

    subgraph Presentation_Layer["Interactive Power BI Dashboards"]
        D1["Executive Summary Page<br/>(KPI Cards, Category Splits)"]
        D2["Regional Matrix View<br/>(State Heatmaps & Shipping Modes)"]
        D3["Product & Discount Deep-Dive<br/>(Margin Leakage Diagnostics)"]
    end

    A1 --> A2 --> B1 --> B2 --> B3
    B3 --> C1 & C2 & C3
    C1 & C2 & C3 --> D1 & D2 & D3
```

---

## 🛠 Tech Stack Breakdown

| Layer | Tools & Technologies | Role in System |
| :--- | :--- | :--- |
| **BI Platform** | Microsoft Power BI Desktop | Data modeling, interactive canvas rendering, and report compilation |
| **ETL Engine** | Power Query (M Language) | Data hygiene, schema validation, type transformation, and column derivation |
| **Formula Language** | DAX (Data Analysis Expressions) | Business logic aggregation, ratio division, and conditional KPI calculations |
| **Data Source** | Sample Superstore Dataset (CSV) | High-volume tabular retail records (Sales, Profit, Quantity, Discount) |
| **Documentation** | Microsoft Word / PDF Reports | Comprehensive experimental methodology, insights, and faculty report submissions |

---

## 🚀 Reproducible Quickstart & Setup

### Prerequisites
- Windows 10/11 Operating System
- **Microsoft Power BI Desktop** (Free download from Microsoft Store or official website)
- Standard PDF Viewer (Adobe Acrobat, Edge, or Chrome)

### Step-by-Step Exploration
```bash
# 1. Clone this repository
git clone https://github.com/akashvenkey/Business-Analytics.3.git

# 2. Navigate to project root
cd Business-Analytics.3

# 3. Open the primary Power BI report file in Power BI Desktop
start "Experiment 2 BI.pbix"
# Or open the first assignment file:
# start "BA Assignment 1.pbix"
```

### Reviewing the Technical Report
For detailed academic problem formulations, step-by-step methodologies, and visual chart interpretations, review `Superstore_Power_BI_Report.docx` or `POWER_BI_ASSIGNMENT.pdf`.

---

## 📂 Project Directory Layout

```plaintext
Business-Analytics.3/
├── BA Assignment 1.pbix            # Primary Power BI workbook for Assignment 1
├── Experiment 2 BI.pbix            # Comprehensive Power BI report for Superstore performance
├── POWER_BI_ASSIGNMENT.pdf         # Formatted academic submission with visual report snapshots
├── Superstore_Power_BI_Report.docx # Detailed technical report documenting methodology and findings
├── README.md                       # Comprehensive documentation and project guide
└── experiment 1/                   # Experiment 1 lab deliverables
    ├── BA Assignment 1.pbix        # Workbook snapshot for experiment 1
    └── sales performance .1.pdf    # Lab documentation on sales performance analysis
```

---

## 👨‍💻 Author & Contributions

**Akash V**  
- **GitHub:** [@akashvenkey](https://github.com/akashvenkey)  
- **Course:** Bachelor of Computer Applications (Hons) — Semester V  
- **Institution:** Department of Computer Application, Alliance University, Bengaluru  
- **Faculty Guide:** Mr. Aman Kumar Sharma  

Questions, feedback, or suggestions regarding DAX optimizations and dashboard usability are always appreciated!

---

<div align="center">

<a href="https://github.com/akashvenkey/Business-Analytics.3">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=78350F,D97706,FBBF24&height=100&section=footer" alt="Footer Banner" width="100%" />
</a>



### 🔗 **Project Source Link:** [https://github.com/akashvenkey/Business-Analytics.3](https://github.com/akashvenkey/Business-Analytics.3)

[![Source Code](https://img.shields.io/badge/Source_Code-github.com%2Fakashvenkey%2FBusiness-Analytics.3-blue?style=for-the-badge&logo=github)](https://github.com/akashvenkey/Business-Analytics.3)
[![Clone URL](https://img.shields.io/badge/Clone-git_clone-success?style=for-the-badge&logo=git)](https://github.com/akashvenkey/Business-Analytics.3.git)

</div>