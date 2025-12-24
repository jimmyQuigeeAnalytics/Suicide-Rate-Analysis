# Suicide Rate Analysis - Exploratory Data Analysis Report

## Executive Summary

This report presents a comprehensive exploratory data analysis of global suicide rates from 1985 to 2016, covering 101 countries and 27,820 data records. The analysis addresses six key questions to identify patterns in suicide rates across different demographics, countries, and socioeconomic factors.

## Dataset Overview

- **Time Period**: 1985 - 2016 (32 years)
- **Number of Countries**: 101
- **Total Records**: 27,820
- **Missing Data**: HDI (Human Development Index) data is missing for 19,456 records (70% of data)

## Key Findings

### 1. Age Categories Analysis

**Question**: Is the suicide rate more prominent in some age categories than others?

**Answer**: Yes, there is a significant variation in suicide rates across age groups.

**Findings**:
- **Highest Rate**: 75+ years (24.52 per 100k population)
- **Second Highest**: 55-74 years (18.84 per 100k)
- **Third Highest**: 35-54 years (17.06 per 100k)
- **Lowest Rate**: 5-14 years (0.62 per 100k)

**Key Insights**:
- Suicide rates increase dramatically with age, with the elderly (75+) having the highest rates
- The rate for 75+ years is approximately **39 times higher** than the 5-14 years age group
- Middle-aged and elderly populations (35-74 years) show consistently high suicide rates
- Young children (5-14 years) have the lowest suicide rates

**Visualization**: `age_category_analysis.png`

---

### 2. Country Analysis

**Question**: Which countries have the most and the least number of suicides?

**Answer**: There is significant variation between countries, with some countries showing much higher absolute numbers and rates.

**Top 10 Countries by Total Suicides**:
1. Russian Federation: 1,209,742 suicides (32.78 per 100k)
2. United States: 1,034,013 suicides (12.84 per 100k)
3. Japan: 806,902 suicides (21.92 per 100k)
4. France: 329,127 suicides (19.70 per 100k)
5. Ukraine: 319,950 suicides (24.87 per 100k)
6. Germany: 291,262 suicides (14.38 per 100k)
7. Republic of Korea: 261,730 suicides (19.32 per 100k)
8. Brazil: 226,613 suicides (4.67 per 100k)
9. Poland: 139,098 suicides (16.06 per 100k)
10. United Kingdom: 136,805 suicides (7.87 per 100k)

**Bottom 10 Countries by Total Suicides**:
- Saint Kitts and Nevis: 0 suicides
- Dominica: 0 suicides
- San Marino: 4 suicides (5.07 per 100k)
- Antigua and Barbuda: 11 suicides (0.55 per 100k)
- Maldives: 20 suicides (0.69 per 100k)
- Macau: 27 suicides (7.79 per 100k)
- Oman: 33 suicides (0.37 per 100k)
- Grenada: 38 suicides (1.62 per 100k)
- Cabo Verde: 42 suicides (9.29 per 100k)
- Kiribati: 53 suicides (7.15 per 100k)

**Key Insights**:
- Russian Federation has both the highest absolute number and one of the highest rates (32.78 per 100k)
- Large population countries (US, Japan) naturally have high absolute numbers, but rates vary significantly
- Some small island nations report zero or very few suicides, which may reflect data collection issues or cultural factors

**Visualization**: `country_analysis.png`

---

### 3. Population Effect Analysis

**Question**: What is the effect of the population on suicide rates?

**Answer**: Population size has a weak positive correlation (0.0767) with suicide rates per 100k population.

**Findings by Population Size**:
- **<1M**: 8.16 per 100k
- **1M-10M**: 14.42 per 100k
- **10M-50M**: 13.55 per 100k
- **50M-100M**: 10.06 per 100k
- **>100M**: 17.58 per 100k

**Key Insights**:
- The correlation is weak (0.0767), suggesting population size alone is not a strong predictor of suicide rates
- Medium-sized countries (1M-10M and >100M) show higher rates than very small or medium-large countries
- This suggests that factors beyond population size (culture, economic conditions, healthcare systems) are more influential

**Visualization**: `population_effect_analysis.png`

---

### 4. GDP Effect Analysis

**Question**: What is the effect of the GDP of a country on suicide rates?

**Answer**: GDP shows very weak correlations with suicide rates, suggesting economic factors alone are not strong predictors.

**Correlations**:
- **Total GDP vs Suicide Rate**: 0.0490 (very weak)
- **GDP per Capita vs Suicide Rate**: 0.0034 (negligible)

**Findings by GDP per Capita**:
- **<5k**: 12.75 per 100k
- **5k-15k**: 12.04 per 100k
- **15k-30k**: 14.27 per 100k (highest)
- **30k-50k**: 12.64 per 100k
- **>50k**: 12.41 per 100k

**Key Insights**:
- GDP per capita shows almost no correlation (0.0034) with suicide rates
- Countries in the middle GDP range (15k-30k) show slightly higher rates, but the pattern is not strong
- This suggests that economic prosperity alone does not predict suicide rates - other factors (culture, social support, mental health services) are more important
- Both very poor and very rich countries can have varying suicide rates

**Visualization**: `gdp_effect_analysis.png`

---

### 5. Time Trend Analysis

**Question**: What is the trend of suicide rates across all the years?

**Answer**: Suicide rates show a slight decreasing trend over the 32-year period, though the trend is not statistically strong.

**Key Statistics**:
- **Slope**: -0.0348 (decrease of 0.0348 per 100k per year)
- **R-squared**: 0.0723 (weak linear relationship)
- **P-value**: 0.1368 (not statistically significant at α=0.05)

**Trend Pattern**:
- **1985-1995**: Gradual increase from 11.51 to 15.30 per 100k
- **1995-2000**: Peak period with rates around 14-15 per 100k
- **2000-2016**: Gradual decline from 14.22 to 11.47 per 100k

**Key Insights**:
- Overall, there is a slight downward trend, but it's not statistically significant
- The 1990s showed the highest suicide rates globally
- Recent years (2010-2016) show lower rates compared to the 1990s peak
- The trend suggests potential improvements in mental health awareness, prevention programs, or data collection methods

**Visualization**: `yearly_trend_analysis.png`

---

### 6. Gender Difference Analysis

**Question**: Is there a difference between the suicide rates of men and women?

**Answer**: Yes, there is a dramatic difference - males have approximately 3.5 times higher suicide rates than females.

**Overall Rates**:
- **Male**: 20.71 per 100k population
- **Female**: 5.94 per 100k population
- **Ratio**: 3.49:1 (males to females)

**Rates by Gender and Age**:

| Age Category | Male Rate | Female Rate | Ratio |
|-------------|-----------|-------------|-------|
| 75+ years | 45.02 | 13.02 | 3.46:1 |
| 55-74 years | 30.36 | 9.04 | 3.36:1 |
| 35-54 years | 27.37 | 6.97 | 3.93:1 |
| 25-34 years | 21.54 | 4.98 | 4.33:1 |
| 15-24 years | 14.40 | 4.13 | 3.49:1 |
| 5-14 years | 0.82 | 0.41 | 2.00:1 |

**Key Insights**:
- Males consistently have higher suicide rates across all age groups
- The gender gap is most pronounced in the 25-34 age group (4.33:1 ratio)
- Even in the elderly (75+), where both genders have high rates, males still have 3.46x higher rates
- The pattern is consistent across all demographics, suggesting deep-rooted gender differences in suicide risk factors

**Visualization**: `sex_comparison_analysis.png`

---

## Summary of Key Patterns

1. **Age Pattern**: Suicide rates increase dramatically with age, peaking in the 75+ category
2. **Geographic Pattern**: Eastern European and some Asian countries show higher rates; small island nations show lower rates
3. **Population Effect**: Weak correlation - population size alone is not a strong predictor
4. **Economic Effect**: Very weak correlation - GDP does not strongly predict suicide rates
5. **Temporal Pattern**: Slight decreasing trend over time, with peak in the 1990s
6. **Gender Pattern**: Males have consistently 3-4x higher rates than females across all age groups

## Recommendations

Based on these findings, suicide prevention efforts should:

1. **Target High-Risk Groups**: Focus on elderly populations (75+) and middle-aged adults (35-74)
2. **Address Gender Disparities**: Develop male-specific mental health and suicide prevention programs
3. **Country-Specific Approaches**: Countries like Russia, Ukraine, and Japan need targeted interventions
4. **Look Beyond Economics**: Economic factors alone don't predict suicide - focus on social support, mental health services, and cultural factors
5. **Maintain Prevention Programs**: The slight downward trend suggests prevention efforts may be working, but need to be sustained

## Files Generated

1. `suicide_rate_analysis.py` - Complete analysis script
2. `age_category_analysis.png` - Age category visualizations
3. `country_analysis.png` - Country comparison visualizations
4. `population_effect_analysis.png` - Population effect analysis
5. `gdp_effect_analysis.png` - GDP effect analysis
6. `yearly_trend_analysis.png` - Time trend analysis
7. `sex_comparison_analysis.png` - Gender comparison analysis
8. `requirements.txt` - Python package dependencies

---

*Analysis conducted using Python 3.9 with pandas, numpy, matplotlib, seaborn, and scipy*
*Dataset: Global suicide rates from 1985-2016*

