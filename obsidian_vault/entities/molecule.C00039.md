---
entity_id: "molecule.C00039"
entity_type: "small_molecule"
name: "DNA"
source_database: "KEGG"
source_id: "C00039"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "DNA"
  - "DNAn"
  - "DNAn+1"
  - "(Deoxyribonucleotide)n"
  - "(Deoxyribonucleotide)m"
  - "(Deoxyribonucleotide)n+m"
  - "Deoxyribonucleic acid"
---

# DNA

`molecule.C00039`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00039`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: DNA; DNAn; DNAn+1; (Deoxyribonucleotide)n; (Deoxyribonucleotide)m; (Deoxyribonucleotide)n+m; Deoxyribonucleic acid

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: DNA; DNAn; DNAn+1; (Deoxyribonucleotide)n; (Deoxyribonucleotide)m; (Deoxyribonucleotide)n+m; Deoxyribonucleic acid

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039
- `is_product_of` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - C00286 + C00039 <=> C00013 + C00039
- `is_product_of` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - C00458 + C00039 <=> C00013 + C00039
- `is_product_of` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - C00459 + C00039 <=> C00013 + C00039
- `is_product_of` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - C00677 + C00039(n) <=> C00013 + C00039(n+1)
- `is_product_of` --> [[reaction.R00382|reaction.R00382]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_substrate_of` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - C00286 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - C00458 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - C00459 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - C00677 + C00039(n) <=> C00013 + C00039(n+1)
- `is_substrate_of` --> [[reaction.R00380|reaction.R00380]] `KEGG` `database` - C00019 + C00039 <=> C00021 + C02967
- `is_substrate_of` --> [[reaction.R00382|reaction.R00382]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00039`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
