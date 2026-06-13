---
entity_id: "reaction.ecocyc.RXN-17393"
entity_type: "reaction"
name: "RXN-17393"
source_database: "EcoCyc"
source_id: "RXN-17393"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17393

`reaction.ecocyc.RXN-17393`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17393`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCI-PERI-BAC-GN

## Enriched Summary

CPD-18807 -> CPD-18808 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18807 -> CPD-18808 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mltG (protein.P28306). Substrates: a nascent peptidoglycan (meso-DAP containing) (molecule.ecocyc.CPD-18807). Products: a peptidoglycan (meso-DAP containing) with GlcNAc-1,6-anhydro-MurNAc terminus (molecule.ecocyc.CPD-17986), a nascent peptidoglycan (meso-DAP containing) with GlcNAc non-reducing terminus (molecule.ecocyc.CPD-18808).

## Enriched Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

CPD-18807 -> CPD-18808 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P28306|protein.P28306]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-17986|molecule.ecocyc.CPD-17986]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18808|molecule.ecocyc.CPD-18808]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18807|molecule.ecocyc.CPD-18807]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17393`

## Notes

CPD-18807 -> CPD-18808 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT
