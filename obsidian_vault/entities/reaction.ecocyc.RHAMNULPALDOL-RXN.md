---
entity_id: "reaction.ecocyc.RHAMNULPALDOL-RXN"
entity_type: "reaction"
name: "RHAMNULPALDOL-RXN"
source_database: "EcoCyc"
source_id: "RHAMNULPALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RHAMNULPALDOL-RXN

`reaction.ecocyc.RHAMNULPALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RHAMNULPALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third step in L-rhamnose catabolism. EcoCyc reaction equation: RHAMNULOSE-1P -> LACTALD + DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE. The third step in L-rhamnose catabolism.

## Biological Role

Catalyzed by rhamnulose-1-phosphate aldolase (complex.ecocyc.RHAMNULPALDOL-CPLX). Substrates: L-Rhamnulose 1-phosphate (molecule.C01131). Products: Glycerone phosphate (molecule.C00111), (S)-Lactaldehyde (molecule.C00424).

## Enriched Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Annotation

The third step in L-rhamnose catabolism.

## Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.RHAMNULPALDOL-CPLX|complex.ecocyc.RHAMNULPALDOL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01131|molecule.C01131]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7388|molecule.ecocyc.CPD-7388]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8819|molecule.ecocyc.CPD-8819]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1286|molecule.ecocyc.CPD0-1286]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1288|molecule.ecocyc.CPD0-1288]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RHAMNULPALDOL-RXN`

## Notes

RHAMNULOSE-1P -> LACTALD + DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE
