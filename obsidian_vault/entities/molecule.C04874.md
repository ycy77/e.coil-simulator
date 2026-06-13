---
entity_id: "molecule.C04874"
entity_type: "small_molecule"
name: "7,8-Dihydroneopterin"
source_database: "KEGG"
source_id: "C04874"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "7,8-Dihydroneopterin"
  - "Dihydroneopterin"
  - "2-Amino-4-hydroxy-6-(D-erythro-1,2,3-trihydroxypropyl)-7,8-dihydropteridine"
---

# 7,8-Dihydroneopterin

`molecule.C04874`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04874`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 7,8-Dihydroneopterin; Dihydroneopterin; 2-Amino-4-hydroxy-6-(D-erythro-1,2,3-trihydroxypropyl)-7,8-dihydropteridine EcoCyc common name: D-erythro-7,8-dihydroneopterin.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 7,8-Dihydroneopterin; Dihydroneopterin; 2-Amino-4-hydroxy-6-(D-erythro-1,2,3-trihydroxypropyl)-7,8-dihydropteridine

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN|reaction.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.H2NEOPTERINALDOL-RXN|reaction.ecocyc.H2NEOPTERINALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10856|reaction.ecocyc.RXN-10856]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04874`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
