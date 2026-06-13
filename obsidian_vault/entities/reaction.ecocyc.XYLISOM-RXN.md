---
entity_id: "reaction.ecocyc.XYLISOM-RXN"
entity_type: "reaction"
name: "XYLISOM-RXN"
source_database: "EcoCyc"
source_id: "XYLISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# XYLISOM-RXN

`reaction.ecocyc.XYLISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:XYLISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Catabolism of xylose. Some enzymes also convert D-glucose to D-fructose. EcoCyc reaction equation: CPD-25028 -> CPD-24961; direction=REVERSIBLE. Catabolism of xylose. Some enzymes also convert D-glucose to D-fructose.

## Biological Role

Catalyzed by xylose isomerase (complex.ecocyc.XYLISOM-CPLX). Substrates: α-D-xylopyranose (molecule.ecocyc.CPD-25028). Products: α-D-xylulofuranose (molecule.ecocyc.CPD-24961).

## Enriched Pathways

- `ecocyc.XYLCAT-PWY` D-xylose degradation I (EcoCyc)

## Annotation

Catabolism of xylose. Some enzymes also convert D-glucose to D-fructose.

## Pathways

- `ecocyc.XYLCAT-PWY` D-xylose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.XYLISOM-CPLX|complex.ecocyc.XYLISOM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-24961|molecule.ecocyc.CPD-24961]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-25028|molecule.ecocyc.CPD-25028]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:XYLISOM-RXN`

## Notes

CPD-25028 -> CPD-24961; direction=REVERSIBLE
