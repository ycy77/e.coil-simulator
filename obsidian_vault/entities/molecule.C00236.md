---
entity_id: "molecule.C00236"
entity_type: "small_molecule"
name: "3-Phospho-D-glyceroyl phosphate"
source_database: "KEGG"
source_id: "C00236"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Phospho-D-glyceroyl phosphate"
  - "1,3-Bisphospho-D-glycerate"
  - "(R)-2-Hydroxy-3-(phosphonooxy)-1-monoanhydride with phosphoric propanoic acid"
  - "D-Glycerate 1,3-diphosphate"
---

# 3-Phospho-D-glyceroyl phosphate

`molecule.C00236`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00236`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Phospho-D-glyceroyl phosphate; 1,3-Bisphospho-D-glycerate; (R)-2-Hydroxy-3-(phosphonooxy)-1-monoanhydride with phosphoric propanoic acid; D-Glycerate 1,3-diphosphate

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Annotation

KEGG compound: 3-Phospho-D-glyceroyl phosphate; 1,3-Bisphospho-D-glycerate; (R)-2-Hydroxy-3-(phosphonooxy)-1-monoanhydride with phosphoric propanoic acid; D-Glycerate 1,3-diphosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.GAPOXNPHOSPHN-RXN|reaction.ecocyc.GAPOXNPHOSPHN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSGLYPHOS-RXN|reaction.ecocyc.PHOSGLYPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00236`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
