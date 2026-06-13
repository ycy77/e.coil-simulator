---
entity_id: "reaction.ecocyc.P-PANTOCYSDECARB-RXN"
entity_type: "reaction"
name: "P-PANTOCYSDECARB-RXN"
source_database: "EcoCyc"
source_id: "P-PANTOCYSDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# P-PANTOCYSDECARB-RXN

`reaction.ecocyc.P-PANTOCYSDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:P-PANTOCYSDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in coenzyme A (CoA) biosynthesis. EcoCyc reaction equation: PROTON + R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE -> PANTETHEINE-P + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT. This is the third reaction in coenzyme A (CoA) biosynthesis.

## Biological Role

Catalyzed by fused 4'-phosphopantothenoylcysteine decarboxylase and phosphopantothenoylcysteine synthetase (complex.ecocyc.CPLX0-341). Substrates: H+ (molecule.C00080), (R)-4'-Phosphopantothenoyl-L-cysteine (molecule.C04352). Products: CO2 (molecule.C00011), Pantetheine 4'-phosphate (molecule.C01134).

## Enriched Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Annotation

This is the third reaction in coenzyme A (CoA) biosynthesis.

## Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-341|complex.ecocyc.CPLX0-341]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01134|molecule.C01134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04352|molecule.C04352]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:P-PANTOCYSDECARB-RXN`

## Notes

PROTON + R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE -> PANTETHEINE-P + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
