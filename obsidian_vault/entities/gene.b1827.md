---
entity_id: "gene.b1827"
entity_type: "gene"
name: "kdgR"
source_database: "NCBI RefSeq"
source_id: "gene-b1827"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1827"
  - "kdgR"
---

# kdgR

`gene.b1827`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1827`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdgR (gene.b1827) is a gene entity. It encodes kdgR (protein.P76268). Encoded protein function: FUNCTION: Transcriptional repressor that negatively regulates the expression of kdgT, kdgK and kdgA, which encode proteins involved in transport and catabolism of 2-keto-3-deoxygluconate (KDG) (PubMed:4359651). Also represses expression of eda, which encodes the Entner-Doudoroff aldolase, by binding to its P2 promoter region (PubMed:15659677). {ECO:0000269|PubMed:15659677, ECO:0000269|PubMed:4359651}. EcoCyc product frame: G7003-MONOMER. EcoCyc synonyms: yebP. Genomic coordinates: 1909308-1910099. EcoCyc protein note: The "2-Keto-3-deoxygluconate repressor," KdgR, is a DNA-binding transcription factor that represses transcription of the operons involved in transport and catabolism of 2-keto-3-deoxy gluconate (KDG) . Synthesis of these genes is induced when E. coli is grown in the presence of KDG and under high-temperature conditions, between 32 and 35°C. Although little is known about the regulating mechanism of KdgR, it has been shown to act as a repressor that binds to a putative inverted repeat sequence . Comparative analysis of intergenic DNA sequences showed the consistent occurrence of KdgR possible binding sites upstream of the genes not related to the transport and catabolism of KDG . It appears that the kdgR gene undergoes adaptive mutations when E...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76268|protein.P76268]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=kdgR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006081,ECOCYC:G7003,GeneID:946129`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1909308-1910099:-; feature_type=gene
