---
entity_id: "reaction.ecocyc.RXN0-947"
entity_type: "reaction"
name: "RXN0-947"
source_database: "EcoCyc"
source_id: "RXN0-947"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-947

`reaction.ecocyc.RXN0-947`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-947`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Octanoyl-ACPs + Lipoyl-Protein-L-Lysine -> Octanoylated-domains + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Octanoyl-ACPs + Lipoyl-Protein-L-Lysine -> Octanoylated-domains + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipB (protein.P60720). Substrates: a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine). Products: H+ (molecule.C00080), a [lipoyl-carrier protein] N6-octanoyl-L-lysine (molecule.ecocyc.Octanoylated-domains).

## Enriched Pathways

- `ecocyc.PWY0-501` lipoate biosynthesis and incorporation I (EcoCyc)

## Annotation

Octanoyl-ACPs + Lipoyl-Protein-L-Lysine -> Octanoylated-domains + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-501` lipoate biosynthesis and incorporation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P60720|protein.P60720]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Octanoylated-domains|molecule.ecocyc.Octanoylated-domains]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-947`

## Notes

Octanoyl-ACPs + Lipoyl-Protein-L-Lysine -> Octanoylated-domains + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
