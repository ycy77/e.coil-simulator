---
entity_id: "protein.Q47538"
entity_type: "protein"
name: "tauB"
source_database: "UniProt"
source_id: "Q47538"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01714}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01714}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tauB ssiB yaiQ b0366 JW0358"
---

# tauB

`protein.Q47538`

## Static

- Type: `protein`
- Source: `UniProt:Q47538`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01714}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01714}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex TauABC involved in taurine import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01714, ECO:0000269|PubMed:10781534, ECO:0000269|PubMed:8808933}. TauB is the predicted ATP-binding subunit of a taurine uptake system; TauB contains sequence motifs conserved in ATP-binding cassette (ABC) proteins . tauBC in-frame deletion mutants are unable to grow with taurine as a sulfur source and show reduced growth with decanesulfonate as a sulfur source .

## Biological Role

Component of taurine ABC transporter (complex.ecocyc.ABC-64-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex TauABC involved in taurine import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01714, ECO:0000269|PubMed:10781534, ECO:0000269|PubMed:8808933}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-64-CPLX|complex.ecocyc.ABC-64-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0366|gene.b0366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47538`
- `KEGG:ecj:JW0358;eco:b0366;`
- `GeneID:93777092;945027;`
- `GO:GO:0005524; GO:0010438; GO:0015411; GO:0015734; GO:0016020; GO:0016887; GO:0055052`
- `EC:7.6.2.7`

## Notes

Taurine import ATP-binding protein TauB (EC 7.6.2.7)
