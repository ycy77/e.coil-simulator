---
entity_id: "reaction.ecocyc.PRODISULFREDUCT-A-RXN"
entity_type: "reaction"
name: "PRODISULFREDUCT-A-RXN"
source_database: "EcoCyc"
source_id: "PRODISULFREDUCT-A-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PRODISULFREDUCT-A-RXN

`reaction.ecocyc.PRODISULFREDUCT-A-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRODISULFREDUCT-A-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction uses glutathione to reduce glutaredoxin. EcoCyc reaction equation: GLUTATHIONE + Ox-Glutaredoxins -> OXIDIZED-GLUTATHIONE + Red-Glutaredoxins; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction uses glutathione to reduce glutaredoxin.

## Biological Role

Substrates: Glutathione (molecule.C00051). Products: Glutathione disulfide (molecule.C00127).

## Enriched Pathways

- `ecocyc.GLUT-REDOX-PWY` glutathione-glutaredoxin redox reactions (EcoCyc)
- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Annotation

This reaction uses glutathione to reduce glutaredoxin.

## Pathways

- `ecocyc.GLUT-REDOX-PWY` glutathione-glutaredoxin redox reactions (EcoCyc)
- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PRODISULFREDUCT-A-RXN`

## Notes

GLUTATHIONE + Ox-Glutaredoxins -> OXIDIZED-GLUTATHIONE + Red-Glutaredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
