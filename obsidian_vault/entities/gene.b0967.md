---
entity_id: "gene.b0967"
entity_type: "gene"
name: "rlmI"
source_database: "NCBI RefSeq"
source_id: "gene-b0967"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0967"
  - "rlmI"
---

# rlmI

`gene.b0967`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0967`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmI (gene.b0967) is a gene entity. It encodes rlmI (protein.P75876). Encoded protein function: FUNCTION: Specifically methylates the cytosine at position 1962 (m5C1962) of 23S rRNA. Methylation occurs before assembly of 23S rRNA into 50S subunits. {ECO:0000269|PubMed:18786544}. EcoCyc product frame: G6501-MONOMER. EcoCyc synonyms: yccW. Genomic coordinates: 1028779-1029969. EcoCyc protein note: RlmI is the methyltransferase responsible for methylation of 23S rRNA at the C5 position of the C1962 nucleotide. The enzyme can methylate naked 23S rRNA, but not assembled 50S ribosomal subunits or 70S ribosomes . A crystal structure of RlmI has been solved at 2 Å resolution; domain organization and possible evolutionary relationships of the enzyme are discussed . A mutant with a deletion of rlmI shows a significant decrease in biofilm formation . However, an rlmI mutant shows only a slight growth defect compared to wild-type cells during competitive growth experiments in rich or minimal medium . Expression of rlmI increases 17-fold upon deletion of tqsA, which increases biofilm formation . RlmI: "rRNA large subunit methyltransferase I" Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75876|protein.P75876]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003272,ECOCYC:G6501,GeneID:946691`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1028779-1029969:-; feature_type=gene
