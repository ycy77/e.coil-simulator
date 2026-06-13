---
entity_id: "gene.b1397"
entity_type: "gene"
name: "paaJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1397"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1397"
  - "paaJ"
---

# paaJ

`gene.b1397`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1397`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaJ (gene.b1397) is a gene entity. It encodes paaJ (protein.P0C7L2). Encoded protein function: FUNCTION: Catalyzes the thiolytic cleavage of the beta-keto C8 intermediate 3-oxo-5,6-dehydrosuberyl-CoA with CoA to yield the C6 intermediate 2,3-dehydroadipyl-CoA and acetyl-CoA. Besides it catalyzes also the last step of the pathway, in which 3-oxoadipyl-CoA similarly is cleaved to acetyl-CoA and succinyl-CoA. {ECO:0000269|PubMed:17259607, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6718-MONOMER. EcoCyc synonyms: ydbW. Genomic coordinates: 1460893-1462098. EcoCyc protein note: PaaJ is a β-ketoadipyl-CoA thiolase catalyzing two steps in phenylacetate catabolism . A paaJ mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaJ: "phenylacetic acid degradation" Review, including new consensus gene names:

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C7L2|protein.P0C7L2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaJ; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaJ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaJ; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaJ; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004668,ECOCYC:G6718,GeneID:946121`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1460893-1462098:+; feature_type=gene
