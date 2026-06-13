---
entity_id: "molecule.C03287"
entity_type: "small_molecule"
name: "L-Glutamyl 5-phosphate"
source_database: "KEGG"
source_id: "C03287"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Glutamyl 5-phosphate"
  - "L-Glutamate 5-phosphate"
---

# L-Glutamyl 5-phosphate

`molecule.C03287`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03287`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Glutamyl 5-phosphate; L-Glutamate 5-phosphate EcoCyc common name: γ-L-glutamyl 5-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)

## Annotation

KEGG compound: L-Glutamyl 5-phosphate; L-Glutamate 5-phosphate

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00239|reaction.R00239]] `KEGG` `database` - C00002 + C00025 <=> C00008 + C03287
- `is_product_of` --> [[reaction.ecocyc.GLUTKIN-RXN|reaction.ecocyc.GLUTKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN|reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19022|reaction.ecocyc.RXN-19022]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03287`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
