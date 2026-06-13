---
entity_id: "reaction.ecocyc.RXN-20919"
entity_type: "reaction"
name: "RXN-20919"
source_database: "EcoCyc"
source_id: "RXN-20919"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20919

`reaction.ecocyc.RXN-20919`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20919`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations. EcoCyc reaction equation: CPD-12817 + LIPID-IV-A -> CPD0-1281 + CPD-22538; direction=PHYSIOL-LEFT-TO-RIGHT. The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations.

## Biological Role

Catalyzed by pagP (protein.P37001). Substrates: 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate (molecule.C04919), 1,2-dipalmitoyl-phosphatidylserine (molecule.ecocyc.CPD-12817). Products: Lipid IVB (molecule.C21982), 2-palmitoyl-sn-glycero-3-phosphoserine (molecule.ecocyc.CPD-22538).

## Annotation

The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37001|protein.P37001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C21982|molecule.C21982]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22538|molecule.ecocyc.CPD-22538]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04919|molecule.C04919]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12817|molecule.ecocyc.CPD-12817]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20919`

## Notes

CPD-12817 + LIPID-IV-A -> CPD0-1281 + CPD-22538; direction=PHYSIOL-LEFT-TO-RIGHT
