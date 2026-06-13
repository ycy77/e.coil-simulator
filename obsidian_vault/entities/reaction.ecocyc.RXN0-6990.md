---
entity_id: "reaction.ecocyc.RXN0-6990"
entity_type: "reaction"
name: "RXN0-6990"
source_database: "EcoCyc"
source_id: "RXN0-6990"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6990

`reaction.ecocyc.RXN0-6990`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6990`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

L-cysteine is oxidised to L-cystine in the periplasm. Overexpression of dsbA facilitates L-cystine production in a high L-cysteine producing strain of E. coli . EcoCyc reaction equation: MONOMER0-4152 + CYS -> L-CYSTINE + DISULFOXRED-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT. L-cysteine is oxidised to L-cystine in the periplasm. Overexpression of dsbA facilitates L-cystine production in a high L-cysteine producing strain of E. coli .

## Biological Role

Substrates: L-Cysteine (molecule.C00097). Products: L-Cystine (molecule.C00491).

## Annotation

L-cysteine is oxidised to L-cystine in the periplasm. Overexpression of dsbA facilitates L-cystine production in a high L-cysteine producing strain of E. coli .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6990`

## Notes

MONOMER0-4152 + CYS -> L-CYSTINE + DISULFOXRED-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT
