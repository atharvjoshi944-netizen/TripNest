"""
Offline PDF Travel Itinerary & Emergency Guide Generator using ReportLab (Epic 5).
Produces a publication-grade, beautifully formatted PDF travel guide with emergency checklists.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import io
from typing import Dict, Any, List
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
from modules.config import EMERGENCY_DIRECTORIES, CURRENCIES, PLATFORM_ID, APP_NAME

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print 'Page X of Y' in the footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_footer(num_pages)
            super().showPage()
        super().save()

    def draw_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        # Top footer line
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 30, letter[0] - 36, 30)
        footer_text = f"{APP_NAME} • Platform ID: {PLATFORM_ID} • Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 36, 18, footer_text)
        self.drawString(36, 18, "Confidential & Personalized Travel Itinerary Guide — Powered by Generative AI")
        self.restoreState()

def get_emergency_numbers(destination: str) -> Dict[str, str]:
    """Retrieves emergency numbers matching destination or returns international default."""
    dest_lower = destination.lower()
    for country, contacts in EMERGENCY_DIRECTORIES.items():
        if country.lower() in dest_lower:
            return contacts
    return EMERGENCY_DIRECTORIES["General / International"]

import streamlit as st

@st.cache_data(show_spinner=False)
def generate_trip_pdf(trip_data: Dict[str, Any]) -> bytes:
    """
    Builds a professional multi-page PDF travel booklet in memory
    and returns bytes ready for 1-click Streamlit download.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    # Custom Wanderlust Palette
    COLOR_PRIMARY = colors.HexColor("#0F172A")    # Deep Navy
    COLOR_ACCENT = colors.HexColor("#E05A47")     # Warm Terracotta
    COLOR_TEAL = colors.HexColor("#0D9488")       # Travel Teal
    COLOR_MUTED = colors.HexColor("#64748B")      # Muted Slate
    COLOR_BG_LIGHT = colors.HexColor("#F8FAFC")   # Light slate
    COLOR_BORDER = colors.HexColor("#E2E8F0")     # Subtle border

    # Custom Paragraph Styles
    style_cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=COLOR_PRIMARY,
        spaceAfter=4
    )

    style_cover_sub = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=COLOR_MUTED,
        spaceAfter=12
    )

    style_section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=COLOR_ACCENT,
        spaceBefore=10,
        spaceAfter=4
    )

    style_day_header = ParagraphStyle(
        'DayHeader',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_PRIMARY,
        spaceBefore=6,
        spaceAfter=2
    )

    style_body = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1E293B")
    )

    style_body_bold = ParagraphStyle(
        'BodyDarkBold',
        parent=style_body,
        fontName='Helvetica-Bold'
    )

    style_transit_note = ParagraphStyle(
        'TransitNote',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10.5,
        textColor=COLOR_TEAL
    )

    story = []

    # 1. Header Banner & Title
    title = trip_data.get("title", f"Vacation Itinerary: {trip_data.get('destination', 'Travel Guide')}")
    destination = trip_data.get("destination", "Global Destination")
    duration = trip_data.get("duration", 3)
    start_date = trip_data.get("start_date", "Flexible")
    party_type = trip_data.get("party_type", "Travel Party")
    budget_tier = trip_data.get("budget_tier", "Moderate")
    currency = trip_data.get("currency", "USD ($)")
    currency_symbol = CURRENCIES.get(currency, {}).get("symbol", "$")
    estimated_total = trip_data.get("estimated_total_cost", 0.0)

    story.append(Paragraph(f"<b>{title}</b>", style_cover_title))
    story.append(Paragraph(f"Personalized Travel Guide & Route Fatigue Elimination Map • Destination: {destination}", style_cover_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_ACCENT, spaceBefore=0, spaceAfter=8))

    # 2. Key Trip Summary Table (Metadata Matrix)
    meta_data = [
        [
            Paragraph("<b>Destination:</b>", style_body_bold), Paragraph(destination, style_body),
            Paragraph("<b>Duration:</b>", style_body_bold), Paragraph(f"{duration} Days", style_body)
        ],
        [
            Paragraph("<b>Travel Dates:</b>", style_body_bold), Paragraph(str(start_date), style_body),
            Paragraph("<b>Travel Party:</b>", style_body_bold), Paragraph(str(party_type), style_body)
        ],
        [
            Paragraph("<b>Budget Level:</b>", style_body_bold), Paragraph(str(budget_tier), style_body),
            Paragraph("<b>Estimated Total:</b>", style_body_bold), Paragraph(f"{currency_symbol}{estimated_total:,.1f}", style_body_bold)
        ]
    ]

    t_meta = Table(meta_data, colWidths=[90, 180, 90, 180])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    # Transit Optimization Callout
    transit_summary = trip_data.get("transit_summary", "Intelligent geographic clustering applied: Attractions grouped by neighborhood to prevent transit fatigue.")
    callout_data = [[
        Paragraph(f"<b>Geographic Route Optimization & Fatigue Mitigation:</b><br/>{transit_summary}", style_transit_note)
    ]]
    t_callout = Table(callout_data, colWidths=[540])
    t_callout.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDFA")),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_TEAL),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_callout)
    story.append(Spacer(1, 10))

    # 3. Day-by-Day Itineraries
    story.append(Paragraph("<b>Day-by-Day Clustered Vacation Itinerary</b>", style_section_title))

    days = trip_data.get("days", [])
    for day in days:
        d_num = day.get("day_number", 1)
        d_title = day.get("title", f"Day {d_num}")
        d_zone = day.get("cluster_zone", "Central District")
        d_cost = day.get("day_cost", 0.0)
        d_notes = day.get("transit_notes", "Clustered walking and short rideshare route.")

        day_story = []
        day_story.append(Paragraph(f"<b>Day {d_num}: {d_title}</b> &nbsp;<font color='#0D9488'>[Cluster: {d_zone}]</font>", style_day_header))

        # Slot Table
        slots = day.get("slots", {})
        table_rows = [
            [
                Paragraph("<b>Time Slot</b>", style_body_bold),
                Paragraph("<b>Activity & Experience</b>", style_body_bold),
                Paragraph("<b>Vibe & Tips</b>", style_body_bold),
                Paragraph(f"<b>Cost ({currency_symbol})</b>", style_body_bold)
            ]
        ]

        slot_order = [
            ("morning", "🌅 Morning"),
            ("lunch", "🍽️ Lunch"),
            ("afternoon", "🏛️ Afternoon"),
            ("evening", "🌆 Evening")
        ]

        for s_key, s_label in slot_order:
            slot = slots.get(s_key, {})
            time_str = f"<b>{s_label}</b><br/>{slot.get('time', 'Flexible')}"
            act_text = f"<b>{slot.get('title', 'Exploration')}</b><br/>{slot.get('description', '')}"
            vibe_text = f"<b>{slot.get('vibe', 'Leisure')}</b><br/><i>Tip: {slot.get('tips', 'Enjoy your visit.')}</i>"
            cost_text = f"{currency_symbol}{slot.get('estimated_cost', 0.0):,.1f}"

            table_rows.append([
                Paragraph(time_str, style_body),
                Paragraph(act_text, style_body),
                Paragraph(vibe_text, style_body),
                Paragraph(cost_text, style_body_bold)
            ])

        t_day = Table(table_rows, colWidths=[80, 230, 160, 70])
        t_day.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
            ('BOX', (0,0), (-1,-1), 0.5, COLOR_BORDER),
            ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        day_story.append(t_day)

        # Transit Note & Day Total Sub-table
        summary_row = [
            [
                Paragraph(f"<b>Transit Route:</b> {d_notes}", style_transit_note),
                Paragraph(f"<b>Day Subtotal: {currency_symbol}{d_cost:,.1f}</b>", style_body_bold)
            ]
        ]
        t_sub = Table(summary_row, colWidths=[420, 120])
        t_sub.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_LIGHT),
            ('BOX', (0,0), (-1,-1), 0.5, COLOR_BORDER),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        day_story.append(t_sub)
        day_story.append(Spacer(1, 8))

        story.append(KeepTogether(day_story))

    # 4. Emergency Contacts & Essential Travel Checklist (Epic 5)
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Emergency Contacts & Traveler Safety Directory</b>", style_section_title))

    emergency_dict = get_emergency_numbers(destination)
    contact_cells = [
        [
            Paragraph("<b>Service</b>", style_body_bold),
            Paragraph("<b>Number / Contact</b>", style_body_bold),
            Paragraph("<b>Action Protocol</b>", style_body_bold)
        ],
        [
            Paragraph("Police / Law Enforcement", style_body),
            Paragraph(f"<b>{emergency_dict.get('police', '112')}</b>", style_body_bold),
            Paragraph("For security emergencies, theft reports, or urgent assistance", style_body)
        ],
        [
            Paragraph("Ambulance / Medical Response", style_body),
            Paragraph(f"<b>{emergency_dict.get('ambulance', '112')}</b>", style_body_bold),
            Paragraph("For acute illness, medical transport, or hospital triage", style_body)
        ],
        [
            Paragraph("Tourist Helpline / Assistance", style_body),
            Paragraph(f"<b>{emergency_dict.get('tourist_helpline', emergency_dict.get('general_eu', 'Hotel Concierge / 112'))}</b>", style_body_bold),
            Paragraph("English-speaking official traveler support, lost passports & disputes", style_body)
        ]
    ]

    t_emergency = Table(contact_cells, colWidths=[160, 120, 260])
    t_emergency.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#FEE2E2")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#FCA5A5")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#FCA5A5")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(KeepTogether([t_emergency]))
    story.append(Spacer(1, 8))

    # Pre-Travel Checklist
    story.append(Paragraph("<b>Pre-Departure Offline Travel Checklist</b>", style_section_title))
    checklist_text = """
    <b>[ &check; ] Passport & Visas:</b> Ensure at least 6 months remaining validity; store digital photocopies on cloud.<br/>
    <b>[ &check; ] Medical & Travel Insurance:</b> Keep 24/7 policy helpline and policy number noted in offline notes.<br/>
    <b>[ &check; ] Offline Maps:</b> Pre-download Google Maps / maps.me for the designated cluster zones prior to transit.<br/>
    <b>[ &check; ] Currency & Banking:</b> Notify bank of foreign travel; keep multi-currency debit card plus emergency cash in small denominations.<br/>
    <b>[ &check; ] Power & Connectivity:</b> Carry universal plug adapter, 10,000+ mAh power bank, and eSIM activation QR code.<br/>
    <b>[ &check; ] Medications & Health:</b> Pack prescription medicines in original labeled containers alongside basic first-aid supplies.
    """
    p_check = Paragraph(checklist_text, style_body)
    t_check = Table([[p_check]], colWidths=[540])
    t_check.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(KeepTogether([t_check]))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
