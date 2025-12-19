def suggest_optimizations(idle_df):
    actions = []
    total_savings = 0
    for _, row in idle_df.iterrows():
        action = f"Resource {row['ResourceID']} under {row['Service']} is underutilized. Suggest: stop or downgrade."
        savings = row['Cost'] * 0.8
        total_savings += savings
        actions.append((action, savings))
    return actions, total_savings
