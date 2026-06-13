---
entity_id: "reaction.ecocyc.TDPFUCACTRANS-RXN"
entity_type: "reaction"
name: "TDPFUCACTRANS-RXN"
source_database: "EcoCyc"
source_id: "TDPFUCACTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TDPFUCACTRANS-RXN

`reaction.ecocyc.TDPFUCACTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TDPFUCACTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in ECA biosynthesis. EcoCyc reaction equation: TDP-D-FUCOSAMINE + ACETYL-COA -> PROTON + TDP-FUC4NAC + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in ECA biosynthesis.

## Biological Role

Catalyzed by dTDP-4-amino-4,6-dideoxy-D-galactose acyltransferase (complex.ecocyc.CPLX0-8614). Substrates: Acetyl-CoA (molecule.C00024), dTDP-4-amino-4,6-dideoxy-D-galactose (molecule.C04346). Products: CoA (molecule.C00010), H+ (molecule.C00080), dTDP-4-acetamido-4,6-dideoxy-D-glucose (molecule.C06018).

## Enriched Pathways

- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Annotation

This is the second reaction in the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in ECA biosynthesis.

## Pathways

- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8614|complex.ecocyc.CPLX0-8614]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06018|molecule.C06018]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04346|molecule.C04346]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TDPFUCACTRANS-RXN`

## Notes

TDP-D-FUCOSAMINE + ACETYL-COA -> PROTON + TDP-FUC4NAC + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
