---
entity_id: "reaction.ecocyc.2TRANSKETO-RXN"
entity_type: "reaction"
name: "2TRANSKETO-RXN"
source_database: "EcoCyc"
source_id: "2TRANSKETO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2TRANSKETO-RXN

`reaction.ecocyc.2TRANSKETO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2TRANSKETO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ERYTHROSE-4P + XYLULOSE-5-PHOSPHATE -> FRUCTOSE-6P + GAP; direction=REVERSIBLE EcoCyc reaction equation: ERYTHROSE-4P + XYLULOSE-5-PHOSPHATE -> FRUCTOSE-6P + GAP; direction=REVERSIBLE.

## Biological Role

Catalyzed by transketolase 2 (complex.ecocyc.CPLX0-1261), transketolase 1 (complex.ecocyc.TRANSKETOI-CPLX). Substrates: D-Xylulose 5-phosphate (molecule.C00231), D-Erythrose 4-phosphate (molecule.C00279). Products: D-Glyceraldehyde 3-phosphate (molecule.C00118), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Annotation

ERYTHROSE-4P + XYLULOSE-5-PHOSPHATE -> FRUCTOSE-6P + GAP; direction=REVERSIBLE

## Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1261|complex.ecocyc.CPLX0-1261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANSKETOI-CPLX|complex.ecocyc.TRANSKETOI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00231|molecule.C00231]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00279|molecule.C00279]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2TRANSKETO-RXN`

## Notes

ERYTHROSE-4P + XYLULOSE-5-PHOSPHATE -> FRUCTOSE-6P + GAP; direction=REVERSIBLE
