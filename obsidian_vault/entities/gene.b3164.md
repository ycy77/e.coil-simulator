---
entity_id: "gene.b3164"
entity_type: "gene"
name: "pnp"
source_database: "NCBI RefSeq"
source_id: "gene-b3164"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3164"
  - "pnp"
---

# pnp

`gene.b3164`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3164`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pnp (gene.b3164) is a gene entity. It encodes pnp (protein.P05055). Encoded protein function: FUNCTION: Involved in mRNA degradation. Catalyzes the phosphorolysis of single-stranded polyribonucleotides processively in the 3'- to 5'-direction. Also involved, along with RNase II, in tRNA processing. RNases II and R contribute to rRNA degradation during starvation, while RNase R and PNPase are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). Contributes to degradation of some small RNAs (sRNA) (PubMed:34210798). {ECO:0000255|HAMAP-Rule:MF_01595, ECO:0000269|PubMed:12162954, ECO:0000269|PubMed:18812438, ECO:0000269|PubMed:19327365, ECO:0000269|PubMed:21135037, ECO:0000269|PubMed:34210798, ECO:0000269|PubMed:4866865, ECO:0000269|PubMed:7509797}. EcoCyc product frame: EG10743-MONOMER. EcoCyc synonyms: bfl. Genomic coordinates: 3309033-3311168.

## Biological Role

Repressed by argR (protein.P0A6D0), crp (protein.P0ACJ8). Activated by zraR (protein.P14375).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05055|protein.P05055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P14375|protein.P14375]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=pnp; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=pnp; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010397,ECOCYC:EG10743,GeneID:947672`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3309033-3311168:-; feature_type=gene
