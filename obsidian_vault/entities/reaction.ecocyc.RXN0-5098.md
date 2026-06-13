---
entity_id: "reaction.ecocyc.RXN0-5098"
entity_type: "reaction"
name: "RXN0-5098"
source_database: "EcoCyc"
source_id: "RXN0-5098"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5098

`reaction.ecocyc.RXN0-5098`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5098`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-Protein-L-Lysine + CPD-195 + ATP -> Octanoylated-domains + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipoyl-Protein-L-Lysine + CPD-195 + ATP -> Octanoylated-domains + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: ATP (molecule.C00002), Octanoic acid (molecule.C06423), a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a [lipoyl-carrier protein] N6-octanoyl-L-lysine (molecule.ecocyc.Octanoylated-domains).

## Annotation

Lipoyl-Protein-L-Lysine + CPD-195 + ATP -> Octanoylated-domains + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Octanoylated-domains|molecule.ecocyc.Octanoylated-domains]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06423|molecule.C06423]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5098`

## Notes

Lipoyl-Protein-L-Lysine + CPD-195 + ATP -> Octanoylated-domains + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
