---
entity_id: "molecule.C00429"
entity_type: "small_molecule"
name: "5,6-Dihydrouracil"
source_database: "KEGG"
source_id: "C00429"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5,6-Dihydrouracil"
  - "Dihydro-2,4(1H,3H)-pyrimidinedione"
  - "Dihydrouracile"
  - "Dihydrouracil"
  - "5,6-Dihydro-2,4-dihydroxypyrimidine"
  - "Hydrouracil"
  - "2,4-Dioxotetrahydropyrimidine"
---

# 5,6-Dihydrouracil

`molecule.C00429`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00429`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5,6-Dihydrouracil; Dihydro-2,4(1H,3H)-pyrimidinedione; Dihydrouracile; Dihydrouracil; 5,6-Dihydro-2,4-dihydroxypyrimidine; Hydrouracil; 2,4-Dioxotetrahydropyrimidine

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: 5,6-Dihydrouracil; Dihydro-2,4(1H,3H)-pyrimidinedione; Dihydrouracile; Dihydrouracil; 5,6-Dihydro-2,4-dihydroxypyrimidine; Hydrouracil; 2,4-Dioxotetrahydropyrimidine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R00977|reaction.R00977]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN|reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00429`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
