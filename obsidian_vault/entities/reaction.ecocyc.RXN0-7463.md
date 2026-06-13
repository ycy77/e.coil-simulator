---
entity_id: "reaction.ecocyc.RXN0-7463"
entity_type: "reaction"
name: "poly(A)-specific ribonuclease"
source_database: "EcoCyc"
source_id: "RXN0-7463"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# poly(A)-specific ribonuclease

`reaction.ecocyc.RXN0-7463`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7463`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction represents the exonucleolytic cleavage of adenosine nucleotides on the 3' end of a tRNA during tRNA processing . EcoCyc reaction equation: RNA-fragment-w-polyA-tail + WATER -> RNA-Fragments + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the exonucleolytic cleavage of adenosine nucleotides on the 3' end of a tRNA during tRNA processing .

## Biological Role

Catalyzed by polynucleotide phosphorylase (complex.ecocyc.CPLX0-3521), rph (protein.P0CG19), rnb (protein.P30850). Substrates: H2O (molecule.C00001). Products: AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

This reaction represents the exonucleolytic cleavage of adenosine nucleotides on the 3' end of a tRNA during tRNA processing .

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3521|complex.ecocyc.CPLX0-3521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0CG19|protein.P0CG19]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P30850|protein.P30850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7463`

## Notes

RNA-fragment-w-polyA-tail + WATER -> RNA-Fragments + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
