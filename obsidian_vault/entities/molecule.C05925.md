---
entity_id: "molecule.C05925"
entity_type: "small_molecule"
name: "Dihydroneopterin phosphate"
source_database: "KEGG"
source_id: "C05925"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dihydroneopterin phosphate"
  - "2-Amino-4-hydroxy-6-(erythro-1,2,3-trihydroxypropyl)dihydropteridine phosphate"
  - "7,8-Dihydroneopterin 3'-phosphate"
---

# Dihydroneopterin phosphate

`molecule.C05925`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05925`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dihydroneopterin phosphate; 2-Amino-4-hydroxy-6-(erythro-1,2,3-trihydroxypropyl)dihydropteridine phosphate; 7,8-Dihydroneopterin 3'-phosphate EcoCyc common name: 7,8-dihydroneopterin 3'-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: Dihydroneopterin phosphate; 2-Amino-4-hydroxy-6-(erythro-1,2,3-trihydroxypropyl)dihydropteridine phosphate; 7,8-Dihydroneopterin 3'-phosphate

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN|reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN|reaction.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN|reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05925`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
