---
entity_id: "reaction.ecocyc.RXN0-7395"
entity_type: "reaction"
name: "RXN0-7395"
source_database: "EcoCyc"
source_id: "RXN0-7395"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7395

`reaction.ecocyc.RXN0-7395`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7395`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

G7211-MONOMER SixA-mediated dephosphorylation of phospho-NPr proceeds via a transient phosphohistidine intermediate; phosphoryl transfer involves switching from π(pros)-phosphohistidine (on NPr His-16) to τ(tele)-phosphohistidine (on SixA His-8) . EcoCyc reaction equation: MONOMER0-4292 + WATER -> EG12147-MONOMER + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. G7211-MONOMER SixA-mediated dephosphorylation of phospho-NPr proceeds via a transient phosphohistidine intermediate; phosphoryl transfer involves switching from π(pros)-phosphohistidine (on NPr His-16) to τ(tele)-phosphohistidine (on SixA His-8) .

## Biological Role

Catalyzed by sixA (protein.P76502). Substrates: H2O (molecule.C00001). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

G7211-MONOMER SixA-mediated dephosphorylation of phospho-NPr proceeds via a transient phosphohistidine intermediate; phosphoryl transfer involves switching from π(pros)-phosphohistidine (on NPr His-16) to τ(tele)-phosphohistidine (on SixA His-8) .

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76502|protein.P76502]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7395`

## Notes

MONOMER0-4292 + WATER -> EG12147-MONOMER + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
