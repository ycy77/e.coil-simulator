---
entity_id: "reaction.ecocyc.DXPREDISOM-RXN"
entity_type: "reaction"
name: "DXPREDISOM-RXN"
source_database: "EcoCyc"
source_id: "DXPREDISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DXPREDISOM-RXN

`reaction.ecocyc.DXPREDISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DXPREDISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the mevalonate-independent isopentenyl diphosphate (IPP) biosynthetic pathway. EcoCyc reaction equation: 2-C-METHYL-D-ERYTHRITOL-4-PHOSPHATE + NADP -> PROTON + DEOXYXYLULOSE-5P + NADPH; direction=REVERSIBLE. This is the second reaction in the mevalonate-independent isopentenyl diphosphate (IPP) biosynthetic pathway.

## Biological Role

Catalyzed by 1-deoxy-D-xylulose 5-phosphate reductoisomerase (complex.ecocyc.DXPREDISOM-CPLX). Substrates: NADP+ (molecule.C00006), 2-C-Methyl-D-erythritol 4-phosphate (molecule.C11434). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

This is the second reaction in the mevalonate-independent isopentenyl diphosphate (IPP) biosynthetic pathway.

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.DXPREDISOM-CPLX|complex.ecocyc.DXPREDISOM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11434|molecule.C11434]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-441|molecule.ecocyc.CPD0-441]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DXPREDISOM-RXN`

## Notes

2-C-METHYL-D-ERYTHRITOL-4-PHOSPHATE + NADP -> PROTON + DEOXYXYLULOSE-5P + NADPH; direction=REVERSIBLE
