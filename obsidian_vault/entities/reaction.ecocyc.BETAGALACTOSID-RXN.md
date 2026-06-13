---
entity_id: "reaction.ecocyc.BETAGALACTOSID-RXN"
entity_type: "reaction"
name: "BETAGALACTOSID-RXN"
source_database: "EcoCyc"
source_id: "BETAGALACTOSID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BETAGALACTOSID-RXN

`reaction.ecocyc.BETAGALACTOSID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BETAGALACTOSID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN|CCO-CYTOSOL

## Enriched Summary

Part of galactose, galactoside and glucose catabolism. EcoCyc reaction equation: CPD-15972 + WATER -> GALACTOSE + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT. Part of galactose, galactoside and glucose catabolism.

## Biological Role

Catalyzed by β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX), bglX (protein.P33363). Substrates: H2O (molecule.C00001), Lactose (molecule.C00243). Products: D-Glucose (molecule.C00031), β-D-galactopyranose (molecule.ecocyc.GALACTOSE).

## Enriched Pathways

- `ecocyc.BGALACT-PWY` lactose degradation III (EcoCyc)

## Annotation

Part of galactose, galactoside and glucose catabolism.

## Pathways

- `ecocyc.BGALACT-PWY` lactose degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (28)

- `catalyzes` <-- [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33363|protein.P33363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GALACTOSE__677c1dad|molecule.ecocyc.GALACTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01678|molecule.C01678]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05979|molecule.C05979]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.15-DIDEOXY-15-IMINO-D-GALACTITOL|molecule.ecocyc.15-DIDEOXY-15-IMINO-D-GALACTITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-AMINO-5-DEOXY-D-GALACTOPYRANOSIDE|molecule.ecocyc.5-AMINO-5-DEOXY-D-GALACTOPYRANOSIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-18165|molecule.ecocyc.CPD-18165]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3682|molecule.ecocyc.CPD-3682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1293|molecule.ecocyc.CPD0-1293]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1294|molecule.ecocyc.CPD0-1294]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1296|molecule.ecocyc.CPD0-1296]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1297|molecule.ecocyc.CPD0-1297]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1299|molecule.ecocyc.CPD0-1299]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1300|molecule.ecocyc.CPD0-1300]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1302|molecule.ecocyc.CPD0-1302]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1303|molecule.ecocyc.CPD0-1303]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1304|molecule.ecocyc.CPD0-1304]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1305|molecule.ecocyc.CPD0-1305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Chelators|molecule.ecocyc.Chelators]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.D-GALACTOSYLAMINE|molecule.ecocyc.D-GALACTOSYLAMINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.GALACTOSE__677c1dad|molecule.ecocyc.GALACTOSE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.RHg|molecule.ecocyc.RHg]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:BETAGALACTOSID-RXN`

## Notes

CPD-15972 + WATER -> GALACTOSE + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
