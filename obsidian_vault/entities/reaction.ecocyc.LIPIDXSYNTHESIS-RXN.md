---
entity_id: "reaction.ecocyc.LIPIDXSYNTHESIS-RXN"
entity_type: "reaction"
name: "LIPIDXSYNTHESIS-RXN"
source_database: "EcoCyc"
source_id: "LIPIDXSYNTHESIS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LIPIDXSYNTHESIS-RXN

`reaction.ecocyc.LIPIDXSYNTHESIS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LIPIDXSYNTHESIS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + OH-MYRISTOYL -> PROTON + BISOHMYR-GLUCOSAMINYL-1P + UMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + OH-MYRISTOYL -> PROTON + BISOHMYR-GLUCOSAMINYL-1P + UMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxH (protein.P43341). Substrates: H2O (molecule.C00001), UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine (molecule.C04652). Products: H+ (molecule.C00080), UMP (molecule.C00105), Lipid X (molecule.C04824).

## Enriched Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Annotation

WATER + OH-MYRISTOYL -> PROTON + BISOHMYR-GLUCOSAMINYL-1P + UMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P43341|protein.P43341]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04824|molecule.C04824]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04652|molecule.C04652]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2659|molecule.ecocyc.CPD0-2659]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LIPIDXSYNTHESIS-RXN`

## Notes

WATER + OH-MYRISTOYL -> PROTON + BISOHMYR-GLUCOSAMINYL-1P + UMP; direction=PHYSIOL-LEFT-TO-RIGHT
