"""Thin wrapper with the exact CLI form the assignment shows:

python extract_upgrade_risks.py --project Django --current-version 3.2 --target-version 4.2 [--offline]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from urx.cli import app  # noqa: E402

if __name__ == "__main__":
    app(["extract", *sys.argv[1:]])
