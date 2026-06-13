---
entity_id: "gene.b1388"
entity_type: "gene"
name: "paaA"
source_database: "NCBI RefSeq"
source_id: "gene-b1388"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1388"
  - "paaA"
---

# paaA

`gene.b1388`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1388`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaA (gene.b1388) is a gene entity. It encodes paaA (protein.P76077). Encoded protein function: FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit A is the catalytic subunit involved in the incorporation of one atom of molecular oxygen into phenylacetyl-CoA. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21247899, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6709-MONOMER. EcoCyc synonyms: ydbO. Genomic coordinates: 1453927-1454856. EcoCyc protein note: PaaA is the catalytic α subunit of the catalytic core of the enzyme . PaaA has similarity to the large (α) subunit of diiron monooxygenase complexes . PaaA: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76077|protein.P76077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaA; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaA; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaA; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004649,ECOCYC:G6709,GeneID:945833`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1453927-1454856:+; feature_type=gene
