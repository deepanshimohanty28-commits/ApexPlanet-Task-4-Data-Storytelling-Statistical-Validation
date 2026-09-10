"""
Task 4: Data Storytelling & Statistical Validation
Section 3 - Hypothesis Testing
Dataset: Sales transactions (Order_ID, Order_Date, Customer_ID, Customer_Name,
         Age, Gender, City, Product, Category, Quantity, Unit_Price, Total_Sales)

This script:
1. Formulates a testable business hypothesis
2. Performs an appropriate statistical test (T-test and Chi-squared test)
3. Interprets the results (p-value, confidence interval) and states a
   business conclusion
"""

import pandas as pd
import numpy as np
from scipy import stats

# ---------------------------------------------------------------------------
# 1. Load the cleaned dataset (output from Task 1)
# ---------------------------------------------------------------------------
from pathlib import Path

DATA_FOLDER = r"C:\Users\deepa\Downloads\Task 2"
matches = list(Path(DATA_FOLDER).glob("cleaned_sales_data.*"))

if not matches:
    raise FileNotFoundError(
        f"No file named 'cleaned_sales_data.*' found in {DATA_FOLDER}. "
        "Check the folder path and filename."
    )

DATA_PATH = matches[0]
print(f"Loading: {DATA_PATH}")

if DATA_PATH.suffix.lower() == ".csv":
    df = pd.read_csv(DATA_PATH)
else:
    df = pd.read_excel(DATA_PATH)  # requires: pip install openpyxl

print("Dataset shape:", df.shape)
print(df.head())

# ---------------------------------------------------------------------------
# 2. HYPOTHESIS 1 (Independent samples T-test)
# ---------------------------------------------------------------------------
# Business Hypothesis:
#   "Male and Female customers generate a statistically significant
#    difference in average Total_Sales per order."
#
# H0 (Null):        There is NO difference in mean Total_Sales between
#                    Male and Female customers (mu_male = mu_female)
# H1 (Alternative):  There IS a difference in mean Total_Sales between
#                    Male and Female customers (mu_male != mu_female)
#
# Test: Independent two-sample T-test (two groups, continuous outcome)

alpha = 0.05  # significance level

male_sales = df.loc[df["Gender"] == "Male", "Total_Sales"].dropna()
female_sales = df.loc[df["Gender"] == "Female", "Total_Sales"].dropna()

# Levene's test to check equal-variance assumption
levene_stat, levene_p = stats.levene(male_sales, female_sales)
equal_var = levene_p > alpha  # True -> variances roughly equal

t_stat, p_value_ttest = stats.ttest_ind(
    male_sales, female_sales, equal_var=equal_var
)

# 95% Confidence Interval for the difference in means
mean_diff = male_sales.mean() - female_sales.mean()
se_diff = np.sqrt(male_sales.var(ddof=1) / len(male_sales) +
                   female_sales.var(ddof=1) / len(female_sales))
dof = len(male_sales) + len(female_sales) - 2
ci_low, ci_high = stats.t.interval(
    confidence=0.95, df=dof, loc=mean_diff, scale=se_diff
)

print("\n--- Hypothesis 1: T-test on Total_Sales by Gender ---")
print(f"Male mean sales:   {male_sales.mean():.2f}  (n={len(male_sales)})")
print(f"Female mean sales: {female_sales.mean():.2f}  (n={len(female_sales)})")
print(f"Levene's test p-value (equal variance check): {levene_p:.4f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value_ttest:.4f}")
print(f"95% CI for mean difference: ({ci_low:.2f}, {ci_high:.2f})")

if p_value_ttest < alpha:
    print("Result: Reject H0 - statistically significant difference in "
          "average Total_Sales between genders.")
else:
    print("Result: Fail to reject H0 - no statistically significant "
          "difference in average Total_Sales between genders.")

# Business conclusion (example wording - adjust to your actual result)
print(
    "Business Conclusion: "
    + (
        "Gender appears to influence average order value, suggesting "
        "gender-targeted marketing or product bundling could improve revenue."
        if p_value_ttest < alpha
        else "Gender does not meaningfully influence average order value, "
             "so marketing spend need not be split by gender on this basis."
    )
)

# ---------------------------------------------------------------------------
# 3. HYPOTHESIS 2 (Chi-squared test of independence)
# ---------------------------------------------------------------------------
# Business Hypothesis:
#   "Product Category preference is associated with (depends on) Gender."
#
# H0 (Null):        Category and Gender are independent (no association)
# H1 (Alternative):  Category and Gender are NOT independent (associated)
#
# Test: Chi-squared test of independence (two categorical variables)

contingency_table = pd.crosstab(df["Gender"], df["Category"])
chi2_stat, p_value_chi2, dof_chi2, expected = stats.chi2_contingency(
    contingency_table
)

print("\n--- Hypothesis 2: Chi-squared test on Gender vs Category ---")
print("Contingency table:\n", contingency_table)
print(f"Chi-squared statistic: {chi2_stat:.4f}")
print(f"Degrees of freedom: {dof_chi2}")
print(f"P-value: {p_value_chi2:.4f}")

if p_value_chi2 < alpha:
    print("Result: Reject H0 - Category preference is significantly "
          "associated with Gender.")
else:
    print("Result: Fail to reject H0 - no significant association between "
          "Category preference and Gender.")

print(
    "Business Conclusion: "
    + (
        "Product category preferences differ meaningfully by gender, so "
        "category-level merchandising/promotions can be tailored by gender."
        if p_value_chi2 < alpha
        else "Product category preferences are consistent across genders, "
             "so category promotions can be run uniformly."
    )
)

# ---------------------------------------------------------------------------
# 4. Summary table (useful for the presentation deck / final report)
# ---------------------------------------------------------------------------
summary = pd.DataFrame({
    "Hypothesis": [
        "Total_Sales differs by Gender (T-test)",
        "Category is associated with Gender (Chi-squared)"
    ],
    "Test Statistic": [round(t_stat, 4), round(chi2_stat, 4)],
    "P-value": [round(p_value_ttest, 4), round(p_value_chi2, 4)],
    "Significant (alpha=0.05)": [
        p_value_ttest < alpha, p_value_chi2 < alpha
    ]
})

print("\n--- Summary ---")
print(summary)

summary.to_csv("hypothesis_testing_summary.csv", index=False)
print("\nSaved summary to hypothesis_testing_summary.csv")