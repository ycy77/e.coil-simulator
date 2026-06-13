---
entity_id: "gene.b3075"
entity_type: "gene"
name: "ebgR"
source_database: "NCBI RefSeq"
source_id: "gene-b3075"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3075"
  - "ebgR"
---

# ebgR

`gene.b3075`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3075`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ebgR (gene.b3075) is a gene entity. It encodes ebgR (protein.P06846). Encoded protein function: FUNCTION: Repressor for beta galactosidase alpha and beta subunits (ebgA and ebgC). Binds lactose as an inducer. EcoCyc product frame: PD03254. Genomic coordinates: 3221466-3222449. EcoCyc protein note: EbgR (for "evolved β-galactosidase repressor") negatively regulates genes involved in the evolved β-galactosidase system, which constitutes an alternative for lactose utilization in cells with mutations on the lacZ gene . The wild-type Ebg enzyme, encoded by the ebg operon, is not efficient enough to permit growth on lactose. Mutations in ebgR and ebgA, however, enhance its catalytic activity and enable rapid growth on lactose as a sole carbon source . Inhibition of ebgR expression by CRISPRi reduced cellular fitness under treatment with the antibiotics polymyxin B or pyocyanin . EbgR belongs to the GalR-LacI family of transcriptional regulators. There is strong evidence that the ebg and lac operons share a common origin in evolution . EbgR diverged from other repressors shortly after the divergence of the Gram positive from the Gram negative eubacteria, approximately 2.2 billion years ago...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06846|protein.P06846]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010099,ECOCYC:EG10254,GeneID:947586`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3221466-3222449:+; feature_type=gene
