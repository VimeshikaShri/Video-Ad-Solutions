import xml.etree.ElementTree as ET
import sys
import re

def validate_vast(filepath):
    """Validate a VAST/VPAID XML tag and return a report."""
    report = {
        "file": filepath,
        "valid": True,
        "errors": [],
        "warnings": [],
        "version": None,
        "is_vpaid": False,
    }

    # 1. Parse XML
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        report["valid"] = False
        report["errors"].append(f"XML parse error: {e}")
        return report

    # TODO 1: Check root element is <VAST>
    # hint: root.tag might include a namespace like '{http://...}VAST'
    # if you see '}' in root.tag, split it.

    # TODO 2: Extract version attribute
    # Valid versions: 2.0, 3.0, 4.0, 4.1, 4.2

    # TODO 3: Find all <Ad> elements
    # If none, report an error.

    # TODO 4: For each Ad, find <InLine> or <Wrapper>
    # If neither, report an error.

    # TODO 5: Validate <Duration> inside <Linear>
    # Regex pattern: r"^\d{2}:\d{2}:\d{2}$"
    # Also check duration is not 00:00:00

    # TODO 6: Check <MediaFile> elements
    # - URL must not be empty
    # - MIME type must be valid (video/mp4, video/webm, application/javascript for VPAID)
    # - URL should use HTTPS (warning if HTTP)

    # TODO 7: Detect VPAID issues
    # - apiFramework should be "VPAID"
    # - MIME type should be "application/javascript"
    # - Set report["is_vpaid"] = True if declared

    # TODO 8: Check quartile tracking events
    # Required: start, firstQuartile, midpoint, thirdQuartile, complete
    # Look inside <TrackingEvents> under <Linear>

    return report


def print_report(report):
    print("=" * 60)
    print("VAST / VPAID Validation Report")
    print("=" * 60)
    print(f"File:   {report['file']}")
    print(f"Version: {report['version'] or 'not detected'}")
    print(f"VPAID:  {'Yes' if report['is_vpaid'] else 'No'}")
    print("-" * 60)

    if report["errors"]:
        print(f"Errors ({len(report['errors'])}):")
        for e in report["errors"]:
            print(f"  - {e}")

    if report["warnings"]:
        print(f"Warnings ({len(report['warnings'])}):")
        for w in report["warnings"]:
            print(f"  - {w}")

    if not report["errors"] and not report["warnings"]:
        print("No issues found.")

    print(f"Result: {'PASS' if report['valid'] and not report['errors'] else 'FAIL'}")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 vast_parser.py <path-to-vast.xml>")
        sys.exit(1)

    report = validate_vast(sys.argv[1])
    print_report(report)