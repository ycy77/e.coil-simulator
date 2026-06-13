---
entity_id: "molecule.C19946"
entity_type: "small_molecule"
name: "3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde"
source_database: "KEGG"
source_id: "C19946"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde"
---

# 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde

`molecule.C19946`

## Static

- Type: `small_molecule`
- Source: `KEGG:C19946`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde EcoCyc common name: 3-oxo-5,6-didehydrosuberyl-CoA semialdehyde.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXNMETA-12671|reaction.ecocyc.RXNMETA-12671]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R09820|reaction.R09820]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17752|reaction.ecocyc.RXN-17752]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXNMETA-12672|reaction.ecocyc.RXNMETA-12672]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C19946`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
