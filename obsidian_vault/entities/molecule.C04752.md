---
entity_id: "molecule.C04752"
entity_type: "small_molecule"
name: "4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate"
source_database: "KEGG"
source_id: "C04752"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate"
  - "4-Amino-2-methyl-5-(diphosphooxymethyl)pyrimidine"
  - "HMP-PP"
---

# 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate

`molecule.C04752`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04752`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate; 4-Amino-2-methyl-5-(diphosphooxymethyl)pyrimidine; HMP-PP EcoCyc common name: 4-amino-2-methyl-5-(diphosphooxymethyl)pyrimidine.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Annotation

KEGG compound: 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate; 4-Amino-2-methyl-5-(diphosphooxymethyl)pyrimidine; HMP-PP

## Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.PYRIMSYN3-RXN|reaction.ecocyc.PYRIMSYN3-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12610|reaction.ecocyc.RXN-12610]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12611|reaction.ecocyc.RXN-12611]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3543|reaction.ecocyc.RXN0-3543]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04752`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
