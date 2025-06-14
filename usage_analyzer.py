def find_idle_resources(df):
    idle = df[(df['CPUUsage'] < 5) | (df['HoursUsed'] < 100)]
    return idle

def summarize_services(df):
    return df.groupby('Service')['Cost'].sum().reset_index()
