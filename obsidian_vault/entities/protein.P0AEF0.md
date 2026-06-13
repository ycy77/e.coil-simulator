---
entity_id: "protein.P0AEF0"
entity_type: "protein"
name: "dnaC"
source_database: "UniProt"
source_id: "P0AEF0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaC dnaD b4361 JW4325"
---

# dnaC

`protein.P0AEF0`

## Static

- Type: `protein`
- Source: `UniProt:P0AEF0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required to load the replicative helix DnaB onto single-stranded (ss)DNA, to initiate chromosomal replication (PubMed:30797687). Also loads the DnaB in the replication restart primosome (composed of PriA, PriB, PriC, DnaB and DnaT; DnaG primase associates transiently with this complex) (PubMed:6454139, PubMed:8663104, PubMed:8663105). DnaC alters the inter-domain and inter-subunit interactions of DnaB, inducing an open ring conformation that allows ssDNA to access the interior of the DnaB(6):DnaC(6) ring (PubMed:30797687). Has ATPase activity only in the presence of DnaB and ssDNA (PubMed:30797687). ssDNA binds to the central pore in the DnaB(6):DnaC(6) complex, making contacts with both subunits (PubMed:30797687). Mutations in this protein can bypass the need for PriA recognition of collapsed replication fork substrates in order to load DnaB onto recombinational intermediates in vivo (PubMed:10540288). {ECO:0000269|PubMed:10540288, ECO:0000269|PubMed:30797687, ECO:0000269|PubMed:6454139, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105}.

## Biological Role

Component of DNA replication protein DnaC (complex.ecocyc.CPLX0-13255), DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Annotation

FUNCTION: Required to load the replicative helix DnaB onto single-stranded (ss)DNA, to initiate chromosomal replication (PubMed:30797687). Also loads the DnaB in the replication restart primosome (composed of PriA, PriB, PriC, DnaB and DnaT; DnaG primase associates transiently with this complex) (PubMed:6454139, PubMed:8663104, PubMed:8663105). DnaC alters the inter-domain and inter-subunit interactions of DnaB, inducing an open ring conformation that allows ssDNA to access the interior of the DnaB(6):DnaC(6) ring (PubMed:30797687). Has ATPase activity only in the presence of DnaB and ssDNA (PubMed:30797687). ssDNA binds to the central pore in the DnaB(6):DnaC(6) complex, making contacts with both subunits (PubMed:30797687). Mutations in this protein can bypass the need for PriA recognition of collapsed replication fork substrates in order to load DnaB onto recombinational intermediates in vivo (PubMed:10540288). {ECO:0000269|PubMed:10540288, ECO:0000269|PubMed:30797687, ECO:0000269|PubMed:6454139, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13255|complex.ecocyc.CPLX0-13255]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4361|gene.b4361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEF0`
- `KEGG:ecj:JW4325;eco:b4361;ecoc:C3026_23560;`
- `GeneID:93777487;948864;`
- `GO:GO:0003677; GO:0005524; GO:0006260; GO:0006269; GO:0006270; GO:0006271; GO:0016787; GO:0031297; GO:1990077; GO:1990100; GO:1990158; GO:1990159; GO:1990160`
- `EC:3.6.4.-`

## Notes

Replicative helicase loader DnaC (EC 3.6.4.-) (DNA replication protein DnaC)
