from analyzer import analyze_csv

print("📊 CSV Insight")
print("=" * 40)

filename = input("Enter CSV file path: ").strip()

result = analyze_csv(filename)

if result is None:
    print("❌ File not found.")
else:
    print("\n📈 Dataset Summary")
    print("=" * 40)

    print(f"Rows       : {result['rows']}")
    print(f"Columns    : {result['columns']}")

    print("\n📋 Column Information:")

    for column, info in result["details"].items():
        print(
            f"- {column}: "
            f"{info['type']} | "
            f"missing={info['missing']}"
        )

        if "average" in info:
            print(f"  Average: {info['average']}")
