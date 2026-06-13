---
entity_id: "gene.b1387"
entity_type: "gene"
name: "paaZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1387"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1387"
  - "paaZ"
---

# paaZ

`gene.b1387`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1387`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaZ (gene.b1387) is a gene entity. It encodes paaZ (protein.P77455). Encoded protein function: FUNCTION: Catalyzes the hydrolytic ring cleavage of 2-oxepin-2(3H)-ylideneacetyl-CoA (oxepin-CoA) via the open-chain aldehyde intermediate to yield 3-oxo-5,6-dehydrosuberyl-CoA. The enzyme consists of a C-terminal (R)-specific enoyl-CoA hydratase domain (formerly MaoC) that cleaves the ring and produces the highly reactive 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde and an N-terminal NADP-dependent aldehyde dehydrogenase domain that oxidizes the aldehyde to 3-oxo-5,6-dehydrosuberyl-CoA. Can also use crotonyl-CoA as substrate. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21296885, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6708-MONOMER. EcoCyc synonyms: ydbN, maoC. Genomic coordinates: 1451597-1453642.

## Biological Role

Repressed by paaX (protein.P76086). Activated by crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77455|protein.P77455]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaZ; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=paaZ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004644,ECOCYC:G6708,GeneID:945954`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1451597-1453642:-; feature_type=gene
