---
entity_id: "reaction.ecocyc.THTOREDUCT-RXN"
entity_type: "reaction"
name: "THTOREDUCT-RXN"
source_database: "EcoCyc"
source_id: "THTOREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THTOREDUCT-RXN

`reaction.ecocyc.THTOREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THTOREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is part of anaerobic respiration. EcoCyc reaction equation: TETRAHYDROTHIOPHENE-1-OXIDE + Donor-H2 -> TETRAHYDROTHIOPHENE + Acceptor + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of anaerobic respiration.

## Biological Role

Substrates: tetrahydrothiophene 1-oxide (molecule.ecocyc.TETRAHYDROTHIOPHENE-1-OXIDE). Products: H2O (molecule.C00001), tetrahydrothiophene (molecule.ecocyc.TETRAHYDROTHIOPHENE).

## Annotation

This reaction is part of anaerobic respiration.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TETRAHYDROTHIOPHENE|molecule.ecocyc.TETRAHYDROTHIOPHENE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.TETRAHYDROTHIOPHENE-1-OXIDE|molecule.ecocyc.TETRAHYDROTHIOPHENE-1-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THTOREDUCT-RXN`

## Notes

TETRAHYDROTHIOPHENE-1-OXIDE + Donor-H2 -> TETRAHYDROTHIOPHENE + Acceptor + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
