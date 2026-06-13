---
entity_id: "molecule.C00474"
entity_type: "small_molecule"
name: "Ribitol"
source_database: "KEGG"
source_id: "C00474"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ribitol"
  - "Adonitol"
---

# Ribitol

`molecule.C00474`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00474`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ribitol; Adonitol

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: Ribitol; Adonitol

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN|reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ARABISOM-RXN|reaction.ecocyc.ARABISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DARABISOM-RXN|reaction.ecocyc.DARABISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00474`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
