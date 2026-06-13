---
entity_id: "molecule.C14145"
entity_type: "small_molecule"
name: "(3S)-3-Hydroxyadipyl-CoA"
source_database: "KEGG"
source_id: "C14145"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(3S)-3-Hydroxyadipyl-CoA"
---

# (3S)-3-Hydroxyadipyl-CoA

`molecule.C14145`

## Static

- Type: `small_molecule`
- Source: `KEGG:C14145`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (3S)-3-Hydroxyadipyl-CoA EcoCyc common name: (3S)-hydroxyadipyl-CoA.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00930` Caprolactam degradation (KEGG)

## Annotation

KEGG compound: (3S)-3-Hydroxyadipyl-CoA

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00930` Caprolactam degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R06942|reaction.R06942]] `KEGG` `database` - C14144 + C00001 <=> C14145
- `is_substrate_of` --> [[reaction.R06941|reaction.R06941]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-2425|reaction.ecocyc.RXN-2425]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2044|reaction.ecocyc.RXN0-2044]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C14145`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
