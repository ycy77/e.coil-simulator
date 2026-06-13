---
entity_id: "molecule.C01100"
entity_type: "small_molecule"
name: "L-Histidinol phosphate"
source_database: "KEGG"
source_id: "C01100"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Histidinol phosphate"
---

# L-Histidinol phosphate

`molecule.C01100`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01100`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Histidinol phosphate

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: L-Histidinol phosphate

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.HISTAMINOTRANS-RXN|reaction.ecocyc.HISTAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HISTIDPHOS-RXN|reaction.ecocyc.HISTIDPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-4361|reaction.ecocyc.RXN0-4361]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01100`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
