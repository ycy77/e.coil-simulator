---
entity_id: "reaction.ecocyc.CARBPSYN-RXN"
entity_type: "reaction"
name: "CARBPSYN-RXN"
source_database: "EcoCyc"
source_id: "CARBPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CARBPSYN-RXN

`reaction.ecocyc.CARBPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CARBPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reaction is involved in both arginine and pyrimidine biosynthesis. Constitutes the first step of pyrimidine synthesis. EcoCyc reaction equation: ATP + GLN + HCO3 + WATER -> PROTON + CARBAMOYL-P + GLT + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. The reaction is involved in both arginine and pyrimidine biosynthesis. Constitutes the first step of pyrimidine synthesis.

## Biological Role

Catalyzed by carbamoyl-phosphate synthetase, glutamine-hydrolyzing (complex.ecocyc.CARBPSYN-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), L-Glutamate (molecule.C00025), H+ (molecule.C00080), Carbamoyl phosphate (molecule.C00169), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)
- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Annotation

The reaction is involved in both arginine and pyrimidine biosynthesis. Constitutes the first step of pyrimidine synthesis.

## Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)
- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (20)

- `activates` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CARBPSYN-CPLX|complex.ecocyc.CARBPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1036|molecule.ecocyc.CPD0-1036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1224|molecule.ecocyc.CPD0-1224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1627|molecule.ecocyc.CPD0-1627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-AZASERINE|molecule.ecocyc.L-AZASERINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CARBPSYN-RXN`

## Notes

ATP + GLN + HCO3 + WATER -> PROTON + CARBAMOYL-P + GLT + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
