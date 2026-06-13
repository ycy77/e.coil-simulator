---
entity_id: "reaction.ecocyc.RXN-13031"
entity_type: "reaction"
name: "RXN-13031"
source_database: "EcoCyc"
source_id: "RXN-13031"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13031

`reaction.ecocyc.RXN-13031`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13031`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-Protein-N6-lipoyllysine + WATER -> Lipoyl-Protein-L-Lysine + LIPOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipoyl-Protein-N6-lipoyllysine + WATER -> Lipoyl-Protein-L-Lysine + LIPOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a [lipoyl-carrier protein]-N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine). Products: (R)-Lipoate (molecule.C16241), a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine).

## Annotation

Lipoyl-Protein-N6-lipoyllysine + WATER -> Lipoyl-Protein-L-Lysine + LIPOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine|molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13031`

## Notes

Lipoyl-Protein-N6-lipoyllysine + WATER -> Lipoyl-Protein-L-Lysine + LIPOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT
