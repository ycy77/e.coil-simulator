---
entity_id: "gene.b1111"
entity_type: "gene"
name: "comR"
source_database: "NCBI RefSeq"
source_id: "gene-b1111"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1111"
  - "comR"
---

# comR

`gene.b1111`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1111`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

comR (gene.b1111) is a gene entity. It encodes comR (protein.P75952). Encoded protein function: FUNCTION: Represses expression of BhsA/ComC by binding to its promoter region in the absence of copper. {ECO:0000269|PubMed:22089859}. EcoCyc product frame: G6569-MONOMER. EcoCyc synonyms: ycfQ. Genomic coordinates: 1168200-1168832. EcoCyc protein note: ComR is a member of the TetR family of transcriptional repressors and has been implicated in the the response of E. coli K-12 to copper. ComR contains a helix-turn-helix motif to bind DNA in its N-terminal domain . In in vitro experiments, ComR binds to a 60 bp promotor region upstream of the comC gene but is released in the presence of copper, silver or gold. Expression of comC is dramatically increased (approx 270 fold) in a comR negative strain upon exposure to 3mM copper. comR knockout mutants have lower cytoplasmic copper levels compared to the wild type when exposed to copper . Expression of comR is not affected by copper , but its expression is affected by cadmium . Genome-wide ComR binding sites were determined in vivo in M9 glucose minimal medium by chromatin immunoprecipitation assays (ChIP-exo) . Various target genes of ComR were found upregulated after 10 min of exposure to 2.5 mM H2O2, despite the comR gene being slightly upregulated . Review: .

## Biological Role

Repressed by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75952|protein.P75952]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=comR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003754,ECOCYC:G6569,GeneID:947425`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1168200-1168832:-; feature_type=gene
