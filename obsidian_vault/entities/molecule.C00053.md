---
entity_id: "molecule.C00053"
entity_type: "small_molecule"
name: "3'-Phosphoadenylyl sulfate"
source_database: "KEGG"
source_id: "C00053"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3'-Phosphoadenylyl sulfate"
  - "3'-Phosphoadenosine 5'-phosphosulfate"
  - "3'-Phospho-5'-adenylyl sulfate"
  - "PAPS"
---

# 3'-Phosphoadenylyl sulfate

`molecule.C00053`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00053`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3'-Phosphoadenylyl sulfate; 3'-Phosphoadenosine 5'-phosphosulfate; 3'-Phospho-5'-adenylyl sulfate; PAPS EcoCyc common name: 3'-phosphoadenylyl-sulfate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: 3'-Phosphoadenylyl sulfate; 3'-Phosphoadenosine 5'-phosphosulfate; 3'-Phospho-5'-adenylyl sulfate; PAPS

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00509|reaction.R00509]] `KEGG` `database` - C00002 + C00224 <=> C00008 + C00053
- `is_product_of` --> [[reaction.ecocyc.1.8.4.8-RXN|reaction.ecocyc.1.8.4.8-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ADENYLYLSULFKIN-RXN|reaction.ecocyc.ADENYLYLSULFKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00508|reaction.R00508]] `KEGG` `database` - C00053 + C00001 <=> C00224 + C00009
- `represses` --> [[reaction.ecocyc.ADENYLYLSULFKIN-RXN|reaction.ecocyc.ADENYLYLSULFKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00053`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
