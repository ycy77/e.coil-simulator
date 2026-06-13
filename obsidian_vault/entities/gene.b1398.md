---
entity_id: "gene.b1398"
entity_type: "gene"
name: "paaK"
source_database: "NCBI RefSeq"
source_id: "gene-b1398"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1398"
  - "paaK"
---

# paaK

`gene.b1398`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1398`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaK (gene.b1398) is a gene entity. It encodes paaK (protein.P76085). Encoded protein function: FUNCTION: Catalyzes the activation of phenylacetic acid (PA) to phenylacetyl-CoA (PA-CoA). {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6719-MONOMER. Genomic coordinates: 1462125-1463438. EcoCyc protein note: PaaK has been shown to have phenylacetate-CoA ligase activity in E. coli W. There, the enzyme catalyzes the first step in an aerobic pathway of phenylacetate degradation . Additional steps in the phenylacetate degradation pathway have been predicted and recently experimentally studied . Some, but not all, E. coli K-12 strains are able to utilize phenylacetate as the sole source of carbon and energy. The E. coli K-12 strains MG1655 and W3110 as well as E. coli W exhibit utilization, while E. coli C does not exhibit utilization due to deletion of a large fragment that includes the paa region . PaaK: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76085|protein.P76085]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaK; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaK; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaK; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaK; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004671,ECOCYC:G6719,GeneID:945963`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1462125-1463438:+; feature_type=gene
