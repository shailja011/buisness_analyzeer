import csv
import os
from executive_insights.logger import log_error

def finance_manager(filepath="database/finances.csv"):
    if not os.path.exists(filepath):
        err = "finances.csv file not found at specified path"
        log_error("financial_ops", err)
        return {"error": err}
        
    financials = {}
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                financials[row['metric']] = float(row['amount'])

        total_funding = financials.get("total_funding", 0.0)
        monthly_salaries = financials.get('monthly_salaries', 0.0)
        monthly_rent = financials.get("monthly_rent", 0.0)
        marketing_spend = financials.get("marketing_spend", 0.0)
        misc_expenses = financials.get("misc_expenses", 0.0)
        gross_revenue = financials.get("gross_revenue", 0.0)
        cost_of_goods_sold = financials.get("cost_of_goods_sold", 0.0)
        interest_and_taxes = financials.get("interest_and_taxes", 0.0)
        depreciation_amortization = financials.get("depreciation_amortization", 0.0)
        total_customers_acquired = financials.get("total_customers_acquired", 0.0)
    except (ValueError, KeyError) as e:
        err = f"Data corruption or missing column in finances.csv ({str(e)})"
        log_error("financial_ops", err)
        return {"error": err}

    monthly_burn = monthly_rent + marketing_spend + misc_expenses + monthly_salaries
    runway_months = total_funding / monthly_burn if monthly_burn > 0 else float('inf')  

    gross_profit = gross_revenue - cost_of_goods_sold
    gross_margin_pct = (gross_profit / gross_revenue) * 100 if gross_revenue > 0 else 0.0
    
    net_income = gross_revenue - (cost_of_goods_sold + monthly_burn + interest_and_taxes + depreciation_amortization)
    ebitda = net_income + interest_and_taxes + depreciation_amortization
    ebitda_margin_pct = (ebitda / gross_revenue) * 100 if gross_revenue > 0 else 0.0
    
    cac = marketing_spend / total_customers_acquired if total_customers_acquired > 0 else 0.0

    return {
        "total_cash_left": total_funding,
        "monthly_burn_rate": monthly_burn,
        "runway_remaining_months": round(runway_months, 1),
        "gross_revenue": gross_revenue,
        "gross_margin_pct": round(gross_margin_pct, 1),
        "ebitda": ebitda,
        "ebitda_margin_pct": round(ebitda_margin_pct, 1),
        "customer_acquisition_cost": round(cac, 2)
    }