---
entity_id: "reaction.ecocyc.BARA-RXN"
entity_type: "reaction"
name: "BARA-RXN"
source_database: "EcoCyc"
source_id: "BARA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BARA-RXN

`reaction.ecocyc.BARA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BARA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction represents the autophosphorylation of sensor histidine kinase BarA at histidine residue 302. EcoCyc reaction equation: CPLX0-8302 + ATP -> MONOMER0-4210 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the autophosphorylation of sensor histidine kinase BarA at histidine residue 302.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1501` BarA UvrY Two-Component Signal Transduction System (EcoCyc)

## Annotation

This reaction represents the autophosphorylation of sensor histidine kinase BarA at histidine residue 302.

## Pathways

- `ecocyc.PWY0-1501` BarA UvrY Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BARA-RXN`

## Notes

CPLX0-8302 + ATP -> MONOMER0-4210 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
