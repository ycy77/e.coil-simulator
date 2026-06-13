---
entity_id: "molecule.C04895"
entity_type: "small_molecule"
name: "7,8-Dihydroneopterin 3'-triphosphate"
source_database: "KEGG"
source_id: "C04895"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "7,8-Dihydroneopterin 3'-triphosphate"
  - "2-Amino-4-hydroxy-6-(erythro-1,2,3-trihydroxypropyl)dihydropteridine triphosphate"
  - "6-(L-erythro-1,2-Dihydroxypropyl 3-triphosphate)-7,8-dihydropterin"
  - "6-[(1S,2R)-1,2-Dihydroxy-3-triphosphooxypropyl]-7,8-dihydropterin"
---

# 7,8-Dihydroneopterin 3'-triphosphate

`molecule.C04895`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04895`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 7,8-Dihydroneopterin 3'-triphosphate; 2-Amino-4-hydroxy-6-(erythro-1,2,3-trihydroxypropyl)dihydropteridine triphosphate; 6-(L-erythro-1,2-Dihydroxypropyl 3-triphosphate)-7,8-dihydropterin; 6-[(1S,2R)-1,2-Dihydroxy-3-triphosphooxypropyl]-7,8-dihydropterin

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 7,8-Dihydroneopterin 3'-triphosphate; 2-Amino-4-hydroxy-6-(erythro-1,2,3-trihydroxypropyl)dihydropteridine triphosphate; 6-(L-erythro-1,2-Dihydroxypropyl 3-triphosphate)-7,8-dihydropterin; 6-[(1S,2R)-1,2-Dihydroxy-3-triphosphooxypropyl]-7,8-dihydropterin

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00424|reaction.R00424]] `KEGG` `database` - C00044 + C00001 <=> C04895 + C00058
- `is_product_of` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN|reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.H2NTPEPIM-RXN|reaction.ecocyc.H2NTPEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5507|reaction.ecocyc.RXN0-5507]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04895`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
