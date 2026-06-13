---
entity_id: "protein.Q47537"
entity_type: "protein"
name: "tauA"
source_database: "UniProt"
source_id: "Q47537"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tauA ssiA yaiR b0365 JW0357"
---

# tauA

`protein.Q47537`

## Static

- Type: `protein`
- Source: `UniProt:Q47537`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a binding-protein-dependent transport system for taurine. TauA is the predicted periplasmic binding protein of an ATP-dependent taurine uptake system . tauA in-frame deletion mutants are unable to grow with taurine as a sulfur source and show reduced growth with decanesulfonate as a sulfur source .

## Biological Role

Component of taurine ABC transporter (complex.ecocyc.ABC-64-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a binding-protein-dependent transport system for taurine.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-64-CPLX|complex.ecocyc.ABC-64-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0365|gene.b0365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47537`
- `KEGG:ecj:JW0357;eco:b0365;`
- `GeneID:945030;`
- `GO:GO:0009970; GO:0010438; GO:0015734; GO:0016020; GO:0022857; GO:0030288; GO:0055052`

## Notes

Taurine-binding periplasmic protein (Sulfate starvation-induced protein 1) (SSI1)
