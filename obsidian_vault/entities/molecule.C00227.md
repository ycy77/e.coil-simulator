---
entity_id: "molecule.C00227"
entity_type: "small_molecule"
name: "Acetyl phosphate"
source_database: "KEGG"
source_id: "C00227"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetyl phosphate"
---

# Acetyl phosphate

`molecule.C00227`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00227`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetyl phosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: Acetyl phosphate

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (9)

- `activates` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00230|reaction.R00230]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227
- `is_product_of` --> [[reaction.R00315|reaction.R00315]] `KEGG` `database` - C00002 + C00033 <=> C00008 + C00227
- `is_product_of` --> [[reaction.ecocyc.ACETATEKIN-RXN|reaction.ecocyc.ACETATEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSACETYLTRANS-RXN|reaction.ecocyc.PHOSACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00317|reaction.R00317]] `KEGG` `database` - C00227 + C00001 <=> C00033 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3341|reaction.ecocyc.RXN0-3341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7457|reaction.ecocyc.RXN0-7457]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00227`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
