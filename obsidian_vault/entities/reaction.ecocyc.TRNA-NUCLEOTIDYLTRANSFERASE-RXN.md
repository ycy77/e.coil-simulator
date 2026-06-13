---
entity_id: "reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "TRNA-NUCLEOTIDYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "TRNA-NUCLEOTIDYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "RNASE PH"
  - "PHOSPHATE-DEPENDENT EXONUCLEASE"
---

# TRNA-NUCLEOTIDYLTRANSFERASE-RXN

`reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRNA-NUCLEOTIDYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA-Holder + Pi -> RNA-Holder + Nucleoside-Diphosphates; direction=LEFT-TO-RIGHT EcoCyc reaction equation: RNA-Holder + Pi -> RNA-Holder + Nucleoside-Diphosphates; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rph (protein.P0CG19). Substrates: RNA (molecule.C00046), phosphate (molecule.ecocyc.Pi). Products: RNA (molecule.C00046), a nucleoside diphosphate (molecule.ecocyc.Nucleoside-Diphosphates).

## Annotation

RNA-Holder + Pi -> RNA-Holder + Nucleoside-Diphosphates; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0CG19|protein.P0CG19]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Diphosphates|molecule.ecocyc.Nucleoside-Diphosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRNA-NUCLEOTIDYLTRANSFERASE-RXN`

## Notes

RNA-Holder + Pi -> RNA-Holder + Nucleoside-Diphosphates; direction=LEFT-TO-RIGHT
