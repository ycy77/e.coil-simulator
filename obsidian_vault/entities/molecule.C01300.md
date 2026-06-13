---
entity_id: "molecule.C01300"
entity_type: "small_molecule"
name: "6-(Hydroxymethyl)-7,8-dihydropterin"
source_database: "KEGG"
source_id: "C01300"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "6-(Hydroxymethyl)-7,8-dihydropterin"
  - "6-Hydroxymethyl-7,8-dihydropterin"
  - "2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine"
---

# 6-(Hydroxymethyl)-7,8-dihydropterin

`molecule.C01300`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01300`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 6-(Hydroxymethyl)-7,8-dihydropterin; 6-Hydroxymethyl-7,8-dihydropterin; 2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 6-(Hydroxymethyl)-7,8-dihydropterin; 6-Hydroxymethyl-7,8-dihydropterin; 2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.H2NEOPTERINALDOL-RXN|reaction.ecocyc.H2NEOPTERINALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN|reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01300`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
