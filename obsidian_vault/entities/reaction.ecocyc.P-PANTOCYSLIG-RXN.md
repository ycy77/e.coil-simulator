---
entity_id: "reaction.ecocyc.P-PANTOCYSLIG-RXN"
entity_type: "reaction"
name: "P-PANTOCYSLIG-RXN"
source_database: "EcoCyc"
source_id: "P-PANTOCYSLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# P-PANTOCYSLIG-RXN

`reaction.ecocyc.P-PANTOCYSLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:P-PANTOCYSLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in coenzyme A (CoA) biosynthesis. EcoCyc reaction equation: 4-P-PANTOTHENATE + CYS + CTP -> PROTON + PPI + CMP + R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in coenzyme A (CoA) biosynthesis.

## Biological Role

Catalyzed by fused 4'-phosphopantothenoylcysteine decarboxylase and phosphopantothenoylcysteine synthetase (complex.ecocyc.CPLX0-341). Substrates: CTP (molecule.C00063), L-Cysteine (molecule.C00097), D-4'-Phosphopantothenate (molecule.C03492). Products: Diphosphate (molecule.C00013), CMP (molecule.C00055), H+ (molecule.C00080), (R)-4'-Phosphopantothenoyl-L-cysteine (molecule.C04352).

## Enriched Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Annotation

This is the second reaction in coenzyme A (CoA) biosynthesis.

## Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-341|complex.ecocyc.CPLX0-341]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04352|molecule.C04352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03492|molecule.C03492]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C03492|molecule.C03492]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:P-PANTOCYSLIG-RXN`

## Notes

4-P-PANTOTHENATE + CYS + CTP -> PROTON + PPI + CMP + R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE; direction=PHYSIOL-LEFT-TO-RIGHT
