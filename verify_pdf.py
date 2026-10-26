"""
Verification script testing PDF generation with ReportLab.
"""

import os
from sample_data.showcase_trips import SHOWCASE_TRIPS
from modules.pdf_export import generate_trip_pdf

def main():
    print("Testing PDF Generation for Showcase Trip...")
    trip = SHOWCASE_TRIPS[0]
    pdf_bytes = generate_trip_pdf(trip)
    print(f"Generated PDF bytes size: {len(pdf_bytes)} bytes")
    assert len(pdf_bytes) > 5000, "PDF size should be at least 5KB"
    assert pdf_bytes[:4] == b"%PDF", "Generated file must start with %PDF magic header"

    test_out = "test_kyoto_itinerary.pdf"
    with open(test_out, "wb") as f:
        f.write(pdf_bytes)
    print(f"Successfully saved test PDF to {test_out}")
    print("[SUCCESS] ReportLab PDF generation verified!")

if __name__ == "__main__":
    main()
