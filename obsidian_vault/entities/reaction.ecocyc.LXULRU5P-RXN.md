---
entity_id: "reaction.ecocyc.LXULRU5P-RXN"
entity_type: "reaction"
name: "LXULRU5P-RXN"
source_database: "EcoCyc"
source_id: "LXULRU5P-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LXULRU5P-RXN

`reaction.ecocyc.LXULRU5P-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LXULRU5P-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-RIBULOSE-5-P -> L-XYLULOSE-5-P; direction=RIGHT-TO-LEFT EcoCyc reaction equation: L-RIBULOSE-5-P -> L-XYLULOSE-5-P; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by sgbU (protein.P37679), ulaE (protein.P39305). Substrates: L-Ribulose 5-phosphate (molecule.C01101). Products: L-Xylulose 5-phosphate (molecule.C03291).

## Enriched Pathways

- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)
- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)
- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Annotation

L-RIBULOSE-5-P -> L-XYLULOSE-5-P; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)
- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)
- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P37679|protein.P37679]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39305|protein.P39305]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03291|molecule.C03291]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01101|molecule.C01101]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LXULRU5P-RXN`

## Notes

L-RIBULOSE-5-P -> L-XYLULOSE-5-P; direction=RIGHT-TO-LEFT
