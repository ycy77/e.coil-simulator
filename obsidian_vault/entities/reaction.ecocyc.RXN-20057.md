---
entity_id: "reaction.ecocyc.RXN-20057"
entity_type: "reaction"
name: "RXN-20057"
source_database: "EcoCyc"
source_id: "RXN-20057"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20057

`reaction.ecocyc.RXN-20057`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20057`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

an-oxidized-DsbD-protein + Protein-Dithiols -> a-reduced-DsbD-protein + Protein-Disulfides; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: an-oxidized-DsbD-protein + Protein-Dithiols -> a-reduced-DsbD-protein + Protein-Disulfides; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: a [protein]-dithiol (molecule.ecocyc.Protein-Dithiols). Products: a [protein]-disulfide (molecule.ecocyc.Protein-Disulfides).

## Enriched Pathways

- `ecocyc.PWY0-1600` periplasmic disulfide bond reduction (EcoCyc)

## Annotation

an-oxidized-DsbD-protein + Protein-Dithiols -> a-reduced-DsbD-protein + Protein-Disulfides; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-1600` periplasmic disulfide bond reduction (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.Protein-Disulfides|molecule.ecocyc.Protein-Disulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Dithiols|molecule.ecocyc.Protein-Dithiols]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20057`

## Notes

an-oxidized-DsbD-protein + Protein-Dithiols -> a-reduced-DsbD-protein + Protein-Disulfides; direction=PHYSIOL-RIGHT-TO-LEFT
