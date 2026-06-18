import csv
import os

def all_insights(asset_data, team_data, financial_data):
    if "error" in asset_data or "error" in team_data or "error" in financial_data:
        print("Data Pipeline Execution Halted: Component Error Detected.")
        if "error" in asset_data: print(f"   [ASSETS ERROR]: {asset_data['error']}")
        if "error" in team_data: print(f"   [TEAM ERROR]: {team_data['error']}")
        if "error" in financial_data: print(f"   [FINANCE ERROR]: {financial_data['error']}")
        return

    total_assets_value = asset_data.get("total amount used", 0.0)
    total_equipments   = asset_data.get("total equipments", 0)
    total_payroll      = team_data.get("Total salary of all employees", 0.0)
    
    cash_reserve       = financial_data.get("total_cash_left", 0.0)
    monthly_burn       = financial_data.get("monthly_burn_rate", 0.0)
    runway_months      = financial_data.get("runway_remaining_months", 0.0)
    
    gross_revenue      = financial_data.get("gross_revenue", 0.0)
    gross_margin_pct   = financial_data.get("gross_margin_pct", 0.0)
    ebitda             = financial_data.get("ebitda", 0.0)
    ebitda_margin_pct  = financial_data.get("ebitda_margin_pct", 0.0)
    cac                = financial_data.get("customer_acquisition_cost", 0.0)

    asset_to_burn_ratio = total_assets_value / monthly_burn if monthly_burn > 0 else 0.0

    print("=" * 65)
    print("                EXECUTIVE BOARDROOM DASHBOARD                ")
    print("=" * 65)
    
    print(f"[TOP LINE]   Gross Revenue (Sales)       : {gross_revenue:,.2f}")
    print(f"[PROFIT]     Gross Margin Percentage     : {gross_margin_pct}%")
    print(f"[EARNINGS]   EBITDA (Operational Profit) : {ebitda:,.2f}")
    print(f"[MARGIN]     EBITDA Margin Percentage    : {ebitda_margin_pct}%")
    print("-" * 65)
    
    print(f"[VALUATION]  Cash Reserves               : {cash_reserve:,.2f}")
    print(f"[BURN RATE]  Monthly Cash Outflow        : {monthly_burn:,.2f}")
    print(f"[RUNWAY]     Survival Runway Clock       : {runway_months} Months")
    print(f"[ECONOMICS]  CAC                         : {cac:,.2f}")
    print("-" * 65)
    
    print(f"[HUMAN RES]  Monthly Team Payroll        : {total_payroll:,.2f}")
    print(f"[LOGISTICS]  Total Asset Valuation       : {total_assets_value:,.2f}")
    print(f"[LOGISTICS]  Active Inventory Count      : {total_equipments} Units")
    print(f"[LOGISTICS]  Asset-to-Burn Leverage Ratio: {asset_to_burn_ratio:.2f}x")
    print("=" * 65)