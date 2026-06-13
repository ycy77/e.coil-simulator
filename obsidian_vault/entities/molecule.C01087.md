---
entity_id: "molecule.C01087"
entity_type: "small_molecule"
name: "(R)-2-Hydroxyglutarate"
source_database: "KEGG"
source_id: "C01087"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-2-Hydroxyglutarate"
  - "(R)-Hydroxyglutarate"
---

# (R)-2-Hydroxyglutarate

`molecule.C01087`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01087`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-2-Hydroxyglutarate; (R)-Hydroxyglutarate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)

## Annotation

KEGG compound: (R)-2-Hydroxyglutarate; (R)-Hydroxyglutarate

## Pathways

- `eco00310` Lysine degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R13011|reaction.R13011]] `KEGG` `database` - C00322 + C00007 <=> C01087 + C00011
- `is_substrate_of` --> [[reaction.R11337|reaction.R11337]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14932|reaction.ecocyc.RXN-14932]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01087`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
