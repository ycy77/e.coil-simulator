---
entity_id: "gene.b3535"
entity_type: "gene"
name: "yhjR"
source_database: "NCBI RefSeq"
source_id: "gene-b3535"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3535"
  - "yhjR"
---

# yhjR

`gene.b3535`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3535`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhjR (gene.b3535) is a gene entity. It encodes yhjR (protein.P0ADJ3). Encoded protein function: Protein YhjR EcoCyc product frame: EG12262-MONOMER. EcoCyc synonyms: bcsR. Genomic coordinates: 3695997-3696185. EcoCyc protein note: In the commensal cellulose-producing E. coli strain 1094, report that yhjR is not necessary for cellulose production while report that it is essential for cellulose secretion. In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology. A ΔyhjR mutation introduced into this strain leads to loss of cellulose biosynthesis (see also ). Related review:

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADJ3|protein.P0ADJ3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yhjR; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011551,ECOCYC:EG12262,GeneID:948051`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3695997-3696185:-; feature_type=gene
