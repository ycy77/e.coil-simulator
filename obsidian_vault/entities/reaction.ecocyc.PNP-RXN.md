---
entity_id: "reaction.ecocyc.PNP-RXN"
entity_type: "reaction"
name: "PNP-RXN"
source_database: "EcoCyc"
source_id: "PNP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PNP-RXN

`reaction.ecocyc.PNP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PNP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in nucleotide metabolism. EcoCyc reaction equation: Purine-Ribonucleosides + Pi -> Purine-Bases + RIBOSE-1P; direction=REVERSIBLE. This reaction is involved in nucleotide metabolism.

## Biological Role

Catalyzed by purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX). Substrates: phosphate (molecule.ecocyc.Pi), a purine ribonucleoside (molecule.ecocyc.Purine-Ribonucleosides). Products: alpha-D-Ribose 1-phosphate (molecule.C00620), a purine base (molecule.ecocyc.Purine-Bases).

## Annotation

This reaction is involved in nucleotide metabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Purine-Bases|molecule.ecocyc.Purine-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Purine-Ribonucleosides|molecule.ecocyc.Purine-Ribonucleosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PNP-RXN`

## Notes

Purine-Ribonucleosides + Pi -> Purine-Bases + RIBOSE-1P; direction=REVERSIBLE
