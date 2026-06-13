---
entity_id: "gene.b3211"
entity_type: "gene"
name: "yhcC"
source_database: "NCBI RefSeq"
source_id: "gene-b3211"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3211"
  - "yhcC"
---

# yhcC

`gene.b3211`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3211`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhcC (gene.b3211) is a gene entity. It encodes yhcC (protein.P0ADW6). Encoded protein function: FUNCTION: In vitro, can cleave S-adenosyl-L-methionine into methionine and 5'-deoxyadenosine (AdoH). {ECO:0000269|PubMed:25117543}. EcoCyc product frame: G7669-MONOMER. Genomic coordinates: 3353121-3354050. EcoCyc protein note: Purified YhcC can be reconstituted to contain a 4Fe-4S cluster. In support of its annotation as a radical SAM enzyme, the Fe-S cluster-containing enzyme catalyzes the reductive cleavage of S-adenosylmethionine to methionine and 5'-deoxyadenosine . Review:

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADW6|protein.P0ADW6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhcC; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=yhcC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010540,ECOCYC:G7669,GeneID:947733`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3353121-3354050:-; feature_type=gene
