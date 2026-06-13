---
entity_id: "reaction.ecocyc.TRANS-RXN0-565"
entity_type: "reaction"
name: "export of GMP"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-565"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# export of GMP

`reaction.ecocyc.TRANS-RXN0-565`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-565`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli K-12 strains that overproduce IMP or GMP and that lack periplasmic 5' nucleotidases (UshA and AphA) excrete the purine nucleotides IMP and GMP. Although the cytoplasmic membrane is considered impermeable to exogenous nucleotides this result implies the existence of a mechanism for nucleotide efflux . EcoCyc reaction equation: GMP -> GMP; direction=PHYSIOL-LEFT-TO-RIGHT. E. coli K-12 strains that overproduce IMP or GMP and that lack periplasmic 5' nucleotidases (UshA and AphA) excrete the purine nucleotides IMP and GMP. Although the cytoplasmic membrane is considered impermeable to exogenous nucleotides this result implies the existence of a mechanism for nucleotide efflux .

## Biological Role

Substrates: GMP (molecule.C00144). Products: GMP (molecule.C00144).

## Annotation

E. coli K-12 strains that overproduce IMP or GMP and that lack periplasmic 5' nucleotidases (UshA and AphA) excrete the purine nucleotides IMP and GMP. Although the cytoplasmic membrane is considered impermeable to exogenous nucleotides this result implies the existence of a mechanism for nucleotide efflux .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-565`

## Notes

GMP -> GMP; direction=PHYSIOL-LEFT-TO-RIGHT
