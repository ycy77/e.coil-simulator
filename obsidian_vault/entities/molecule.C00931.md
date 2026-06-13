---
entity_id: "molecule.C00931"
entity_type: "small_molecule"
name: "Porphobilinogen"
source_database: "KEGG"
source_id: "C00931"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Porphobilinogen"
---

# Porphobilinogen

`molecule.C00931`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00931`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Porphobilinogen

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Porphobilinogen

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R00036|reaction.R00036]] `KEGG` `database` - 2 C00430 <=> C00931 + 2 C00001
- `is_product_of` --> [[reaction.ecocyc.PORPHOBILSYNTH-RXN|reaction.ecocyc.PORPHOBILSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00084|reaction.R00084]] `KEGG` `database` - 4 C00931 + C00001 <=> C01024 + 4 C00014
- `is_substrate_of` --> [[reaction.ecocyc.OHMETHYLBILANESYN-RXN|reaction.ecocyc.OHMETHYLBILANESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21523|reaction.ecocyc.RXN-21523]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21524|reaction.ecocyc.RXN-21524]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21526|reaction.ecocyc.RXN-21526]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21527|reaction.ecocyc.RXN-21527]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00931`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
