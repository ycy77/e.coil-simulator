---
entity_id: "molecule.C00606"
entity_type: "small_molecule"
name: "3-Sulfino-L-alanine"
source_database: "KEGG"
source_id: "C00606"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Sulfino-L-alanine"
  - "L-Cysteinesulfinic acid"
  - "3-Sulphino-L-alanine"
  - "3-Sulfinoalanine"
---

# 3-Sulfino-L-alanine

`molecule.C00606`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00606`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Sulfino-L-alanine; L-Cysteinesulfinic acid; 3-Sulphino-L-alanine; 3-Sulfinoalanine

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)

## Annotation

KEGG compound: 3-Sulfino-L-alanine; L-Cysteinesulfinic acid; 3-Sulphino-L-alanine; 3-Sulfinoalanine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R02619|reaction.R02619]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22695|reaction.ecocyc.RXN-22695]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-279|reaction.ecocyc.RXN0-279]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASNSYNB-RXN|reaction.ecocyc.ASNSYNB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00606`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
