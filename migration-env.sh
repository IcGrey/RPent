source /data/gc02/RPent/.venv/bin/activate

export HF_HOME=/data/gc02/cache/huggingface
export XDG_CACHE_HOME=/data/gc02/cache
export HF_HUB_DISABLE_XET=1

export LIBERO_TYPE=pro
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

export PI05_CHECKPOINT_PATH=/data/gc02/RPent/checkpoints/RLinf-Pi05-LIBERO-130-fullshot-SFT
export SAM3_CHECKPOINT_PATH=/data/gc02/RPent/checkpoints/sam3/sam3.pt

export RPENT_CODEX_EXECUTABLE=/data/gc02/tools/codex
export CODEX_BIN=/data/gc02/RPent/migration/rpent-codex-lab

unset CUDA_VISIBLE_DEVICES
unset CODEX_API_KEY CODEX_BASE_URL
