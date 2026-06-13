---
entity_id: "reaction.ecocyc.RXN-17631"
entity_type: "reaction"
name: "RXN-17631"
source_database: "EcoCyc"
source_id: "RXN-17631"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17631

`reaction.ecocyc.RXN-17631`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17631`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

METHYL-GLYOXAL + Protein-L-lysine -> Protein-Lysine-Aminocarbinol + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: METHYL-GLYOXAL + Protein-L-lysine -> Protein-Lysine-Aminocarbinol + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Methylglyoxal (molecule.C00546), Protein lysine (molecule.C02188). Products: H+ (molecule.C00080), an N6-(1-hydroxy-2-oxopropyl)-[protein]-L-lysine (molecule.ecocyc.Protein-Lysine-Aminocarbinol).

## Annotation

METHYL-GLYOXAL + Protein-L-lysine -> Protein-Lysine-Aminocarbinol + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Lysine-Aminocarbinol|molecule.ecocyc.Protein-Lysine-Aminocarbinol]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17631`

## Notes

METHYL-GLYOXAL + Protein-L-lysine -> Protein-Lysine-Aminocarbinol + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
