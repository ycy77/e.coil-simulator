---
entity_id: "gene.b4361"
entity_type: "gene"
name: "dnaC"
source_database: "NCBI RefSeq"
source_id: "gene-b4361"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4361"
  - "dnaC"
---

# dnaC

`gene.b4361`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4361`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaC (gene.b4361) is a gene entity. It encodes dnaC (protein.P0AEF0). Encoded protein function: FUNCTION: Required to load the replicative helix DnaB onto single-stranded (ss)DNA, to initiate chromosomal replication (PubMed:30797687). Also loads the DnaB in the replication restart primosome (composed of PriA, PriB, PriC, DnaB and DnaT; DnaG primase associates transiently with this complex) (PubMed:6454139, PubMed:8663104, PubMed:8663105). DnaC alters the inter-domain and inter-subunit interactions of DnaB, inducing an open ring conformation that allows ssDNA to access the interior of the DnaB(6):DnaC(6) ring (PubMed:30797687). Has ATPase activity only in the presence of DnaB and ssDNA (PubMed:30797687). ssDNA binds to the central pore in the DnaB(6):DnaC(6) complex, making contacts with both subunits (PubMed:30797687). Mutations in this protein can bypass the need for PriA recognition of collapsed replication fork substrates in order to load DnaB onto recombinational intermediates in vivo (PubMed:10540288). {ECO:0000269|PubMed:10540288, ECO:0000269|PubMed:30797687, ECO:0000269|PubMed:6454139, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105}. EcoCyc product frame: EG10237-MONOMER. EcoCyc synonyms: dnaD. Genomic coordinates: 4600238-4600975.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEF0|protein.P0AEF0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014304,ECOCYC:EG10237,GeneID:948864`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4600238-4600975:-; feature_type=gene
