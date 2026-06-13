---
entity_id: "reaction.ecocyc.H2NTPEPIM-RXN"
entity_type: "reaction"
name: "H2NTPEPIM-RXN"
source_database: "EcoCyc"
source_id: "H2NTPEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# H2NTPEPIM-RXN

`reaction.ecocyc.H2NTPEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:H2NTPEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction dihydroneopterin triphosphate undergoes epimerization of the C2' carbon forming dihydromonapterin triphosphate. EcoCyc reaction equation: DIHYDRONEOPTERIN-P3 -> DIHYDROMONAPTERIN-TRIPHOSPHATE; direction=REVERSIBLE. In this reaction dihydroneopterin triphosphate undergoes epimerization of the C2' carbon forming dihydromonapterin triphosphate.

## Biological Role

Catalyzed by dihydroneopterin triphosphate 2'-epimerase (complex.ecocyc.FOLXTET-CPLX). Substrates: 7,8-Dihydroneopterin 3'-triphosphate (molecule.C04895). Products: 7,8-Dihydromonapterin 3'-triphosphate (molecule.C21094).

## Enriched Pathways

- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Annotation

In this reaction dihydroneopterin triphosphate undergoes epimerization of the C2' carbon forming dihydromonapterin triphosphate.

## Pathways

- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FOLXTET-CPLX|complex.ecocyc.FOLXTET-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C21094|molecule.C21094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04895|molecule.C04895]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:H2NTPEPIM-RXN`

## Notes

DIHYDRONEOPTERIN-P3 -> DIHYDROMONAPTERIN-TRIPHOSPHATE; direction=REVERSIBLE
