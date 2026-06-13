---
entity_id: "gene.b1463"
entity_type: "gene"
name: "nhoA"
source_database: "NCBI RefSeq"
source_id: "gene-b1463"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1463"
  - "nhoA"
---

# nhoA

`gene.b1463`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1463`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nhoA (gene.b1463) is a gene entity. It encodes nhoA (protein.P77567). Encoded protein function: FUNCTION: Catalyzes the acetyl-CoA-dependent N-acetylation of aromatic amines, and, probably, the O-acetylation of N-hydroxyarylamines. In vitro, catalyzes the N-acetylation of various arylamines such as aminobenzoic acid, aminophenol, aminotoluene, phenetidine, anisidine, aniline, isoniazid and 2-amino-fluorene (PubMed:10806332, PubMed:23452042). N-hydroxyarylamine O-acetyltransferase activity has not been assayed directly, however, NhoA activity is required for the mutagenicity of nitroaromatic compounds, suggesting that it also has O-acetyltransferase activity (Probable). {ECO:0000269|PubMed:10806332, ECO:0000269|PubMed:23452042, ECO:0000305|PubMed:12222687, ECO:0000305|PubMed:23452042}. EcoCyc product frame: G6770-MONOMER. EcoCyc synonyms: yddI. Genomic coordinates: 1534024-1534869. EcoCyc protein note: Arylamine acetyltransferase (NhoA) catalyzes the acetyl-CoA-dependent N-acetylation of a variety of arylamine substrates. It acts via a ping-pong bi bi mechanism . The physiological role of NhoA is unknown. Two acetylated lysine residues within NhoA can be deacetylated by G6577-MONOMER "CobB". Mutants of NhoA in which one or both lysine residues have been mutated have lower N-acetyltransferase activity than wild-type...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77567|protein.P77567]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004882,ECOCYC:G6770,GeneID:947251`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1534024-1534869:+; feature_type=gene
