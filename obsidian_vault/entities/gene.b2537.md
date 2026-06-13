---
entity_id: "gene.b2537"
entity_type: "gene"
name: "hcaR"
source_database: "NCBI RefSeq"
source_id: "gene-b2537"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2537"
  - "hcaR"
---

# hcaR

`gene.b2537`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2537`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcaR (gene.b2537) is a gene entity. It encodes hcaR (protein.Q47141). Encoded protein function: FUNCTION: Transcriptional activator of the hca operon for 3-phenylpropionic acid catabolism. EcoCyc product frame: G7331-MONOMER. EcoCyc synonyms: phdR, yfhT. Genomic coordinates: 2668006-2668896.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), C0293 (gene.b4806), fur (protein.P0A9A9), hcaR (protein.Q47141). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47141|protein.Q47141]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hcaR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4806|gene.b4806]] `RegulonDB` `S` - regulator=C0293; target=hcaR; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=hcaR; function=-
- `represses` <-- [[protein.Q47141|protein.Q47141]] `RegulonDB` `S` - regulator=HcaR; target=hcaR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008351,ECOCYC:G7331,GeneID:947000`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2668006-2668896:-; feature_type=gene
