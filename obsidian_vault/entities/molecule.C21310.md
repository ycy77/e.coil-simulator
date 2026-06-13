---
entity_id: "molecule.C21310"
entity_type: "small_molecule"
name: "(8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate"
source_database: "KEGG"
source_id: "C21310"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate"
---

# (8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate

`molecule.C21310`

## Static

- Type: `small_molecule`
- Source: `KEGG:C21310`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: (8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-8340|reaction.ecocyc.RXN-8340]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R11372|reaction.R11372]] `KEGG` `database` - C21310 + C00001 <=> C18239 + C00013
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17809|reaction.ecocyc.RXN-17809]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C21310`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
