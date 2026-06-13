---
entity_id: "reaction.ecocyc.RXN0-1141"
entity_type: "reaction"
name: "lipoate--GcvH protein ligase"
source_database: "EcoCyc"
source_id: "RXN0-1141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lipoate--GcvH protein ligase

`reaction.ecocyc.RXN0-1141`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1141`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Gcv-H + ATP + LIPOIC-ACID -> AMP + PPI + PROTEIN-LIPOYLLYSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Gcv-H + ATP + LIPOIC-ACID -> AMP + PPI + PROTEIN-LIPOYLLYSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: ATP (molecule.C00002), (R)-Lipoate (molecule.C16241), [glycine cleavage system lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Gcv-H). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a [glycine-cleavage complex H protein] N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.PROTEIN-LIPOYLLYSINE).

## Annotation

Gcv-H + ATP + LIPOIC-ACID -> AMP + PPI + PROTEIN-LIPOYLLYSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTEIN-LIPOYLLYSINE|molecule.ecocyc.PROTEIN-LIPOYLLYSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Gcv-H|molecule.ecocyc.Gcv-H]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1141`

## Notes

Gcv-H + ATP + LIPOIC-ACID -> AMP + PPI + PROTEIN-LIPOYLLYSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
