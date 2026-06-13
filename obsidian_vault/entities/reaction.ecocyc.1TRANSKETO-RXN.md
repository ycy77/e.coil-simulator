---
entity_id: "reaction.ecocyc.1TRANSKETO-RXN"
entity_type: "reaction"
name: "1TRANSKETO-RXN"
source_database: "EcoCyc"
source_id: "1TRANSKETO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1TRANSKETO-RXN

`reaction.ecocyc.1TRANSKETO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1TRANSKETO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the pentose phosphate pathway. EcoCyc reaction equation: D-SEDOHEPTULOSE-7-P + GAP -> RIBOSE-5P + XYLULOSE-5-PHOSPHATE; direction=REVERSIBLE. This reaction is involved in the pentose phosphate pathway.

## Biological Role

Catalyzed by transketolase 2 (complex.ecocyc.CPLX0-1261), transketolase 1 (complex.ecocyc.TRANSKETOI-CPLX). Substrates: D-Glyceraldehyde 3-phosphate (molecule.C00118), Sedoheptulose 7-phosphate (molecule.C05382). Products: D-Ribose 5-phosphate (molecule.C00117), D-Xylulose 5-phosphate (molecule.C00231).

## Enriched Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Annotation

This reaction is involved in the pentose phosphate pathway.

## Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1261|complex.ecocyc.CPLX0-1261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANSKETOI-CPLX|complex.ecocyc.TRANSKETOI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00231|molecule.C00231]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01112|molecule.C01112]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2022|molecule.ecocyc.CPD0-2022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1TRANSKETO-RXN`

## Notes

D-SEDOHEPTULOSE-7-P + GAP -> RIBOSE-5P + XYLULOSE-5-PHOSPHATE; direction=REVERSIBLE
