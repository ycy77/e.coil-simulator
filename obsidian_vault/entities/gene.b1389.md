---
entity_id: "gene.b1389"
entity_type: "gene"
name: "paaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1389"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1389"
  - "paaB"
---

# paaB

`gene.b1389`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1389`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaB (gene.b1389) is a gene entity. It encodes paaB (protein.P76078). Encoded protein function: FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit B may play a regulatory role or be directly involved in electron transport. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6710-MONOMER. EcoCyc synonyms: ynbF. Genomic coordinates: 1454868-1455155. EcoCyc protein note: PaaB has similarity to the activator protein of diiron monooxygenase complexes . PaaB: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76078|protein.P76078]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaB; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaB; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaB; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004651,ECOCYC:G6710,GeneID:947595`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1454868-1455155:+; feature_type=gene
