---
entity_id: "gene.b1395"
entity_type: "gene"
name: "paaH"
source_database: "NCBI RefSeq"
source_id: "gene-b1395"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1395"
  - "paaH"
---

# paaH

`gene.b1395`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1395`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaH (gene.b1395) is a gene entity. It encodes paaH (protein.P76083). Encoded protein function: FUNCTION: Catalyzes the oxidation of 3-hydroxyadipyl-CoA to yield 3-oxoadipyl-CoA. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6716-MONOMER. EcoCyc synonyms: hbdH, ydbU. Genomic coordinates: 1459054-1460481. EcoCyc protein note: PaaH is the NAD+-dependent 3-hydroxyadipyl-CoA dehydrogenase involved in phenylacetate catabolism . A paaH mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaH: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76083|protein.P76083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaH; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaH; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaH; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004663,ECOCYC:G6716,GeneID:945940`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1459054-1460481:+; feature_type=gene
