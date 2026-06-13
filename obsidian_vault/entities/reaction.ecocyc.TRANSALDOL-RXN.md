---
entity_id: "reaction.ecocyc.TRANSALDOL-RXN"
entity_type: "reaction"
name: "TRANSALDOL-RXN"
source_database: "EcoCyc"
source_id: "TRANSALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANSALDOL-RXN

`reaction.ecocyc.TRANSALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANSALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pentose-phosphate pathway. EcoCyc reaction equation: D-SEDOHEPTULOSE-7-P + GAP -> FRUCTOSE-6P + ERYTHROSE-4P; direction=REVERSIBLE. This reaction is part of the pentose-phosphate pathway.

## Biological Role

Catalyzed by transaldolase B (complex.ecocyc.TRANSALDOLB-CPLX), talA (protein.P0A867). Substrates: D-Glyceraldehyde 3-phosphate (molecule.C00118), Sedoheptulose 7-phosphate (molecule.C05382). Products: D-Erythrose 4-phosphate (molecule.C00279), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Annotation

This reaction is part of the pentose-phosphate pathway.

## Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.TRANSALDOLB-CPLX|complex.ecocyc.TRANSALDOLB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A867|protein.P0A867]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00279|molecule.C00279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01112|molecule.C01112]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02426|molecule.C02426]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.TRIS|molecule.ecocyc.TRIS]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANSALDOL-RXN`

## Notes

D-SEDOHEPTULOSE-7-P + GAP -> FRUCTOSE-6P + ERYTHROSE-4P; direction=REVERSIBLE
