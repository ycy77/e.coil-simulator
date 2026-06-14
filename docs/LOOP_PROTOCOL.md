# Local ⇄ Remote development loop

Two agents share this repo through GitHub (`origin/main`):

- **LOCAL** — strong model, on the laptop. Writes/edits code, designs experiments,
  analyzes results. **Cannot reach the vLLM** (it lives on the GPU host) and has
  **no network egress** for downloads.
- **REMOTE** — weaker model, on the GPU host (`/home/zkyd/data1/ycy/P_world/coil`).
  **Has the vLLM and network.** Runs the experiments, writes reports, applies
  small fixes LOCAL asks for.

It is a **baton hand-off, not concurrent editing.** Only one side works at a
time. The baton is the file [`HANDOFF.md`](../HANDOFF.md) at the repo root.

## The cycle

```
LOCAL turn:  git pull --rebase  →  edit code  →  update HANDOFF (TURN: REMOTE + task)
             →  git add -A && git commit && git push
REMOTE turn: git pull --rebase  →  run the commands in HANDOFF  →  write report under
             docs/reports/  →  apply only the small fixes asked for  →
             update HANDOFF (TURN: LOCAL + results)  →  git add -A && commit && push
(repeat)
```

## Rules that keep it conflict-free

1. **Pull before you work, push when done.** Always `git pull --rebase` at the
   start of your turn; `git push` at the end. Never start work without pulling.
2. **One baton.** Only act if `HANDOFF.md` says it is your TURN. If it says the
   other side's turn, stop — they haven't handed off yet.
3. **Ownership avoids collisions:**
   - LOCAL owns: `ecoil_sim/`, `scripts/`, `configs/`, `prompts/`, `schemas/`,
     `tests/`, `main.py`.
   - REMOTE owns: `docs/reports/` (its reports) and `HANDOFF.md` result section.
   - REMOTE edits code ONLY for the specific small fixes LOCAL listed in HANDOFF,
     nothing else. Larger changes are described in the report and left for LOCAL.
4. **If `git pull --rebase` reports a conflict** (should be rare with the baton):
   - In `docs/reports/**` → keep REMOTE's version.
   - In code/tests/configs → keep LOCAL's version (`git checkout --theirs`/`--ours`
     as appropriate), then note the dropped change in the report instead of
     forcing it.
5. **Keep the tree green.** Each side runs `python -m pytest -q` before pushing.
   If red, fix or revert before pushing — never push a red tree.
6. **Never commit large data.** `runs/`, `logs/`, `data/raw/ecocyc/`,
   `data/raw/transcriptome_compendium/` are gitignored. Reports go in
   `docs/reports/` as small Markdown + the key numbers, not raw outputs.

## REMOTE turn — copy-paste checklist

```bash
cd /home/zkyd/data1/ycy/P_world/coil
git pull --rebase origin main

# 1. environment sane?
python -m pytest -q                      # must be green before and after
curl -sS --max-time 5 http://127.0.0.1:8000/v1/models | head   # vLLM up?

# 2. run exactly what HANDOFF.md "TASK FOR REMOTE" lists, e.g.:
#    python scripts/score_phenotypes.py --mode both --repeat 3
#    python scripts/benchmark_perturbation.py --mode both --max-tfs 80
#    ... (HANDOFF lists the precise commands each cycle)

# 3. write the report (use docs/reports/TEMPLATE.md), paste the key numbers
# 4. apply ONLY the small fixes HANDOFF asked for; re-run pytest
# 5. hand the baton back:
#    edit HANDOFF.md -> TURN: LOCAL, fill RESULTS, list what LOCAL should address
git add -A && git commit -m "remote cycle N: <one line>" && git push origin main
```

## LOCAL turn — checklist

```bash
git pull --rebase origin main            # get REMOTE's report + fixes
# read docs/reports/<latest> and HANDOFF.md RESULTS
# make code changes addressing the findings; keep pytest green
# update HANDOFF.md -> TURN: REMOTE, write TASK FOR REMOTE (exact commands)
git add -A && git commit -m "local cycle N: <one line>" && git push origin main
```

## Bootstrapping the remote

The remote's git must be able to push. One-time on the GPU host:
```bash
cd /home/zkyd/data1/ycy/P_world/coil
git remote -v                            # should show origin = the GitHub repo
git config user.name "remote-agent"; git config user.email "remote@zkyd"
# ensure an SSH key or token with push access is configured for origin
```

To run a cycle, the operator simply tells the remote AI: **"Follow HANDOFF.md."**
That file always contains the current task in copy-paste form.
