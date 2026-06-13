---
entity_id: "reaction.ecocyc.KDGALDOL-RXN"
entity_type: "reaction"
name: "KDGALDOL-RXN"
source_database: "EcoCyc"
source_id: "KDGALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDGALDOL-RXN

`reaction.ecocyc.KDGALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDGALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the catabolism of both glucarate and galactarate. EcoCyc reaction equation: 5-KETO-4-DEOXY-D-GLUCARATE -> CPD-26279 + PYRUVATE; direction=REVERSIBLE. This is the second reaction in the catabolism of both glucarate and galactarate.

## Biological Role

Catalyzed by α-dehydro-β-deoxy-D-glucarate aldolase (complex.ecocyc.CPLX0-7615). Substrates: 5-Dehydro-4-deoxy-D-glucarate (molecule.C00679). Products: Pyruvate (molecule.C00022), (2R)-tartronate semialdehyde (molecule.ecocyc.CPD-26279).

## Enriched Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)
- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)

## Annotation

This is the second reaction in the catabolism of both glucarate and galactarate.

## Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)
- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (24)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7615|complex.ecocyc.CPLX0-7615]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26279|molecule.ecocyc.CPD-26279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00679|molecule.C00679]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00818|molecule.C00818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00879|molecule.C00879]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04442|molecule.C04442]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06473|molecule.C06473]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BR-|molecule.ecocyc.BR-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1506|molecule.ecocyc.CPD0-1506]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Hexaric-Acids|molecule.ecocyc.Hexaric-Acids]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Hexonic-Acids|molecule.ecocyc.Hexonic-Acids]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Hexuronates|molecule.ecocyc.Hexuronates]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.KDO|molecule.ecocyc.KDO]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pentaric-Acids|molecule.ecocyc.Pentaric-Acids]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Tetraric-Acids|molecule.ecocyc.Tetraric-Acids]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Xylarates|molecule.ecocyc.Xylarates]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KDGALDOL-RXN`

## Notes

5-KETO-4-DEOXY-D-GLUCARATE -> CPD-26279 + PYRUVATE; direction=REVERSIBLE
