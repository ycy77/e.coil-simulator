---
entity_id: "reaction.ecocyc.LCARNCOALIG-RXN"
entity_type: "reaction"
name: "LCARNCOALIG-RXN"
source_database: "EcoCyc"
source_id: "LCARNCOALIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LCARNCOALIG-RXN

`reaction.ecocyc.LCARNCOALIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LCARNCOALIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in carnitine metabolism, utilizing L-carnitine. EcoCyc reaction equation: CO-A + CARNITINE + ATP -> L-CARNITINYL-COA + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction in carnitine metabolism, utilizing L-carnitine.

## Biological Role

Catalyzed by caiC (protein.P31552). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), L-carnitine (molecule.ecocyc.CARNITINE). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), (R)-carnitinyl-CoA (molecule.ecocyc.L-CARNITINYL-COA).

## Enriched Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Annotation

This is a reaction in carnitine metabolism, utilizing L-carnitine.

## Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P31552|protein.P31552]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-CARNITINYL-COA|molecule.ecocyc.L-CARNITINYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CARNITINE|molecule.ecocyc.CARNITINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LCARNCOALIG-RXN`

## Notes

CO-A + CARNITINE + ATP -> L-CARNITINYL-COA + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
