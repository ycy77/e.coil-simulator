# Co-expression validation of regulatory edges (data/normalized/simulation)

External data: PRECISE-1K (SBRG, Lamoureux 2023; 1035 RNA-seq samples) — 1035 samples, 2541 mapped gene keys.
Regulatory edges scored (both endpoints have expression): **6187** / 7092.

## Correlation by regulatory sign

| Sign | n | mean r | frac r>0 | frac |r|≥0.3 |
| --- | --- | --- | --- | --- |
| activates (expect r>0) | 3786 | 0.176 | 0.728 | 0.273 |
| represses (expect r<0) | 2401 | 0.163 | 0.626 | 0.267 |

**Sign agreement with co-expression: 0.591 (3656/6187)** (activates↔r>0, represses↔r<0).

## Interpretation

- activates mean_r should be clearly above represses mean_r; ideally activates>0>represses.
- This is independent of RegulonDB (expression data, not curation), so agreement is genuine external validation of the graph's regulatory directions.
- Edges with sign opposite to a strong correlation are data-quality candidates to review.
