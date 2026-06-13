---
entity_id: "gene.b1394"
entity_type: "gene"
name: "paaG"
source_database: "NCBI RefSeq"
source_id: "gene-b1394"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1394"
  - "paaG"
---

# paaG

`gene.b1394`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1394`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaG (gene.b1394) is a gene entity. It encodes paaG (protein.P77467). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of the epoxide to 2-oxepin-2(3H)-ylideneacetyl-CoA (oxepin-CoA). {ECO:0000269|PubMed:12846838, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6715-MONOMER. EcoCyc synonyms: ydbT. Genomic coordinates: 1458264-1459052. EcoCyc protein note: PaaG is the predicted oxepin-CoA-forming ring 1,2-epoxyphenylacetyl-CoA isomerase involved in phenylacetate catabolism. The enzyme from Pseudomonas sp. strain Y2 has been biochemically characterized . A paaG mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaG: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77467|protein.P77467]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaG; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaG; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaG; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaG; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004661,ECOCYC:G6715,GeneID:946263`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1458264-1459052:+; feature_type=gene
