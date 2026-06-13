---
entity_id: "reaction.ecocyc.GLYOXI-RXN"
entity_type: "reaction"
name: "GLYOXI-RXN"
source_database: "EcoCyc"
source_id: "GLYOXI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Ketone-aldehyde mutase"
  - "Glyoxalase I"
  - "Aldoketomutase"
  - "Methylglyoxalase"
---

# GLYOXI-RXN

`reaction.ecocyc.GLYOXI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYOXI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of one path for the degradation of methylglyoxal. EcoCyc reaction equation: S-LACTOYL-GLUTATHIONE -> METHYL-GLYOXAL + GLUTATHIONE; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is part of one path for the degradation of methylglyoxal.

## Biological Role

Catalyzed by lactoylglutathione lyase (complex.ecocyc.GLYOXI-CPLX). Substrates: (R)-S-Lactoylglutathione (molecule.C03451). Products: Glutathione (molecule.C00051), Methylglyoxal (molecule.C00546).

## Enriched Pathways

- `ecocyc.PWY-5386` methylglyoxal degradation I (EcoCyc)

## Annotation

This reaction is part of one path for the degradation of methylglyoxal.

## Pathways

- `ecocyc.PWY-5386` methylglyoxal degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.GLYOXI-CPLX|complex.ecocyc.GLYOXI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03451|molecule.C03451]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYOXI-RXN`

## Notes

S-LACTOYL-GLUTATHIONE -> METHYL-GLYOXAL + GLUTATHIONE; direction=PHYSIOL-RIGHT-TO-LEFT
