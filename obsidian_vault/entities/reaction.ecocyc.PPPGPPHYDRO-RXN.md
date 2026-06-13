---
entity_id: "reaction.ecocyc.PPPGPPHYDRO-RXN"
entity_type: "reaction"
name: "PPPGPPHYDRO-RXN"
source_database: "EcoCyc"
source_id: "PPPGPPHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PPPGPPHYDRO-RXN

`reaction.ecocyc.PPPGPPHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PPPGPPHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction pppGpp is converted to ppGpp. EcoCyc reaction equation: WATER + GDP-TP -> PROTON + Pi + GUANOSINE-5DP-3DP; direction=LEFT-TO-RIGHT. In this reaction pppGpp is converted to ppGpp.

## Biological Role

Catalyzed by guanosine-5'-triphosphate,3'-diphosphate phosphatase (complex.ecocyc.PPPGPPHYDRO-CPLX), apaH (protein.P05637). Substrates: H2O (molecule.C00001), Guanosine 3'-diphosphate 5'-triphosphate (molecule.C04494). Products: H+ (molecule.C00080), Guanosine 3',5'-bis(diphosphate) (molecule.C01228), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Annotation

In this reaction pppGpp is converted to ppGpp.

## Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.PPPGPPHYDRO-CPLX|complex.ecocyc.PPPGPPHYDRO-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P05637|protein.P05637]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1410|molecule.ecocyc.CPD0-1410]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NaF|molecule.ecocyc.NaF]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PPPGPPHYDRO-RXN`

## Notes

WATER + GDP-TP -> PROTON + Pi + GUANOSINE-5DP-3DP; direction=LEFT-TO-RIGHT
