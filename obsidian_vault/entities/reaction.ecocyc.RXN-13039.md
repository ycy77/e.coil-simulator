---
entity_id: "reaction.ecocyc.RXN-13039"
entity_type: "reaction"
name: "RXN-13039"
source_database: "EcoCyc"
source_id: "RXN-13039"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13039

`reaction.ecocyc.RXN-13039`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13039`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LIPOYL-AMP + Gcv-H -> PROTEIN-LIPOYLLYSINE + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LIPOYL-AMP + Gcv-H -> PROTEIN-LIPOYLLYSINE + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Lipoyl-AMP (molecule.C16238), [glycine cleavage system lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Gcv-H). Products: AMP (molecule.C00020), H+ (molecule.C00080), a [glycine-cleavage complex H protein] N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.PROTEIN-LIPOYLLYSINE).

## Annotation

LIPOYL-AMP + Gcv-H -> PROTEIN-LIPOYLLYSINE + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTEIN-LIPOYLLYSINE|molecule.ecocyc.PROTEIN-LIPOYLLYSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16238|molecule.C16238]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Gcv-H|molecule.ecocyc.Gcv-H]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13039`

## Notes

LIPOYL-AMP + Gcv-H -> PROTEIN-LIPOYLLYSINE + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
