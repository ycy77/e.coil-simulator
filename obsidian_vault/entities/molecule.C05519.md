---
entity_id: "molecule.C05519"
entity_type: "small_molecule"
name: "L-Allothreonine"
source_database: "KEGG"
source_id: "C05519"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Allothreonine"
  - "L-allo-Threonine"
---

# L-Allothreonine

`molecule.C05519`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05519`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Allothreonine; L-allo-Threonine EcoCyc common name: L-allo-threonine.

## Biological Role

Consumed as substrate in 5 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)

## Annotation

KEGG compound: L-Allothreonine; L-allo-Threonine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)

## Outgoing Edges (5)

- `is_substrate_of` --> [[reaction.R06171|reaction.R06171]] `KEGG` `database` - C05519 <=> C00037 + C00084
- `is_substrate_of` --> [[reaction.R10852|reaction.R10852]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.LTAA-RXN|reaction.ecocyc.LTAA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16000|reaction.ecocyc.RXN-16000]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16001|reaction.ecocyc.RXN-16001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05519`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
