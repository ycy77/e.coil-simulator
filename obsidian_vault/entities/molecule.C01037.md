---
entity_id: "molecule.C01037"
entity_type: "small_molecule"
name: "7,8-Diaminononanoate"
source_database: "KEGG"
source_id: "C01037"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "7,8-Diaminononanoate"
  - "7,8-Diaminopelargonic acid"
  - "DAPA"
  - "7,8-Diaminononanoic acid"
---

# 7,8-Diaminononanoate

`molecule.C01037`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01037`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 7,8-Diaminononanoate; 7,8-Diaminopelargonic acid; DAPA; 7,8-Diaminononanoic acid EcoCyc common name: (7R,8S)-diaminononanoate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)

## Annotation

KEGG compound: 7,8-Diaminononanoate; 7,8-Diaminopelargonic acid; DAPA; 7,8-Diaminononanoic acid

## Pathways

- `eco00780` Biotin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.DAPASYN-RXN|reaction.ecocyc.DAPASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03182|reaction.R03182]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_substrate_of` --> [[reaction.ecocyc.DETHIOBIOTIN-SYN-RXN|reaction.ecocyc.DETHIOBIOTIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN1ZN3-9|reaction.ecocyc.RXN1ZN3-9]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01037`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
