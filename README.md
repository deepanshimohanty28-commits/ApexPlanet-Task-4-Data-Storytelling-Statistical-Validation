# 📊 Task 4 — Data Storytelling & Statistical Validation

### Turning Numbers into Narratives. Turning Evidence into Decisions. 🚀

> **“Good analysis finds patterns. Great analysis proves which patterns matter.”**

This project is the final stage of my **ApexPlanet Data Analytics Internship**, where I transformed sales analysis into a clear business story and validated key observations using statistical hypothesis testing.

---

## 🎯 Project Objective

The goal of this task was to move beyond simply presenting charts and answer a more important question:

**What do the numbers actually mean for the business?**

The analysis focuses on identifying important sales patterns, communicating insights through storytelling, and using statistical evidence to distinguish meaningful differences from observations that may occur by chance.

---

## 🔍 Business Questions

- 📈 Which product category shows strong sales performance?
- 👥 Does customer age have a meaningful relationship with sales?
- 💰 Which factors are most closely related to Total Sales?
- 🧪 Is the difference between Electronics and non-Electronics sales statistically significant?
- 💡 What business actions can be derived from the analysis?

---

## 🧠 Data Story

The analysis follows a simple journey:

**Raw Data → Insights → Patterns → Statistical Validation → Business Decisions**

### 01 — Discover
Explore sales performance and understand customer and transaction patterns.

### 02 — Connect
Analyze relationships between variables such as **Age, Quantity, Unit Price, and Total Sales**.

### 03 — Question
Observed that Electronics had a higher average Total Sales than non-Electronics orders.

### 04 — Validate
Used a **Welch's Independent Two-Sample t-test** to determine whether the observed difference was statistically significant.

### 05 — Decide
Converted the validated findings into practical business recommendations.

---

## 🧪 Hypothesis Testing

### Business Question

**Do Electronics orders have a significantly different average Total Sales compared with non-Electronics orders?**

### Hypotheses

**H₀:** There is no significant difference in average Total Sales.

**H₁:** There is a significant difference in average Total Sales.

### Statistical Method

**Welch's Independent Two-Sample t-test**

**Significance Level:** α = 0.05

---

## 📌 Statistical Results

| Metric | Result |
|---|---:|
| Electronics Orders | 354 |
| Non-Electronics Orders | 646 |
| Electronics Average Sales | ₹143,442.32 |
| Non-Electronics Average Sales | ₹137,183.99 |
| Mean Difference | ₹6,258.33 |
| t-statistic | 0.818 |
| p-value | 0.414 |

### ✅ Decision

Since:

**p-value = 0.414 > 0.05**

➡️ **Fail to Reject H₀**

### 💡 Interpretation

Although Electronics has a higher observed average Total Sales, the difference is **not statistically significant**.

Therefore, there is insufficient statistical evidence to conclude that Electronics orders have significantly different average sales compared with non-Electronics orders.

---

## 📊 Key Insights

### 🔹 Category Performance
Electronics recorded **354 orders**, making it the strongest category by order volume.

### 🔹 Customer Age
Age shows almost no relationship with Total Sales, suggesting that **age alone is not a strong predictor of purchasing value**.

### 🔹 Sales Drivers
**Quantity** and **Unit Price** show meaningful positive relationships with Total Sales.

- Quantity → Total Sales: **0.65**
- Unit Price → Total Sales: **0.69**
- Age → Total Sales: **~0.001**

### 🔹 Statistical Evidence
A higher observed average does not automatically mean a statistically significant difference. Hypothesis testing helped validate the business observation.

---

## 💼 Business Recommendations

- 📦 Encourage larger purchases through bundles and volume-based offers.
- 💰 Monitor pricing strategies and their impact on sales value.
- 🛍️ Continue analyzing high-performing product categories.
- 🎯 Build customer segments around purchasing behavior rather than age alone.
- 🧪 Use statistical validation before making major business decisions based on observed patterns.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| 🐍 Python | Statistical analysis |
| 🐼 Pandas | Data manipulation |
| 📊 Power BI | Interactive dashboards |
| 🗄️ SQL | Business analysis |
| 📗 Excel | Data preparation |
| 📈 Matplotlib / Seaborn | Data visualization |
| 🐙 GitHub | Project documentation & version control |

---

## 📂 Project Files

```text
Task 4
│
├── 📊 Task_4_Presentation.pptx
├── 🧪 hypothesis_testing.py
├── 📄 Task_4_Hypothesis_Testing_Summary.pdf
└── 📘 README.md
