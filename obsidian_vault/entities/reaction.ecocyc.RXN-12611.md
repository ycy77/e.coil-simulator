---
entity_id: "reaction.ecocyc.RXN-12611"
entity_type: "reaction"
name: "thiamin phosphate synthase"
source_database: "EcoCyc"
source_id: "RXN-12611"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# thiamin phosphate synthase

`reaction.ecocyc.RXN-12611`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12611`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13575 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13575 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thiE (protein.P30137). Substrates: H+ (molecule.C00080), 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate (molecule.C04752), 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate (molecule.C20246). Products: CO2 (molecule.C00011), Diphosphate (molecule.C00013), Thiamin monophosphate (molecule.C01081).

## Enriched Pathways

- `ecocyc.PWY-6894` thiamine diphosphate biosynthesis I (E. coli) (EcoCyc)

## Annotation

CPD-13575 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6894` thiamine diphosphate biosynthesis I (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P30137|protein.P30137]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01081|molecule.C01081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04752|molecule.C04752]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20246|molecule.C20246]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12611`

## Notes

CPD-13575 + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + PROTON -> THIAMINE-P + CARBON-DIOXIDE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
