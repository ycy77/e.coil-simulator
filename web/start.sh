#!/usr/bin/env bash
# Launch the E.coil diagnostic UI: backend (FastAPI) + frontend (Vite).
#
# Ports: backend 28932, frontend 40211. Both are intentionally unusual to
# avoid clashing with common dev services.
set -euo pipefail
PROJECT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

PYTHON="${PYTHON:-/home/zkyd/software/miniconda3/envs/world/bin/python}"

cleanup() {
  echo "shutting down..."
  jobs -p | xargs -r kill 2>/dev/null || true
  wait 2>/dev/null || true
}
trap cleanup EXIT INT TERM

echo "starting backend on 127.0.0.1:28932 ..."
( cd "$PROJECT_ROOT/web" && "$PYTHON" -m uvicorn backend.main:app --host 127.0.0.1 --port 28932 --log-level warning ) &
BACKEND_PID=$!

sleep 2

echo "starting frontend on 127.0.0.1:40211 ..."
( cd "$PROJECT_ROOT/web/frontend" && npx vite --host 127.0.0.1 --port 40211 ) &
FRONTEND_PID=$!

echo
echo "================================================"
echo "  Backend:  http://127.0.0.1:28932/api/health"
echo "  Frontend: http://127.0.0.1:40211/"
echo "================================================"
echo "  Open http://127.0.0.1:40211/ in a browser."
echo

wait
