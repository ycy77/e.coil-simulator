---
entity_id: "gene.b3984"
entity_type: "gene"
name: "rplA"
source_database: "NCBI RefSeq"
source_id: "gene-b3984"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3984"
  - "rplA"
---

# rplA

`gene.b3984`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3984`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplA (gene.b3984) is a gene entity. It encodes rplA (protein.P0A7L0). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds very close to the 3'-end of the 23S rRNA. Forms part of the L1 stalk. It is often not seen in high-resolution crystal structures, but can be seen in cryo_EM and 3D reconstruction models. These indicate that the distal end of the stalk moves by approximately 20 angstroms (PubMed:12859903, PubMed:16272117). This stalk movement is thought to be coupled to movement of deacylated tRNA into and out of the E site, and thus to participate in tRNA translocation (PubMed:12859903, PubMed:16272117). Contacts the P and E site tRNAs. {ECO:0000269|PubMed:12859903, ECO:0000269|PubMed:16272117}.; FUNCTION: Protein L1 is also a translational repressor protein, it controls the translation of the L11 operon by binding to its mRNA. EcoCyc product frame: EG10864-MONOMER. EcoCyc synonyms: rpy. Genomic coordinates: 4178879-4179583. EcoCyc protein note: The L1 protein is a component of the 50S subunit of the ribosome and also functions in the post-transcriptional regulation of the ribosomal protein genes encoded in the L11 operon. Ribosomes lacking L1 show a lower translation activity than wild type and are defective in binding of aminoacylated tRNA...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7L0|protein.P0A7L0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013031,ECOCYC:EG10864,GeneID:948483`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4178879-4179583:+; feature_type=gene
