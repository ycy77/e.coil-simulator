---
entity_id: "reaction.ecocyc.RIB5PISOM-RXN"
entity_type: "reaction"
name: "RIB5PISOM-RXN"
source_database: "EcoCyc"
source_id: "RIB5PISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIB5PISOM-RXN

`reaction.ecocyc.RIB5PISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIB5PISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the pentose phosphate pathway. This is part of the non-oxidative branch of the path, leading to xylulose 5-phosphate. EcoCyc reaction equation: RIBOSE-5P -> RIBULOSE-5P; direction=REVERSIBLE. Part of the pentose phosphate pathway. This is part of the non-oxidative branch of the path, leading to xylulose 5-phosphate.

## Biological Role

Catalyzed by ribose-5-phosphate isomerase A (complex.ecocyc.RIB5PISOMA-CPLX), allose-6-phosphate isomerase / ribose-5-phosphate isomerase B (complex.ecocyc.RIB5PISOMB-CPLX). Substrates: D-Ribose 5-phosphate (molecule.C00117). Products: D-Ribulose 5-phosphate (molecule.C00199).

## Enriched Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Annotation

Part of the pentose phosphate pathway. This is part of the non-oxidative branch of the path, leading to xylulose 5-phosphate.

## Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.RIB5PISOMA-CPLX|complex.ecocyc.RIB5PISOMA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.RIB5PISOMB-CPLX|complex.ecocyc.RIB5PISOMB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01112|molecule.C01112]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RIB5PISOM-RXN`

## Notes

RIBOSE-5P -> RIBULOSE-5P; direction=REVERSIBLE
