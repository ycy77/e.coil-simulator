---
entity_id: "protein.P06971"
entity_type: "protein"
name: "fhuA"
source_database: "UniProt"
source_id: "P06971"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:2066336, ECO:0000269|PubMed:8916906, ECO:0000269|PubMed:9856937, ECO:0000269|PubMed:9865695}; Multi-pass membrane protein {ECO:0000269|PubMed:9856937, ECO:0000269|PubMed:9865695}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhuA tonA b0150 JW0146"
---

# fhuA

`protein.P06971`

## Static

- Type: `protein`
- Source: `UniProt:P06971`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:2066336, ECO:0000269|PubMed:8916906, ECO:0000269|PubMed:9856937, ECO:0000269|PubMed:9865695}; Multi-pass membrane protein {ECO:0000269|PubMed:9856937, ECO:0000269|PubMed:9865695}.

## Enriched Summary

FUNCTION: Involved in the uptake of iron in complex with ferrichrome, a hydroxamate-type siderophore. Binds and transports ferrichrome-iron across the outer membrane (PubMed:1089064, PubMed:2066336). In addition to its role in ferrichrome-iron transport, transports the antibiotic albomycin, which is a structural analog of ferrichrome, and acts as a receptor for colicin M, microcin J25 and bacteriophages T1, T5, phi80 and UC-1 (PubMed:1089064, PubMed:2066336, PubMed:353030, PubMed:8617231). The energy source, which is required for all FhuA functions except infection by phage T5, is provided by the inner membrane TonB system (PubMed:12427941, PubMed:353030, PubMed:9353297). {ECO:0000269|PubMed:1089064, ECO:0000269|PubMed:12427941, ECO:0000269|PubMed:2066336, ECO:0000269|PubMed:353030, ECO:0000269|PubMed:8617231, ECO:0000269|PubMed:9353297}. FhuA is an outer membrane protein that mediates binding and EG11012-MONOMER TonB-dependent active transport of ferrichrome and its close analogs across the outer membrane; it also transports the antibiotics albomycin and rifamycin CGP 4832, and serves as the receptor for phages T1, T5, UC-1, Φ80 (and others ), and the peptides colicin M and microcin J25 (see ). Early studies characterized fhuA (formerly tonA) mutants which are deficient in ferrichrome uptake and resistant to phages T1, T5 and Φ80, to colicin M and to the antibiotic albomycin...

## Biological Role

Component of ferrichrome outer membrane transport complex (complex.ecocyc.CPLX0-1942).

## Annotation

FUNCTION: Involved in the uptake of iron in complex with ferrichrome, a hydroxamate-type siderophore. Binds and transports ferrichrome-iron across the outer membrane (PubMed:1089064, PubMed:2066336). In addition to its role in ferrichrome-iron transport, transports the antibiotic albomycin, which is a structural analog of ferrichrome, and acts as a receptor for colicin M, microcin J25 and bacteriophages T1, T5, phi80 and UC-1 (PubMed:1089064, PubMed:2066336, PubMed:353030, PubMed:8617231). The energy source, which is required for all FhuA functions except infection by phage T5, is provided by the inner membrane TonB system (PubMed:12427941, PubMed:353030, PubMed:9353297). {ECO:0000269|PubMed:1089064, ECO:0000269|PubMed:12427941, ECO:0000269|PubMed:2066336, ECO:0000269|PubMed:353030, ECO:0000269|PubMed:8617231, ECO:0000269|PubMed:9353297}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1942|complex.ecocyc.CPLX0-1942]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0150|gene.b0150]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06971`
- `KEGG:ecj:JW0146;eco:b0150;`
- `GeneID:75202035;944856;`
- `GO:GO:0005506; GO:0006879; GO:0009279; GO:0015344; GO:0015643; GO:0016020; GO:0019904; GO:0033214; GO:0038023; GO:0044718; GO:0046790; GO:1902495`

## Notes

Ferrichrome outer membrane transporter/phage receptor (Ferric hydroxamate receptor) (Ferric hydroxamate uptake) (Ferrichrome-iron receptor)
