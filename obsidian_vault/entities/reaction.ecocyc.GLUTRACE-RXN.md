---
entity_id: "reaction.ecocyc.GLUTRACE-RXN"
entity_type: "reaction"
name: "GLUTRACE-RXN"
source_database: "EcoCyc"
source_id: "GLUTRACE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTRACE-RXN

`reaction.ecocyc.GLUTRACE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTRACE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction racemizes L-glutamate to D-glutamate which is an essential component of peptidoglycan. EcoCyc reaction equation: GLT -> D-GLT; direction=REVERSIBLE. This reaction racemizes L-glutamate to D-glutamate which is an essential component of peptidoglycan.

## Biological Role

Catalyzed by murI (protein.P22634). Substrates: L-Glutamate (molecule.C00025). Products: D-Glutamate (molecule.C00217).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This reaction racemizes L-glutamate to D-glutamate which is an essential component of peptidoglycan.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C01212|molecule.C01212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P22634|protein.P22634]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00217|molecule.C00217]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUTRACE-RXN`

## Notes

GLT -> D-GLT; direction=REVERSIBLE
