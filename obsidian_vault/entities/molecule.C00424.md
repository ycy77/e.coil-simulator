---
entity_id: "molecule.C00424"
entity_type: "small_molecule"
name: "(S)-Lactaldehyde"
source_database: "KEGG"
source_id: "C00424"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Lactaldehyde"
  - "L-Lactaldehyde"
  - "L-2-Hydroxypropionaldehyde"
---

# (S)-Lactaldehyde

`molecule.C00424`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00424`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Lactaldehyde; L-Lactaldehyde; L-2-Hydroxypropionaldehyde

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: (S)-Lactaldehyde; L-Lactaldehyde; L-2-Hydroxypropionaldehyde

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.FUCPALDOL-RXN|reaction.ecocyc.FUCPALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.LACTALDREDUCT-RXN|reaction.ecocyc.LACTALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RHAMNULPALDOL-RXN|reaction.ecocyc.RHAMNULPALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15744|reaction.ecocyc.RXN-15744]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5433|reaction.ecocyc.RXN0-5433]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.283-RXN|reaction.ecocyc.1.1.1.283-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LACTALDDEHYDROG-RXN|reaction.ecocyc.LACTALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.LACTALDDEHYDROG-RXN|reaction.ecocyc.LACTALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00424`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
