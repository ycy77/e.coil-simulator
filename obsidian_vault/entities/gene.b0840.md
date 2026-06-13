---
entity_id: "gene.b0840"
entity_type: "gene"
name: "deoR"
source_database: "NCBI RefSeq"
source_id: "gene-b0840"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0840"
  - "deoR"
---

# deoR

`gene.b0840`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0840`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

deoR (gene.b0840) is a gene entity. It encodes deoR (protein.P0ACK5). Encoded protein function: FUNCTION: This protein is one of the repressors that regulate the expression of deoCABD genes, which encode nucleotide and deoxy ribonucleotide catabolizing enzymes. It also negatively regulates the expression of nupG (a transport protein) and tsx (a pore-forming protein). The inducer is deoxyribose-5-phosphate. EcoCyc product frame: PD01196. EcoCyc synonyms: nucR. Genomic coordinates: 881976-882734. EcoCyc protein note: The transcriptional repressor DeoR, for "Deoxyribose Regulator," is involved in the negative expression of genes related to transport and catabolism of deoxyribonucleoside nucleotides . A transposon insertion mutation in the deoR gene produces cellular susceptibility to the antibiotic trimethoprim . On the other hand, inhibition of deoR expression by CRISPRi reduced cellular fitness under treatment with the antibiotic carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . DeoR belongs to the DeoR family of transcriptional regulators . This protein consists of two domains, an amino-terminal domain that contains a potential helix-turn-helix DNA-binding motif and a carboxy-terminal domain involved in the oligomerization and the recognition of a possible co-inducer...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACK5|protein.P0ACK5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002862,ECOCYC:EG10223,GeneID:945453`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:881976-882734:-; feature_type=gene
