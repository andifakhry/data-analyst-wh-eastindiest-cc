from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from pathlib import Path


def rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")


def dataframe_to_table_data(df, col_widths=None):
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data, colWidths=col_widths, hAlign="LEFT")

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ]))
    return table


def export_inventory_pdf(
    supplier_spending,
    monthly_spending,
    avg_daily_sep,
    avg_daily_oct,
    avg_daily_nov,
    avg_kitchen,
    avg_staff_meals,
):
    REPORT_DIR = Path(__file__).resolve().parents[1] / "reports"
    REPORT_DIR.mkdir(exist_ok=True)

    pdf_path = REPORT_DIR / "eda_inventory_report.pdf"

    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # =====================
    # TITLE
    # =====================
    story.append(Paragraph(
        "EDA Inventory Report<br/>East Indies Coffee Company",
        styles["Title"]
    ))
    story.append(Spacer(1, 14))

    # =====================
    # SUPPLIER SPENDING
    # =====================
    story.append(Paragraph("Total Spending per Supplier", styles["Heading2"]))
    story.append(dataframe_to_table_data(supplier_spending))
    story.append(Spacer(1, 14))

    # =====================
    # MONTHLY SPENDING
    # =====================
    story.append(Paragraph("Total Pembelian per Bulan", styles["Heading2"]))
    story.append(dataframe_to_table_data(monthly_spending))
    story.append(Spacer(1, 14))

    # =====================
    # AVERAGE DAILY
    # =====================
    story.append(Paragraph("Rata-rata Pembelian Harian", styles["Heading2"]))

    avg_data = [
        ["Kategori", "Rata-rata Pembelian per Hari"],
        ["September", rupiah(avg_daily_sep)],
        ["Oktober", rupiah(avg_daily_oct)],
        ["November", rupiah(avg_daily_nov)],
        ["Reguler Kitchen", rupiah(avg_kitchen)],
        ["Staff Meals", rupiah(avg_staff_meals)],
    ]

    story.append(Table(avg_data, hAlign="LEFT"))
    story.append(Spacer(1, 14))

    doc.build(story)

    print(f"PDF berhasil dibuat di: {pdf_path}")
