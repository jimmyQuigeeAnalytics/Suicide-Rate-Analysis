"""
Suicide Rate Analysis - Exploratory Data Analysis
This script performs comprehensive EDA to answer key questions about suicide rates globally.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('master.csv')

# Data cleaning
print("\nData Cleaning...")
print(f"Original dataset shape: {df.shape}")

# Clean GDP columns - remove commas and convert to numeric
df['gdp_for_year ($)'] = df[' gdp_for_year ($) '].str.replace(',', '').str.strip().astype(float)
# gdp_per_capita already has correct name, just convert to float
df['gdp_per_capita ($)'] = pd.to_numeric(df['gdp_per_capita ($)'], errors='coerce')

# Drop the original GDP column with spaces
df = df.drop(columns=[' gdp_for_year ($) '])

# Check for missing values
print(f"\nMissing values:\n{df.isnull().sum()}")

# Basic info
print(f"\nDataset Info:")
print(f"Date range: {df['year'].min()} - {df['year'].max()}")
print(f"Number of countries: {df['country'].nunique()}")
print(f"Total records: {len(df)}")

# ============================================================================
# QUESTION 1: Is the suicide rate more prominent in some age categories than others?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 1: Is the suicide rate more prominent in some age categories than others?")
print("="*80)

age_analysis = df.groupby('age').agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean'
}).reset_index()

# Calculate overall suicide rate per 100k for each age group
age_analysis['overall_rate'] = (age_analysis['suicides_no'] / age_analysis['population']) * 100000

# Sort by suicide rate
age_analysis = age_analysis.sort_values('overall_rate', ascending=False)

print("\nSuicide Rates by Age Category:")
print(age_analysis[['age', 'suicides_no', 'overall_rate']].to_string(index=False))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Bar plot of suicide rates by age
age_order = age_analysis.sort_values('overall_rate', ascending=False)['age'].values
sns.barplot(data=age_analysis, x='age', y='overall_rate', order=age_order, ax=axes[0], palette='viridis')
axes[0].set_title('Average Suicide Rate per 100k Population by Age Category', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Age Category', fontsize=12)
axes[0].set_ylabel('Suicide Rate (per 100k)', fontsize=12)
axes[0].tick_params(axis='x', rotation=45)

# Total suicides by age
sns.barplot(data=age_analysis, x='age', y='suicides_no', order=age_order, ax=axes[1], palette='plasma')
axes[1].set_title('Total Number of Suicides by Age Category', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Age Category', fontsize=12)
axes[1].set_ylabel('Total Suicides', fontsize=12)
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('age_category_analysis.png', dpi=300, bbox_inches='tight')
print("\nSaved visualization: age_category_analysis.png")

# ============================================================================
# QUESTION 2: Which countries have the most and the least number of suicides?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 2: Which countries have the most and the least number of suicides?")
print("="*80)

country_analysis = df.groupby('country').agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean'
}).reset_index()

# Calculate overall rate
country_analysis['overall_rate'] = (country_analysis['suicides_no'] / country_analysis['population']) * 100000
country_analysis = country_analysis.sort_values('suicides_no', ascending=False)

print("\nTop 10 Countries by Total Suicides:")
print(country_analysis[['country', 'suicides_no', 'overall_rate']].head(10).to_string(index=False))

print("\nBottom 10 Countries by Total Suicides:")
print(country_analysis[['country', 'suicides_no', 'overall_rate']].tail(10).to_string(index=False))

# Visualization
fig, axes = plt.subplots(2, 1, figsize=(14, 12))

# Top 15 countries by total suicides
top_countries = country_analysis.head(15)
sns.barplot(data=top_countries, x='suicides_no', y='country', ax=axes[0], palette='Reds_r')
axes[0].set_title('Top 15 Countries by Total Number of Suicides', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Total Suicides', fontsize=12)
axes[0].set_ylabel('Country', fontsize=12)

# Bottom 15 countries by total suicides
bottom_countries = country_analysis.tail(15)
sns.barplot(data=bottom_countries, x='suicides_no', y='country', ax=axes[1], palette='Blues_r')
axes[1].set_title('Bottom 15 Countries by Total Number of Suicides', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Total Suicides', fontsize=12)
axes[1].set_ylabel('Country', fontsize=12)

plt.tight_layout()
plt.savefig('country_analysis.png', dpi=300, bbox_inches='tight')
print("\nSaved visualization: country_analysis.png")

# ============================================================================
# QUESTION 3: What is the effect of the population on suicide rates?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 3: What is the effect of the population on suicide rates?")
print("="*80)

# Aggregate by country-year to analyze population effect
country_year = df.groupby(['country', 'year']).agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean'
}).reset_index()

# Calculate correlation
correlation = country_year['population'].corr(country_year['suicides/100k pop'])
print(f"\nCorrelation between population and suicide rate (per 100k): {correlation:.4f}")

# Group population into bins for analysis
country_year['population_bin'] = pd.cut(country_year['population'], 
                                        bins=[0, 1e6, 10e6, 50e6, 100e6, 1e9], 
                                        labels=['<1M', '1M-10M', '10M-50M', '50M-100M', '>100M'])

pop_bin_analysis = country_year.groupby('population_bin')['suicides/100k pop'].mean().reset_index()
print("\nAverage Suicide Rate by Population Size:")
print(pop_bin_analysis.to_string(index=False))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot
axes[0].scatter(country_year['population'], country_year['suicides/100k pop'], alpha=0.3, s=20)
axes[0].set_xlabel('Population', fontsize=12)
axes[0].set_ylabel('Suicide Rate (per 100k)', fontsize=12)
axes[0].set_title('Population vs Suicide Rate (per 100k)', fontsize=14, fontweight='bold')
axes[0].set_xscale('log')
axes[0].grid(True, alpha=0.3)

# Box plot by population bins
sns.boxplot(data=country_year, x='population_bin', y='suicides/100k pop', ax=axes[1], palette='Set2')
axes[1].set_title('Suicide Rate Distribution by Population Size', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Population Size Category', fontsize=12)
axes[1].set_ylabel('Suicide Rate (per 100k)', fontsize=12)
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('population_effect_analysis.png', dpi=300, bbox_inches='tight')
print("\nSaved visualization: population_effect_analysis.png")

# ============================================================================
# QUESTION 4: What is the effect of the GDP of a country on suicide rates?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 4: What is the effect of the GDP of a country on suicide rates?")
print("="*80)

# Aggregate by country-year for GDP analysis
gdp_analysis = df.groupby(['country', 'year']).agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean',
    'gdp_for_year ($)': 'first',
    'gdp_per_capita ($)': 'first'
}).reset_index()

# Calculate correlations
corr_gdp_total = gdp_analysis['gdp_for_year ($)'].corr(gdp_analysis['suicides/100k pop'])
corr_gdp_per_capita = gdp_analysis['gdp_per_capita ($)'].corr(gdp_analysis['suicides/100k pop'])

print(f"\nCorrelation between Total GDP and suicide rate: {corr_gdp_total:.4f}")
print(f"Correlation between GDP per capita and suicide rate: {corr_gdp_per_capita:.4f}")

# Group GDP per capita into bins
gdp_analysis['gdp_per_capita_bin'] = pd.cut(gdp_analysis['gdp_per_capita ($)'], 
                                            bins=[0, 5000, 15000, 30000, 50000, 1e6], 
                                            labels=['<5k', '5k-15k', '15k-30k', '30k-50k', '>50k'])

gdp_bin_analysis = gdp_analysis.groupby('gdp_per_capita_bin')['suicides/100k pop'].mean().reset_index()
print("\nAverage Suicide Rate by GDP per Capita:")
print(gdp_bin_analysis.to_string(index=False))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot: GDP per capita vs suicide rate
axes[0].scatter(gdp_analysis['gdp_per_capita ($)'], gdp_analysis['suicides/100k pop'], alpha=0.3, s=20)
axes[0].set_xlabel('GDP per Capita ($)', fontsize=12)
axes[0].set_ylabel('Suicide Rate (per 100k)', fontsize=12)
axes[0].set_title('GDP per Capita vs Suicide Rate', fontsize=14, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Box plot by GDP per capita bins
sns.boxplot(data=gdp_analysis, x='gdp_per_capita_bin', y='suicides/100k pop', ax=axes[1], palette='Set3')
axes[1].set_title('Suicide Rate Distribution by GDP per Capita', fontsize=14, fontweight='bold')
axes[1].set_xlabel('GDP per Capita Category', fontsize=12)
axes[1].set_ylabel('Suicide Rate (per 100k)', fontsize=12)

plt.tight_layout()
plt.savefig('gdp_effect_analysis.png', dpi=300, bbox_inches='tight')
print("\nSaved visualization: gdp_effect_analysis.png")

# ============================================================================
# QUESTION 5: What is the trend of suicide rates across all the years?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 5: What is the trend of suicide rates across all the years?")
print("="*80)

yearly_analysis = df.groupby('year').agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean'
}).reset_index()

yearly_analysis['overall_rate'] = (yearly_analysis['suicides_no'] / yearly_analysis['population']) * 100000

print("\nYearly Suicide Rate Trend:")
print(yearly_analysis[['year', 'suicides_no', 'overall_rate']].to_string(index=False))

# Calculate trend
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(yearly_analysis['year'], yearly_analysis['overall_rate'])
print(f"\nLinear Trend Analysis:")
print(f"Slope: {slope:.4f} (suicide rate change per year)")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value: {p_value:.4f}")

# Visualization
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Line plot of suicide rate over time
axes[0].plot(yearly_analysis['year'], yearly_analysis['overall_rate'], marker='o', linewidth=2, markersize=6)
axes[0].plot(yearly_analysis['year'], intercept + slope * yearly_analysis['year'], 
             'r--', linewidth=2, label=f'Trend (slope={slope:.4f})')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Suicide Rate (per 100k)', fontsize=12)
axes[0].set_title('Global Suicide Rate Trend Over Time', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Bar plot of total suicides over time
axes[1].bar(yearly_analysis['year'], yearly_analysis['suicides_no'], color='steelblue', alpha=0.7)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Total Suicides', fontsize=12)
axes[1].set_title('Total Number of Suicides Over Time', fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('yearly_trend_analysis.png', dpi=300, bbox_inches='tight')
print("\nSaved visualization: yearly_trend_analysis.png")

# ============================================================================
# QUESTION 6: Is there a difference between the suicide rates of men and women?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 6: Is there a difference between the suicide rates of men and women?")
print("="*80)

sex_analysis = df.groupby('sex').agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean'
}).reset_index()

sex_analysis['overall_rate'] = (sex_analysis['suicides_no'] / sex_analysis['population']) * 100000

print("\nSuicide Rates by Sex:")
print(sex_analysis[['sex', 'suicides_no', 'overall_rate']].to_string(index=False))

# Calculate ratio
male_rate = sex_analysis[sex_analysis['sex'] == 'male']['overall_rate'].values[0]
female_rate = sex_analysis[sex_analysis['sex'] == 'female']['overall_rate'].values[0]
ratio = male_rate / female_rate
print(f"\nMale to Female Suicide Rate Ratio: {ratio:.2f}:1")

# Analysis by sex and age
sex_age_analysis = df.groupby(['sex', 'age']).agg({
    'suicides_no': 'sum',
    'population': 'sum',
    'suicides/100k pop': 'mean'
}).reset_index()
sex_age_analysis['overall_rate'] = (sex_age_analysis['suicides_no'] / sex_age_analysis['population']) * 100000

print("\nSuicide Rates by Sex and Age:")
print(sex_age_analysis[['sex', 'age', 'overall_rate']].to_string(index=False))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Bar plot comparing sexes
sns.barplot(data=sex_analysis, x='sex', y='overall_rate', palette=['lightblue', 'lightcoral'], ax=axes[0])
axes[0].set_title('Average Suicide Rate by Sex', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Sex', fontsize=12)
axes[0].set_ylabel('Suicide Rate (per 100k)', fontsize=12)

# Grouped bar plot by sex and age
sex_age_pivot = sex_age_analysis.pivot(index='age', columns='sex', values='overall_rate')
sex_age_pivot = sex_age_pivot.sort_values('male', ascending=False)
sex_age_pivot.plot(kind='bar', ax=axes[1], color=['lightblue', 'lightcoral'], width=0.8)
axes[1].set_title('Suicide Rate by Sex and Age Category', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Age Category', fontsize=12)
axes[1].set_ylabel('Suicide Rate (per 100k)', fontsize=12)
axes[1].legend(title='Sex')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('sex_comparison_analysis.png', dpi=300, bbox_inches='tight')
print("\nSaved visualization: sex_comparison_analysis.png")

# ============================================================================
# SUMMARY REPORT
# ============================================================================
print("\n" + "="*80)
print("SUMMARY OF KEY FINDINGS")
print("="*80)

print("\n1. AGE CATEGORIES:")
print(f"   Highest suicide rate: {age_analysis.iloc[0]['age']} ({age_analysis.iloc[0]['overall_rate']:.2f} per 100k)")
print(f"   Lowest suicide rate: {age_analysis.iloc[-1]['age']} ({age_analysis.iloc[-1]['overall_rate']:.2f} per 100k)")

print("\n2. COUNTRIES:")
print(f"   Country with most suicides: {country_analysis.iloc[0]['country']} ({country_analysis.iloc[0]['suicides_no']:,.0f} total)")
print(f"   Country with least suicides: {country_analysis.iloc[-1]['country']} ({country_analysis.iloc[-1]['suicides_no']:,.0f} total)")

print("\n3. POPULATION EFFECT:")
print(f"   Correlation with suicide rate: {correlation:.4f}")

print("\n4. GDP EFFECT:")
print(f"   Correlation (GDP per capita): {corr_gdp_per_capita:.4f}")

print("\n5. TIME TREND:")
if slope > 0:
    print(f"   Suicide rates are INCREASING over time (slope: {slope:.4f})")
else:
    print(f"   Suicide rates are DECREASING over time (slope: {slope:.4f})")

print("\n6. SEX DIFFERENCE:")
print(f"   Male suicide rate: {male_rate:.2f} per 100k")
print(f"   Female suicide rate: {female_rate:.2f} per 100k")
print(f"   Males have {ratio:.2f}x higher suicide rate than females")

print("\n" + "="*80)
print("Analysis complete! All visualizations have been saved.")
print("="*80)

