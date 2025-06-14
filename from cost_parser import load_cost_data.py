from cost_parser import load_cost_data
from usage_analyzer import find_idle_resources, summarize_services
from optimizer import suggest_optimizations
from report_generator import generate_report

def main():
    print("🔍 Loading cloud usage data...")
    df = load_cost_data("sample_data/aws_bill.csv")

    print("📊 Analyzing usage...")
    idle = find_idle_resources(df)
    summary = summarize_services(df)
    actions, savings = suggest_optimizations(idle)

    print("💡 Optimization Suggestions:")
    for act, save in actions:
        print(f"- {act} | Estimated saving: ₹{int(save)}")

    print(f"\n✅ Total Potential Savings: ₹{int(savings)}")

    generate_report(actions, savings)
    print("📄 Report generated: reports/optimization_report.pdf")

if __name__ == "__main__":
    main()
