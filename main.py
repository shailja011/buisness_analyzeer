from resource_manager.resource import inventory_assets
from financial_manager.finance import finance_manager
from executive_insights.report import all_insights
from employess.employe import salary_insights

def main():
    print("Today's data getting generated.........\n")

    asset_data = inventory_assets()
    team_data = salary_insights()
    financial_data = finance_manager()

    all_insights(asset_data, team_data, financial_data)
if __name__ == "__main__":
    main()