---
entity_id: "protein.P06129"
entity_type: "protein"
name: "btuB"
source_database: "UniProt"
source_id: "P06129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:12595710, ECO:0000269|PubMed:12652322, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:12595710, ECO:0000269|PubMed:12652322, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btuB bfe cer dcrC b3966 JW3938"
---

# btuB

`protein.P06129`

## Static

- Type: `protein`
- Source: `UniProt:P06129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:12595710, ECO:0000269|PubMed:12652322, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:12595710, ECO:0000269|PubMed:12652322, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793}.

## Enriched Summary

FUNCTION: Involved in the active translocation of vitamin B12 (cyanocobalamin) across the outer membrane to the periplasmic space (PubMed:4579869). It derives its energy for transport by interacting with the trans-periplasmic membrane protein TonB. {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:10485884, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793, ECO:0000269|PubMed:4579869}.; FUNCTION: (Microbial infection) Acts as a receptor for bacteriophages BF23 and C1, and for A and E colicins (PubMed:14528295, PubMed:4579869). Cyanocobalamin (CN-B12) in solid medium protects against colicins E1 and E3 (PubMed:4579869). Does not act as the translocon for colicin E3 (ColE3). The translocon is OmpF; trimeric complexes with ColE3, BtuB and OmpF can be cross-linked and immunoprecipitated (PubMed:18636093). {ECO:0000269|PubMed:14528295, ECO:0000269|PubMed:18636093, ECO:0000269|PubMed:4579869}. btuB mutants, defective in cobalamin (vitamin B12) transport/binding and resistant to E colicins and phage BF23, were originally isolated from a methionine-coenzyme B12 auxotroph (K-12 strain KBT001; see ). BtuB is an outer membrane protein that mediates binding and TonB-dependent active transport of cobalamin across the outer membrane (see )...

## Biological Role

Component of cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924).

## Annotation

FUNCTION: Involved in the active translocation of vitamin B12 (cyanocobalamin) across the outer membrane to the periplasmic space (PubMed:4579869). It derives its energy for transport by interacting with the trans-periplasmic membrane protein TonB. {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:10485884, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793, ECO:0000269|PubMed:4579869}.; FUNCTION: (Microbial infection) Acts as a receptor for bacteriophages BF23 and C1, and for A and E colicins (PubMed:14528295, PubMed:4579869). Cyanocobalamin (CN-B12) in solid medium protects against colicins E1 and E3 (PubMed:4579869). Does not act as the translocon for colicin E3 (ColE3). The translocon is OmpF; trimeric complexes with ColE3, BtuB and OmpF can be cross-linked and immunoprecipitated (PubMed:18636093). {ECO:0000269|PubMed:14528295, ECO:0000269|PubMed:18636093, ECO:0000269|PubMed:4579869}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3966|gene.b3966]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06129`
- `KEGG:ecj:JW3938;eco:b3966;`
- `GeneID:93777927;948468;`
- `GO:GO:0005509; GO:0009279; GO:0015288; GO:0015420; GO:0015889; GO:0016020; GO:0019904; GO:0034220; GO:0046930; GO:1902495`

## Notes

Vitamin B12 transporter BtuB (Cobalamin receptor) (Outer membrane cobalamin translocator)
