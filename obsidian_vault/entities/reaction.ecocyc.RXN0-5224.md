---
entity_id: "reaction.ecocyc.RXN0-5224"
entity_type: "reaction"
name: "RXN0-5224"
source_database: "EcoCyc"
source_id: "RXN0-5224"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5224

`reaction.ecocyc.RXN0-5224`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5224`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HCO3 + PROTON -> CARBON-DIOXIDE + WATER; direction=REVERSIBLE EcoCyc reaction equation: HCO3 + PROTON -> CARBON-DIOXIDE + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by carbonic anhydrase 1 (complex.ecocyc.CARBODEHYDRAT-CPLX), carbonic anhydrase 2 (complex.ecocyc.CPLX0-7521). Substrates: H+ (molecule.C00080), HCO3- (molecule.C00288). Products: H2O (molecule.C00001), CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.CYANCAT-PWY` cyanate degradation (EcoCyc)

## Annotation

HCO3 + PROTON -> CARBON-DIOXIDE + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.CYANCAT-PWY` cyanate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00780|molecule.C00780]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CARBODEHYDRAT-CPLX|complex.ecocyc.CARBODEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7521|complex.ecocyc.CPLX0-7521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1626|molecule.ecocyc.CPD0-1626]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5224`

## Notes

HCO3 + PROTON -> CARBON-DIOXIDE + WATER; direction=REVERSIBLE
