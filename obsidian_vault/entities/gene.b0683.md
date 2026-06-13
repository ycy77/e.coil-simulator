---
entity_id: "gene.b0683"
entity_type: "gene"
name: "fur"
source_database: "NCBI RefSeq"
source_id: "gene-b0683"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0683"
  - "fur"
---

# fur

`gene.b0683`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0683`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fur (gene.b0683) is a gene entity. It encodes fur (protein.P0A9A9). Encoded protein function: FUNCTION: Acts as a global negative controlling element, employing Fe(2+) as a cofactor to bind the operator of the repressed genes. Regulates the expression of several outer-membrane proteins including the iron transport operon. {ECO:0000269|PubMed:2823881}. EcoCyc product frame: PD00260. Genomic coordinates: 710200-710646.

## Biological Role

Repressed by ryhB (gene.b4451), fur (protein.P0A9A9). Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), crp (protein.P0ACJ8), oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9A9|protein.P0A9A9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fur; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=fur; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fur; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=fur; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=fur; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=fur; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002327,ECOCYC:EG10359,GeneID:945295`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:710200-710646:-; feature_type=gene
