---
entity_id: "gene.b0091"
entity_type: "gene"
name: "murC"
source_database: "NCBI RefSeq"
source_id: "gene-b0091"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0091"
  - "murC"
---

# murC

`gene.b0091`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0091`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murC (gene.b0091) is a gene entity. It encodes murC (protein.P17952). Encoded protein function: FUNCTION: Cell wall formation. {ECO:0000269|PubMed:7601127}. EcoCyc product frame: UDP-NACMUR-ALA-LIG-MONOMER. Genomic coordinates: 100765-102240.

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17952|protein.P17952]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=murC; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=murC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000324,ECOCYC:EG10619,GeneID:946153`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:100765-102240:+; feature_type=gene
