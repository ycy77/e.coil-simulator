---
entity_id: "gene.b1625"
entity_type: "gene"
name: "cnu"
source_database: "NCBI RefSeq"
source_id: "gene-b1625"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1625"
  - "cnu"
---

# cnu

`gene.b1625`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1625`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cnu (gene.b1625) is a gene entity. It encodes cnu (protein.P64467). Encoded protein function: FUNCTION: Modifies the set of genes regulated by H-NS; Hha and Cnu (YdgT) increase the number of genes bound by H-NS/StpA and may also modulate the oligomerization of the H-NS/StpA-complex on DNA (PubMed:23543115). The complex formed with H-NS binds to the specific 26-bp cnb site in the origin of replication oriC (PubMed:16199570). Can complement, at least partially, the absence of the Hha protein in hha mutants. {ECO:0000269|PubMed:16199570, ECO:0000269|PubMed:23543115}. EcoCyc product frame: G6869-MONOMER. EcoCyc synonyms: ydgT. Genomic coordinates: 1704949-1705164. EcoCyc protein note: YdgT (Cnu) is a paralog of the EG10439-MONOMER Hha protein and can partially compensate for the phenotypes of a hha mutant. YdgT interacts with H-NS and StpA and appears to protect StpA from proteolytic degradation . A heteromeric YdgT-H-NS complex binds the origin of replication (G0-10506 oriC) at a specific 26-bp sequence that overlaps a DnaA binding site . Both YdgT and HolE appear to influence expression of EG11005 tnaA by enhancing transcription termination at the leader DNA sequence . A solution structure of YdgT has been determined. The H-NS binding site includes the flexible C-terminal region of YdgT...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64467|protein.P64467]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005443,ECOCYC:G6869,GeneID:946152`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1704949-1705164:+; feature_type=gene
