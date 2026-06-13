---
entity_id: "reaction.ecocyc.RXN-24036"
entity_type: "reaction"
name: "RXN-24036"
source_database: "EcoCyc"
source_id: "RXN-24036"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24036

`reaction.ecocyc.RXN-24036`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24036`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-Protein-L-Lysine + CPD-26594 -> Octanoylated-domains + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipoyl-Protein-L-Lysine + CPD-26594 -> Octanoylated-domains + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (octanoyl)adenylate (molecule.ecocyc.CPD-26594), a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine). Products: AMP (molecule.C00020), H+ (molecule.C00080), a [lipoyl-carrier protein] N6-octanoyl-L-lysine (molecule.ecocyc.Octanoylated-domains).

## Enriched Pathways

- `ecocyc.PWY0-1275` lipoate biosynthesis and incorporation II (EcoCyc)

## Annotation

Lipoyl-Protein-L-Lysine + CPD-26594 -> Octanoylated-domains + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1275` lipoate biosynthesis and incorporation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Octanoylated-domains|molecule.ecocyc.Octanoylated-domains]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26594|molecule.ecocyc.CPD-26594]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24036`

## Notes

Lipoyl-Protein-L-Lysine + CPD-26594 -> Octanoylated-domains + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
