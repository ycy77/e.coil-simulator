---
entity_id: "gene.b3023"
entity_type: "gene"
name: "ygiV"
source_database: "NCBI RefSeq"
source_id: "gene-b3023"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3023"
  - "ygiV"
---

# ygiV

`gene.b3023`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3023`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiV (gene.b3023) is a gene entity. It encodes ygiV (protein.Q46866). Encoded protein function: FUNCTION: Represses expression of mcbR. {ECO:0000269|PubMed:18309357}. EcoCyc product frame: G7573-MONOMER. Genomic coordinates: 3168749-3169231. EcoCyc protein note: YgiV had been predicted as a transcriptional regulator . However, based on nickel enrichment DNA microarrays and additional gel shift assays, it was identified as a transcriptional repressor of mcbR, which regulates biofilm formation and mucoidity by repressing expression of mcbA (ybiM) . In the E. coli K-12-derived strain BW25113, a ygiV knockout mutant, only a slightly increase in biofilm formation was observed, in contrast to the large decrease observed with the same mutation in the pathogenic strain UPEC CFT073 . MqsR has a toxic effect on Escherichia coli bacterial growth, which is partially reduced by the ygiV mutation . Inhibition of ygiV expression by CRISPRi reduced cellular fitness under treatment with the antibiotics pyocyanin or novobiocin .

## Biological Role

Repressed by lrp (protein.P0ACJ0), glaR (protein.P37338). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46866|protein.Q46866]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ygiV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009928,ECOCYC:G7573,GeneID:945805`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3168749-3169231:-; feature_type=gene
