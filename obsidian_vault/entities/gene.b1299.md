---
entity_id: "gene.b1299"
entity_type: "gene"
name: "puuR"
source_database: "NCBI RefSeq"
source_id: "gene-b1299"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1299"
  - "puuR"
---

# puuR

`gene.b1299`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1299`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuR (gene.b1299) is a gene entity. It encodes puuR (protein.P0A9U6). Encoded protein function: FUNCTION: Represses puuA, puuD and puuP. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:20639325}. EcoCyc product frame: EG12431-MONOMER. EcoCyc synonyms: ycjC. Genomic coordinates: 1361911-1362468. EcoCyc protein note: PuuR is a transcription repressor that regulates transcription of several genes and operons involved in putrescine utilization and transport . Transcription of puuA was induced in a puuR deletion mutant . This regulator is comprised of two domains: the carboxy-terminal domain, which is similar to cupin superfamily proteins, and the amino-terminal domain, which has high similarity to regulators of the HTH-XRE family . Nemoto et al. showed that this regulator binds to four target sites in the divergent region located between the operons puuA and puuDR. Its regulator represses transcription by overlapping the promoters puuAp and puuDp, and the binding targets for PuuR consist of 15 nucleotides, with the following recognition sequence: AAAATATAATGAACA . The transcription of the puu genes occurs when putrescine interacts with PuuR; this effect changes the conformation of PuuR, and its regulator dissociates from the binding sites. When the level of putrescine decreases in the cell, PuuR can repress the transcription of puu genes...

## Biological Role

Repressed by puuR (protein.P0A9U6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9U6|protein.P0A9U6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `S` - regulator=PuuR; target=puuR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004371,ECOCYC:EG12431,GeneID:945886`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1361911-1362468:+; feature_type=gene
