---
entity_id: "molecule.C00860"
entity_type: "small_molecule"
name: "L-Histidinol"
source_database: "KEGG"
source_id: "C00860"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Histidinol"
---

# L-Histidinol

`molecule.C00860`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00860`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Histidinol EcoCyc common name: histidinol.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: L-Histidinol

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.HISTIDPHOS-RXN|reaction.ecocyc.HISTIDPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01158|reaction.R01158]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_substrate_of` --> [[reaction.ecocyc.HISTOLDEHYD-RXN|reaction.ecocyc.HISTOLDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8001|reaction.ecocyc.RXN-8001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN|reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HISTIDPHOS-RXN|reaction.ecocyc.HISTIDPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00860`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
