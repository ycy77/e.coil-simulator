---
entity_id: "reaction.ecocyc.CATAL-RXN"
entity_type: "reaction"
name: "CATAL-RXN"
source_database: "EcoCyc"
source_id: "CATAL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "KatG"
---

# CATAL-RXN

`reaction.ecocyc.CATAL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CATAL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in detoxification. EcoCyc reaction equation: HYDROGEN-PEROXIDE -> WATER + OXYGEN-MOLECULE; direction=LEFT-TO-RIGHT. This reaction is involved in detoxification.

## Biological Role

Catalyzed by adenine deaminase (complex.ecocyc.CPLX0-1683), catalase/hydroperoxidase HPI (complex.ecocyc.HYDROPEROXIDI-CPLX), catalase HPII (complex.ecocyc.HYDROPEROXIDII-CPLX). Substrates: Hydrogen peroxide (molecule.C00027). Products: H2O (molecule.C00001), Oxygen (molecule.C00007).

## Enriched Pathways

- `ecocyc.DETOX1-PWY` superoxide radicals degradation (EcoCyc)

## Annotation

This reaction is involved in detoxification.

## Pathways

- `ecocyc.DETOX1-PWY` superoxide radicals degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1683|complex.ecocyc.CPLX0-1683]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.HYDROPEROXIDI-CPLX|complex.ecocyc.HYDROPEROXIDI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.HYDROPEROXIDII-CPLX|complex.ecocyc.HYDROPEROXIDII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CATAL-RXN`

## Notes

HYDROGEN-PEROXIDE -> WATER + OXYGEN-MOLECULE; direction=LEFT-TO-RIGHT
