---
entity_id: "reaction.ecocyc.RXN-17391"
entity_type: "reaction"
name: "RXN-17391"
source_database: "EcoCyc"
source_id: "RXN-17391"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17391

`reaction.ecocyc.RXN-17391`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17391`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-17989 -> CPD-17989 + CPD0-1080; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-17989 -> CPD-17989 + CPD0-1080; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mltA (protein.P0A935), mltD (protein.P0AEZ7), slt (protein.P0AGC3), mltF (protein.P0AGC5), mltC (protein.P0C066), emtA (protein.P0C960), mltB (protein.P41052). Substrates: a mature peptidoglycan (meso-DAP containing) (molecule.ecocyc.CPD-17989). Products: a mature peptidoglycan (meso-DAP containing) (molecule.ecocyc.CPD-17989), GlcNAc-1,6-anhMurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala (molecule.ecocyc.CPD0-1080).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

CPD-17989 -> CPD-17989 + CPD0-1080; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0A935|protein.P0A935]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEZ7|protein.P0AEZ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AGC3|protein.P0AGC3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AGC5|protein.P0AGC5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C066|protein.P0C066]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C960|protein.P0C960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P41052|protein.P41052]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-17989|molecule.ecocyc.CPD-17989]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1080|molecule.ecocyc.CPD0-1080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17989|molecule.ecocyc.CPD-17989]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17391`

## Notes

CPD-17989 -> CPD-17989 + CPD0-1080; direction=PHYSIOL-LEFT-TO-RIGHT
