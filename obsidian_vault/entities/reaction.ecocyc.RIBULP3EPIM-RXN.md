---
entity_id: "reaction.ecocyc.RIBULP3EPIM-RXN"
entity_type: "reaction"
name: "RIBULP3EPIM-RXN"
source_database: "EcoCyc"
source_id: "RIBULP3EPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "D-ribulose-5-phosphate 3-epimerase"
  - "pentose phosphate epimerase"
  - "PPE"
---

# RIBULP3EPIM-RXN

`reaction.ecocyc.RIBULP3EPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBULP3EPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the non-oxidative branch of the pentose phosphate pathway. EcoCyc reaction equation: RIBULOSE-5P -> XYLULOSE-5-PHOSPHATE; direction=REVERSIBLE. This reaction is part of the non-oxidative branch of the pentose phosphate pathway.

## Biological Role

Catalyzed by rpe (protein.P0AG07). Substrates: D-Ribulose 5-phosphate (molecule.C00199). Products: D-Xylulose 5-phosphate (molecule.C00231).

## Enriched Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Annotation

This reaction is part of the non-oxidative branch of the pentose phosphate pathway.

## Pathways

- `ecocyc.NONOXIPENT-PWY` pentose phosphate pathway (non-oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AG07|protein.P0AG07]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00231|molecule.C00231]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBULP3EPIM-RXN`

## Notes

RIBULOSE-5P -> XYLULOSE-5-PHOSPHATE; direction=REVERSIBLE
