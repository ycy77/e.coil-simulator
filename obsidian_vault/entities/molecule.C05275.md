---
entity_id: "molecule.C05275"
entity_type: "small_molecule"
name: "trans-Dec-2-enoyl-CoA"
source_database: "KEGG"
source_id: "C05275"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans-Dec-2-enoyl-CoA"
  - "(2E)-Decenoyl-CoA"
---

# trans-Dec-2-enoyl-CoA

`molecule.C05275`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05275`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans-Dec-2-enoyl-CoA; (2E)-Decenoyl-CoA EcoCyc common name: (2E)-dec-2-enoyl-CoA.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Annotation

KEGG compound: trans-Dec-2-enoyl-CoA; (2E)-Decenoyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-13615|reaction.ecocyc.RXN-13615]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13616|reaction.ecocyc.RXN-13616]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIENOYLCOAREDUCT-RXN|reaction.ecocyc.DIENOYLCOAREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05275`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
