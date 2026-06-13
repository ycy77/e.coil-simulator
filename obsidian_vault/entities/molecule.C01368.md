---
entity_id: "molecule.C01368"
entity_type: "small_molecule"
name: "3'-UMP"
source_database: "KEGG"
source_id: "C01368"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3'-UMP"
  - "Uridine 3'-monophosphate"
  - "Uridine 3'-phosphate"
---

# 3'-UMP

`molecule.C01368`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01368`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3'-UMP; Uridine 3'-monophosphate; Uridine 3'-phosphate EcoCyc common name: uridine 3'-monophosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: 3'-UMP; Uridine 3'-monophosphate; Uridine 3'-phosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-14091|reaction.ecocyc.RXN-14091]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01877|reaction.R01877]] `KEGG` `database` - C01368 + C00001 <=> C00299 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14115|reaction.ecocyc.RXN-14115]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01368`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
