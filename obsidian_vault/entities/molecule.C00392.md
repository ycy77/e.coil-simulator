---
entity_id: "molecule.C00392"
entity_type: "small_molecule"
name: "Mannitol"
source_database: "KEGG"
source_id: "C00392"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Mannitol"
  - "D-Mannitol"
---

# Mannitol

`molecule.C00392`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00392`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Mannitol; D-Mannitol EcoCyc common name: D-mannitol.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Mannitol; D-Mannitol

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN|reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-156|reaction.ecocyc.TRANS-RXN-156]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00392`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
