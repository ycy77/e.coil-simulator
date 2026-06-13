---
entity_id: "molecule.C01279"
entity_type: "small_molecule"
name: "4-Amino-5-hydroxymethyl-2-methylpyrimidine"
source_database: "KEGG"
source_id: "C01279"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Amino-5-hydroxymethyl-2-methylpyrimidine"
  - "Toxopyrimidine"
  - "4-Amino-2-methyl-5-pyrimidinemethanol"
  - "HMP"
---

# 4-Amino-5-hydroxymethyl-2-methylpyrimidine

`molecule.C01279`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01279`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Amino-5-hydroxymethyl-2-methylpyrimidine; Toxopyrimidine; 4-Amino-2-methyl-5-pyrimidinemethanol; HMP EcoCyc common name: 4-amino-2-methyl-5-pyrimidinemethanol. Merck index 9482

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: 4-Amino-5-hydroxymethyl-2-methylpyrimidine; Toxopyrimidine; 4-Amino-2-methyl-5-pyrimidinemethanol; HMP

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-462|reaction.ecocyc.TRANS-RXN0-462]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.OHMETPYRKIN-RXN|reaction.ecocyc.OHMETPYRKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-462|reaction.ecocyc.TRANS-RXN0-462]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PNKIN-RXN|reaction.ecocyc.PNKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01279`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
