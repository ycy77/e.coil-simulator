---
entity_id: "molecule.C01092"
entity_type: "small_molecule"
name: "8-Amino-7-oxononanoate"
source_database: "KEGG"
source_id: "C01092"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "8-Amino-7-oxononanoate"
  - "8-Amino-7-oxononanoic acid"
  - "7-Keto-8-aminopelargonic acid"
  - "KAPA"
---

# 8-Amino-7-oxononanoate

`molecule.C01092`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01092`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 8-Amino-7-oxononanoate; 8-Amino-7-oxononanoic acid; 7-Keto-8-aminopelargonic acid; KAPA EcoCyc common name: (8S)-8-amino-7-oxononanoate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)

## Annotation

KEGG compound: 8-Amino-7-oxononanoate; 8-Amino-7-oxononanoic acid; 7-Keto-8-aminopelargonic acid; KAPA

## Pathways

- `eco00780` Biotin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.7KAPSYN-RXN|reaction.ecocyc.7KAPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11484|reaction.ecocyc.RXN-11484]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DAPASYN-RXN|reaction.ecocyc.DAPASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DAPASYN-RXN|reaction.ecocyc.DAPASYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01092`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
