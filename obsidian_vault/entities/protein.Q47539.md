---
entity_id: "protein.Q47539"
entity_type: "protein"
name: "tauC"
source_database: "UniProt"
source_id: "Q47539"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tauC ssiC yaiJ b0367 JW0359"
---

# tauC

`protein.Q47539`

## Static

- Type: `protein`
- Source: `UniProt:Q47539`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of a binding-protein-dependent transport system for taurine. Probably responsible for the translocation of the substrate across the membrane. TauC is the predicted inner membrane subunit of an ATP-dependent taurine uptake system; TauC contains six potential membrane-spanning regions . tauBC in-frame deletion mutants are unable to grow with taurine as a sulfur source and show reduced growth with decanesulfonate as a sulfur source .

## Biological Role

Component of taurine ABC transporter (complex.ecocyc.ABC-64-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a binding-protein-dependent transport system for taurine. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-64-CPLX|complex.ecocyc.ABC-64-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0367|gene.b0367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47539`
- `KEGG:ecj:JW0359;eco:b0367;`
- `GeneID:945026;`
- `GO:GO:0005886; GO:0010438; GO:0015734; GO:0016020; GO:0055052`

## Notes

Taurine transport system permease protein TauC
