#!/usr/bin/env bash
set -euo pipefail

GPU_COUNT=2
DEVICES="6,7"
PORT=8000
HOST="0.0.0.0"
MODEL="/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B"
SERVED_MODEL="/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B"
CHAT_TEMPLATE="/home/zkyd/data1/ycy/P_world/primary world/qwen35_no_thinking.jinja"
MAX_MODEL_LEN=65536

while [[ $# -gt 0 ]]; do
  case "$1" in
    --gpus)
      GPU_COUNT="$2"; shift 2 ;;
    --devices)
      DEVICES="$2"; shift 2 ;;
    --port)
      PORT="$2"; shift 2 ;;
    --host)
      HOST="$2"; shift 2 ;;
    --model)
      MODEL="$2"; shift 2 ;;
    --served-model)
      SERVED_MODEL="$2"; shift 2 ;;
    --chat-template)
      CHAT_TEMPLATE="$2"; shift 2 ;;
    --max-model-len)
      MAX_MODEL_LEN="$2"; shift 2 ;;
    -h|--help)
      cat <<'EOF'
Usage: scripts/start_vllm.sh [options]

Options:
  --gpus N                 GPU count, default 1
  --devices LIST           CUDA_VISIBLE_DEVICES, default 0
  --port PORT              vLLM OpenAI-compatible port, default 8000
  --host HOST              bind host, default 0.0.0.0
  --model PATH             model path
  --served-model NAME      served model name
  --chat-template PATH     chat template path
  --max-model-len N        max model length, default 65536

Example:
  scripts/start_vllm.sh
  scripts/start_vllm.sh --gpus 1 --devices 6
  scripts/start_vllm.sh --gpus 4 --devices 4,5,6,7 --port 8000
EOF
      exit 0 ;;
    *)
      echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

export CUDA_VISIBLE_DEVICES="${DEVICES}"
export PATH="/home/zkyd/software/miniconda3/envs/world/bin:${PATH}"
export LD_LIBRARY_PATH="/home/zkyd/software/miniconda3/envs/world/lib:${LD_LIBRARY_PATH:-}"

echo "[vLLM] devices=${CUDA_VISIBLE_DEVICES} gpus=${GPU_COUNT} port=${PORT}"
exec /home/zkyd/software/miniconda3/envs/world/bin/python -m vllm.entrypoints.openai.api_server \
  --host "${HOST}" \
  --port "${PORT}" \
  --model "${MODEL}" \
  --served-model-name "${SERVED_MODEL}" \
  --tensor-parallel-size "${GPU_COUNT}" \
  --max-model-len "${MAX_MODEL_LEN}" \
  --enable-prefix-caching \
  --trust-remote-code \
  --chat-template "${CHAT_TEMPLATE}"
