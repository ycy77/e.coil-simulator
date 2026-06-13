---
entity_id: "reaction.ecocyc.RXN0-1138"
entity_type: "reaction"
name: "RXN0-1138"
source_database: "EcoCyc"
source_id: "RXN0-1138"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1138

`reaction.ecocyc.RXN0-1138`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1138`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Gcv-H + Lipoyl-ACPs -> PROTEIN-LIPOYLLYSINE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Gcv-H + Lipoyl-ACPs -> PROTEIN-LIPOYLLYSINE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipB (protein.P60720). Substrates: [glycine cleavage system lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Gcv-H). Products: H+ (molecule.C00080), a [glycine-cleavage complex H protein] N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.PROTEIN-LIPOYLLYSINE).

## Annotation

Gcv-H + Lipoyl-ACPs -> PROTEIN-LIPOYLLYSINE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P60720|protein.P60720]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTEIN-LIPOYLLYSINE|molecule.ecocyc.PROTEIN-LIPOYLLYSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Gcv-H|molecule.ecocyc.Gcv-H]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1138`

## Notes

Gcv-H + Lipoyl-ACPs -> PROTEIN-LIPOYLLYSINE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
