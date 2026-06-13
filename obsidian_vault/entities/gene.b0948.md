---
entity_id: "gene.b0948"
entity_type: "gene"
name: "rlmL"
source_database: "NCBI RefSeq"
source_id: "gene-b0948"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0948"
  - "rlmL"
---

# rlmL

`gene.b0948`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0948`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmL (gene.b0948) is a gene entity. It encodes rlmL (protein.P75864). Encoded protein function: FUNCTION: Specifically methylates the guanine in position 2445 (m2G2445) and the guanine in position 2069 (m7G2069) of 23S rRNA. Methylation occurs before assembly of 23S rRNA into 50S subunits. {ECO:0000269|PubMed:17010378, ECO:0000269|PubMed:22210896, ECO:0000269|PubMed:22362734}. EcoCyc product frame: G6488-MONOMER. EcoCyc synonyms: ycbY, rlmK, rlmKL. Genomic coordinates: 1007844-1009952. EcoCyc protein note: RlmL is a fused dual methyltransferase responsible for methylation of 23S rRNA at the N2 position of the G2445 nucleotide as well as at the N7 position of the G2069 nucleotide . Both nucleotides are part of helix 54, and RlmL has RNA helicase activity that is able to unwind this region during substrate recognition and methylation . In vitro, recombinant RlmL is able to methylate naked 23S rRNA, but not 23S rRNA assembled into the 50S ribosomal subunit . Both m2G and m7G were shown to be formed during early steps of 50S ribosomal subunit assembly . The RlmL protein contains an N-terminal THUMP domain followed by two methyltransferase domains. Analysis of point mutants in the predicted active sites allowed separation of the RlmK (G2069 methyltransferase, C-terminal domain) and RlmL (G2445 methyltransferase, N-terminal domain) functions...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75864|protein.P75864]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003211,ECOCYC:G6488,GeneID:945564`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1007844-1009952:+; feature_type=gene
