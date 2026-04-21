import pandas as pd

def analyze(data):

    df = pd.DataFrame(data, columns=[
        "Subject","Total Lectures","Present"
    ])

    # calculate absent
    df["Absent"] = df["Total Lectures"] - df["Present"]

    # percentage
    df["Percentage"] = (
        df["Present"] / df["Total Lectures"]
    ) * 100

    # overall stats
    total_classes = df["Total Lectures"].sum()
    total_present = df["Present"].sum()
    total_absent = df["Absent"].sum()

    overall_percentage = (total_present/total_classes)*100

    # save subject table
    df.to_excel("attendance.xlsx", index=False)

    # append overall stats
    summary = pd.DataFrame({
        "Metric":[
            "Total Classes",
            "Total Present",
            "Total Absent",
            "Overall Percentage"
        ],
        "Value":[
            total_classes,
            total_present,
            total_absent,
            round(overall_percentage,2)
        ]
    })

    with pd.ExcelWriter(
        "attendance.xlsx",
        engine="openpyxl",
        mode="a"
    ) as writer:

        summary.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

    print("Attendance updated in Excel")