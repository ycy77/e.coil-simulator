---
entity_id: "reaction.ecocyc.RXN-16454"
entity_type: "reaction"
name: "RXN-16454"
source_database: "EcoCyc"
source_id: "RXN-16454"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16454

`reaction.ecocyc.RXN-16454`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16454`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Tyrosines + OXYGEN-MOLECULE -> TOPAQUINONE + HYDROGEN-PEROXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Tyrosines + OXYGEN-MOLECULE -> TOPAQUINONE + HYDROGEN-PEROXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), a [protein]-L-tyrosine (molecule.ecocyc.Protein-Tyrosines). Products: Hydrogen peroxide (molecule.C00027), H+ (molecule.C00080), topaquinone (molecule.ecocyc.TOPAQUINONE).

## Annotation

Protein-Tyrosines + OXYGEN-MOLECULE -> TOPAQUINONE + HYDROGEN-PEROXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TOPAQUINONE|molecule.ecocyc.TOPAQUINONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Tyrosines|molecule.ecocyc.Protein-Tyrosines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16454`

## Notes

Protein-Tyrosines + OXYGEN-MOLECULE -> TOPAQUINONE + HYDROGEN-PEROXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
