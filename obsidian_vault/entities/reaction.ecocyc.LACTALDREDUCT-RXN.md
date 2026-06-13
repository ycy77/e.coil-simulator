---
entity_id: "reaction.ecocyc.LACTALDREDUCT-RXN"
entity_type: "reaction"
name: "LACTALDREDUCT-RXN"
source_database: "EcoCyc"
source_id: "LACTALDREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LACTALDREDUCT-RXN

`reaction.ecocyc.LACTALDREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LACTALDREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduction of lactaldehyde. EcoCyc reaction equation: PROPANE-1-2-DIOL + NAD -> LACTALD + NADH + PROTON; direction=REVERSIBLE. Reduction of lactaldehyde.

## Biological Role

Catalyzed by lactaldehyde reductase (complex.ecocyc.LACTALDREDUCT-CPLX). Substrates: NAD+ (molecule.C00003), (S)-propane-1,2-diol (molecule.ecocyc.PROPANE-1-2-DIOL). Products: NADH (molecule.C00004), H+ (molecule.C00080), (S)-Lactaldehyde (molecule.C00424).

## Enriched Pathways

- `ecocyc.PWY0-1315` L-lactaldehyde degradation (anaerobic) (EcoCyc)

## Annotation

Reduction of lactaldehyde.

## Pathways

- `ecocyc.PWY0-1315` L-lactaldehyde degradation (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.LACTALDREDUCT-CPLX|complex.ecocyc.LACTALDREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROPANE-1-2-DIOL|molecule.ecocyc.PROPANE-1-2-DIOL]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1222|molecule.ecocyc.CPD0-1222]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1223|molecule.ecocyc.CPD0-1223]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PROPANE-1-2-DIOL|molecule.ecocyc.PROPANE-1-2-DIOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LACTALDREDUCT-RXN`

## Notes

PROPANE-1-2-DIOL + NAD -> LACTALD + NADH + PROTON; direction=REVERSIBLE
