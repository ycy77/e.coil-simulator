---
entity_id: "gene.b0642"
entity_type: "gene"
name: "leuS"
source_database: "NCBI RefSeq"
source_id: "gene-b0642"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0642"
  - "leuS"
---

# leuS

`gene.b0642`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0642`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuS (gene.b0642) is a gene entity. It encodes leuS (protein.P07813). Encoded protein function: Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS) EcoCyc product frame: LEUS-MONOMER. EcoCyc synonyms: syl. Genomic coordinates: 672201-674783. EcoCyc protein note: Leucine-tRNA ligase (LeuRS) is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. LeuRS belongs to the Class IB aminoacyl tRNA synthetases; apart from sequence motifs within the active site, the different enzymes show little similarity in their primary amino acid sequences . Correct aminoacylation by LeuRS requires both an activation and an editing function . The CCA acceptor end of tRNALeu is essential for both the aminoacylation and editing reaction . Measurement of kinetic parameters for both reactions showed that the rate-limiting step for posttransfer editing is product release, and that its active site functions by kinetic partitioning between hydrolysis and dissociation of misacylated tRNA . LeuRS shows high initial substrate discrimination and appears to correct mistakes by posttransfer editing alone . LeuRS editing defects are lethal to the cell...

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07813|protein.P07813]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002196,ECOCYC:EG10532,GeneID:947497`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:672201-674783:-; feature_type=gene
