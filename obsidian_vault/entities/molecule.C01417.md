---
entity_id: "molecule.C01417"
entity_type: "small_molecule"
name: "Cyanate"
source_database: "KEGG"
source_id: "C01417"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cyanate"
  - "Cyanic acid"
---

# Cyanate

`molecule.C01417`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01417`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cyanate; Cyanic acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Cyanate; Cyanic acid

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (11)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-164|complex.ecocyc.MONOMER0-164]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN-17753|reaction.ecocyc.RXN-17753]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-14|reaction.ecocyc.TRANS-RXN-14]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12893|reaction.ecocyc.RXN-12893]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-298|reaction.ecocyc.RXN0-298]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-14|reaction.ecocyc.TRANS-RXN-14]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3281|reaction.ecocyc.RXN0-3281]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5224|reaction.ecocyc.RXN0-5224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01417`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
