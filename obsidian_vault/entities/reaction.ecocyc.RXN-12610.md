---
entity_id: "reaction.ecocyc.RXN-12610"
entity_type: "reaction"
name: "RXN-12610"
source_database: "EcoCyc"
source_id: "RXN-12610"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12610

`reaction.ecocyc.RXN-12610`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12610`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13576 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13576 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thiE (protein.P30137). Substrates: H+ (molecule.C00080), 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate (molecule.C04752), 2-(2-Carboxy-4-methylthiazol-5-yl)ethyl phosphate (molecule.C20247). Products: CO2 (molecule.C00011), Diphosphate (molecule.C00013), Thiamin monophosphate (molecule.C01081).

## Enriched Pathways

- `ecocyc.PWY-8457` thiamine diphosphate salvage V (EcoCyc)

## Annotation

CPD-13576 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8457` thiamine diphosphate salvage V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P30137|protein.P30137]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01081|molecule.C01081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04752|molecule.C04752]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20247|molecule.C20247]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12610`

## Notes

CPD-13576 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
