# 初始状态与连续扰动

## 核心判断

E.coil 支持“终点作为起点”。一次仿真结束后的 `round_N.json` 可以作为下一次仿真的 `round_0` 基线，然后继续加入新的扰动。

这和 MiroFish 的思路一致：

```text
MiroFish: 上一轮舆情状态 -> 新事件 -> 下一段舆情演化
E.coil: 上一次细胞状态 -> 新扰动 -> 下一段分子状态演化
```

## 默认初始状态

如果不提供 profile，系统会使用实体表里的默认状态：

- gene: 通常为 `expressed`
- protein: 通常为 `active`
- small_molecule: 默认 `medium`
- reaction: 通常为 `active`

这只是“通用正常状态”，不是某个真实培养条件。

## 葡萄糖对数生长 profile

默认配置现在使用：

```text
data/initial_conditions/glucose_log_phase.yaml
```

这个 profile 是保守版本，只设置少量环境定义状态：

- glucose high
- lactose absent
- cAMP low
- LacI active
- lacZYA repressed

它不试图一次性标注全基因组。更大规模的条件状态应该由批量 LLM 生成草稿，再人工审核后写回 profile。

## 续跑方式

从上一次 run 的最终状态继续：

```bash
python3 main.py \
  --resume-run runs/20260607_115456_502229 \
  --perturbation "加入过氧化氢" \
  --rounds 3 \
  --mock-llm
```

指定从某一轮继续：

```bash
python3 main.py \
  --resume-run runs/20260607_115456_502229 \
  --resume-round 1 \
  --perturbation "加入过氧化氢"
```

续跑会把旧 run 的目标 round 状态作为新 run 的 `round_0` 基线。旧状态不会标记为新变化；新加入的扰动才会成为本次 run 的 round 0 changed events。

## LLM 批量标注初始条件

脚本：

```bash
python3 scripts/generate_initial_profile_with_llm.py \
  --condition "glucose logarithmic aerobic growth" \
  --entity-type small_molecule \
  --query glucose \
  --query lactose \
  --query cAMP \
  --limit 200
```

默认是 dry-run，只生成 prompt 和草稿 profile，不调用模型。

真正调用 vLLM：

```bash
python3 scripts/generate_initial_profile_with_llm.py \
  --condition "glucose logarithmic aerobic growth" \
  --entity-type small_molecule \
  --limit 500 \
  --use-llm
```

LLM 生成的草稿统一标注为：

```text
source: llm_inference
review_status: unreviewed
```

只有人工审核并确认进入正式 profile 后，才把稳定条目作为 `source: database` 的初始化知识使用。
