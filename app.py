from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load and clean data
file_path = "GMT_DATA_SINCE 2018-19_ZONE_DIVISION_WISE.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1", header=2)

# Rename columns
df.columns = [
    "RLYCODE", "DIVCODE", "SECCODE", "LINECODE",
    "TMS_Section", "TMS_Line", "GMT_Year",
    "Loc_From_km", "Loc_From_m", "Loc_To_km", "Loc_To_m", "GMT"
]

# Drop rows without GMT
df = df.dropna(subset=["GMT"])
df["GMT"] = pd.to_numeric(df["GMT"], errors="coerce")

# Reports
division_report = df.groupby(["GMT_Year", "DIVCODE"])["GMT"].sum().reset_index()
zone_report = df.groupby(["GMT_Year", "RLYCODE"])["GMT"].sum().reset_index()
overall_report = df.groupby("GMT_Year")["GMT"].sum().reset_index()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/division")
def division():
    # Group by year for separate tables
    division_by_year = {
        year: data.drop("GMT_Year", axis=1).to_html(classes="table table-bordered table-striped", index=False)
        for year, data in division_report.groupby("GMT_Year")
    }

    # Chart
    fig = px.bar(
        division_report, x="GMT_Year", y="GMT", color="DIVCODE", barmode="group",
        title="Division-wise Yearly Comparison"
    )
    graphHTML = pio.to_html(fig, full_html=False)

    return render_template(
        "division.html",
        tables=division_by_year,
        graph=graphHTML
    )

@app.route("/zone")
def zone():
    # Group by year for separate tables
    zone_by_year = {
        year: data.drop("GMT_Year", axis=1).to_html(classes="table table-bordered table-striped", index=False)
        for year, data in zone_report.groupby("GMT_Year")
    }

    # Chart
    fig = px.bar(
        zone_report, x="GMT_Year", y="GMT", color="RLYCODE", barmode="group",
        title="Zone-wise Yearly Comparison"
    )
    graphHTML = pio.to_html(fig, full_html=False)

    return render_template(
        "zone.html",
        tables=zone_by_year,
        graph=graphHTML
    )

@app.route("/overall")
def overall():
    # Group by year for separate tables
    overall_by_year = {
        year: data.drop("GMT_Year", axis=1).to_html(classes="table table-bordered table-striped", index=False)
        for year, data in overall_report.groupby("GMT_Year")
    }

    # Chart
    fig = px.line(
        overall_report, x="GMT_Year", y="GMT", markers=True,
        title="Overall IR Yearly Trend"
    )
    graphHTML = pio.to_html(fig, full_html=False)

    return render_template(
        "overall.html",
        tables=overall_by_year,
        graph=graphHTML
    )

if __name__ == "__main__":
    app.run(debug=True)