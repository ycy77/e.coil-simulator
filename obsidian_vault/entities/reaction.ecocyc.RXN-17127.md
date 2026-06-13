---
entity_id: "reaction.ecocyc.RXN-17127"
entity_type: "reaction"
name: "RXN-17127"
source_database: "EcoCyc"
source_id: "RXN-17127"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17127

`reaction.ecocyc.RXN-17127`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17127`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-Protein-L-Lysine + LIPOIC-ACID + ATP -> Lipoyl-Protein-N6-lipoyllysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipoyl-Protein-L-Lysine + LIPOIC-ACID + ATP -> Lipoyl-Protein-N6-lipoyllysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: ATP (molecule.C00002), (R)-Lipoate (molecule.C16241), a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a [lipoyl-carrier protein]-N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine).

## Annotation

Lipoyl-Protein-L-Lysine + LIPOIC-ACID + ATP -> Lipoyl-Protein-N6-lipoyllysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine|molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.LIPOL-AMP|molecule.ecocyc.LIPOL-AMP]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-17127`

## Notes

Lipoyl-Protein-L-Lysine + LIPOIC-ACID + ATP -> Lipoyl-Protein-N6-lipoyllysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
