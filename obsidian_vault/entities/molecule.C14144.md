---
entity_id: "molecule.C14144"
entity_type: "small_molecule"
name: "5-Carboxy-2-pentenoyl-CoA"
source_database: "KEGG"
source_id: "C14144"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Carboxy-2-pentenoyl-CoA"
  - "2,3-Didehydroadipyl-CoA"
---

# 5-Carboxy-2-pentenoyl-CoA

`molecule.C14144`

## Static

- Type: `small_molecule`
- Source: `KEGG:C14144`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Carboxy-2-pentenoyl-CoA; 2,3-Didehydroadipyl-CoA EcoCyc common name: (2E)-5-carboxy-2-pentenoyl-CoA.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)

## Annotation

KEGG compound: 5-Carboxy-2-pentenoyl-CoA; 2,3-Didehydroadipyl-CoA

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-2425|reaction.ecocyc.RXN-2425]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R06942|reaction.R06942]] `KEGG` `database` - C14144 + C00001 <=> C14145
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6512|reaction.ecocyc.RXN0-6512]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C14144`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
