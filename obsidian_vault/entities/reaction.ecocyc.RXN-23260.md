---
entity_id: "reaction.ecocyc.RXN-23260"
entity_type: "reaction"
name: "RXN-23260"
source_database: "EcoCyc"
source_id: "RXN-23260"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23260

`reaction.ecocyc.RXN-23260`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23260`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXYNAPHTHOATE + AMMONIUM + Acceptor -> CPD-25747 + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXYNAPHTHOATE + AMMONIUM + Acceptor -> CPD-25747 + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 1,4-Dihydroxy-2-naphthoate (molecule.C03657), ammonium (molecule.ecocyc.AMMONIUM). Products: 2-amino-3-carboxy-1,4-naphthoquinone (molecule.ecocyc.CPD-25747).

## Annotation

DIHYDROXYNAPHTHOATE + AMMONIUM + Acceptor -> CPD-25747 + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-25747|molecule.ecocyc.CPD-25747]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03657|molecule.C03657]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23260`

## Notes

DIHYDROXYNAPHTHOATE + AMMONIUM + Acceptor -> CPD-25747 + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT
