---
entity_id: "molecule.C01103"
entity_type: "small_molecule"
name: "Orotidine 5'-phosphate"
source_database: "KEGG"
source_id: "C01103"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Orotidine 5'-phosphate"
  - "Orotidylic acid"
---

# Orotidine 5'-phosphate

`molecule.C01103`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01103`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Orotidine 5'-phosphate; Orotidylic acid

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Orotidine 5'-phosphate; Orotidylic acid

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.OROPRIBTRANS-RXN|reaction.ecocyc.OROPRIBTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.OROTPDECARB-RXN|reaction.ecocyc.OROTPDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01103`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
