---
entity_id: "protein.P27303"
entity_type: "protein"
name: "emrA"
source_database: "UniProt"
source_id: "P27303"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590}; Single-pass membrane protein {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590}; Periplasmic side {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emrA b2685 JW2660"
---

# emrA

`protein.P27303`

## Static

- Type: `protein`
- Source: `UniProt:P27303`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590}; Single-pass membrane protein {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590}; Periplasmic side {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system EmrAB-TolC (PubMed:12482849, PubMed:1409590, PubMed:33065135). The system confers resistance to antibiotics such as nalidixic acid and to various hydrophobic compounds, including CCCP, FCCP and 2,4-dinitrophenol (PubMed:12482849, PubMed:1409590, PubMed:33065135). EmrA is a drug-binding protein that provides a physical link between EmrB and TolC (PubMed:12482849, PubMed:33065135). {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590, ECO:0000269|PubMed:33065135}. EmrA is the membrane fusion protein of a tripartite efflux pump that is implicated in the export of a variety of mainly hydrophobic compounds - carbonylcyanide m-chlorophenylhydrazone (CCCP), tetrachlorosalicyanide (TSA), nalidixate, phenylmercury acetate and others (see CPLX0-2121 for more details). EmrA is anchored to the inner membrane by an N-terminal α-helix; EmrA can form dimers and trimers; the periplasmic domain of EmrA appears to be elongated and contains a drug-binding site . EmrA forms dynamic oligomers on a biochip sensor surface; EmrA forms dimers and trimers in solution; EmrA-TolC interaction can be reconstituted in vitro . emr: E. coli multidrug resistance

## Biological Role

Component of multidrug efflux pump EmrAB-TolC (complex.ecocyc.CPLX0-2121).

## Annotation

FUNCTION: Part of the tripartite efflux system EmrAB-TolC (PubMed:12482849, PubMed:1409590, PubMed:33065135). The system confers resistance to antibiotics such as nalidixic acid and to various hydrophobic compounds, including CCCP, FCCP and 2,4-dinitrophenol (PubMed:12482849, PubMed:1409590, PubMed:33065135). EmrA is a drug-binding protein that provides a physical link between EmrB and TolC (PubMed:12482849, PubMed:33065135). {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590, ECO:0000269|PubMed:33065135}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2121|complex.ecocyc.CPLX0-2121]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2685|gene.b2685]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27303`
- `KEGG:ecj:JW2660;eco:b2685;ecoc:C3026_14785;`
- `GeneID:947166;`
- `GO:GO:0005886; GO:0009636; GO:0015125; GO:0015721; GO:0030288; GO:0042802; GO:0042910; GO:0046677; GO:0048545; GO:0098567; GO:0140330; GO:1990281; GO:1990961`

## Notes

Multidrug export protein EmrA
