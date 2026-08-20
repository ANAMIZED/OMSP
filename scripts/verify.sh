#!/usr/bin/env bash
# OMSP full acceptance gate — stranger-runnable, offline-first
# Extracts the audited omsp-complete.zip first so all checks run against
# the exact original sources (no changes / no omissions).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== OMSP verify.sh ==="
echo

# 0. Materialize exact original package from the audited ZIP
echo "[0/7] Extracting omsp-complete.zip (exact audited package)..."
if [ ! -f omsp-complete.zip ]; then
  echo "ERROR: omsp-complete.zip missing"
  exit 1
fi
# Clean any partial stubs then extract
rm -rf reference app omsp.html ARCHITECTURE.md CHANGELOG.md PARITY.md VERIFICATION_REPORT.md
unzip -q -o omsp-complete.zip
# The ZIP contains a top-level omsp-complete/ directory — promote its contents
if [ -d omsp-complete ]; then
  # Move everything up one level
  shopt -s dotglob
  mv omsp-complete/* .
  rmdir omsp-complete
  shopt -u dotglob
fi
echo "  OK (extracted)"

# 1. Python reference suite
echo "[1/7] Python unit tests (62)..."
(cd reference && python3 -m unittest discover -s tests -q)
echo "  OK"

# 2. Python REQ coverage
echo "[2/7] Python SPEC coverage audit..."
(cd reference && python3 audit/verify_coverage.py | grep -q "AUDIT: PASS")
echo "  OK"

# 3. Browser engine tests
echo "[3/7] App engine tests (77)..."
(cd app && node test_engine.js | tail -1 | grep -q "77 passed")
echo "  OK"

# 4. Constellation tests
echo "[4/7] App constellation tests (46)..."
(cd app && node test_constellation.js | tail -1 | grep -q "46 passed")
echo "  OK"

# 5. UI harness
echo "[5/7] App UI harness (48)..."
(cd app && node test_ui.js | tail -1 | grep -q "48 passed")
echo "  OK"

# 6. Spec ↔ app parity
echo "[6/7] Spec ↔ app parity audit..."
(cd app && node audit/verify_parity.js | grep -q "PARITY AUDIT: PASS")
echo "  OK"

# 7. Build reproducibility / integrity
echo "[7/7] omsp.html integrity..."
EXPECTED="1e9abd2b98deb6bc8789648195a04aad1ec871ecc9b568236de35a15924caa01"
ACTUAL=$(sha256sum omsp.html | awk '{print $1}')
if [ "$ACTUAL" = "$EXPECTED" ]; then
  echo "  OK (sha256 match)"
else
  echo "  FAIL: sha256 mismatch (expected $EXPECTED got $ACTUAL)"
  exit 1
fi

echo
echo "=== ALL CHECKS PASSED ==="
