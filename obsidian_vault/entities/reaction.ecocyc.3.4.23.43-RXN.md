---
entity_id: "reaction.ecocyc.3.4.23.43-RXN"
entity_type: "reaction"
name: "3.4.23.43-RXN"
source_database: "EcoCyc"
source_id: "3.4.23.43-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.23.43-RXN

`reaction.ecocyc.3.4.23.43-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.23.43-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + type-IV-prepillin -> Peptide-C-terminal-Glycines + Cleaved-Type-IV-Prepillins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + type-IV-prepillin -> Peptide-C-terminal-Glycines + Cleaved-Type-IV-Prepillins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by gspO (protein.P25960). Substrates: H2O (molecule.C00001). Products: an N-terminal L-phenylalanyl-[type IV prepilin] (molecule.ecocyc.Cleaved-Type-IV-Prepillins), a [protein] C-terminal glycine (molecule.ecocyc.Peptide-C-terminal-Glycines).

## Annotation

WATER + type-IV-prepillin -> Peptide-C-terminal-Glycines + Cleaved-Type-IV-Prepillins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P25960|protein.P25960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Cleaved-Type-IV-Prepillins|molecule.ecocyc.Cleaved-Type-IV-Prepillins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Peptide-C-terminal-Glycines|molecule.ecocyc.Peptide-C-terminal-Glycines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.23.43-RXN`

## Notes

WATER + type-IV-prepillin -> Peptide-C-terminal-Glycines + Cleaved-Type-IV-Prepillins; direction=PHYSIOL-LEFT-TO-RIGHT
