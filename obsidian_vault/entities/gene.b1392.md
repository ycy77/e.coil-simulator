---
entity_id: "gene.b1392"
entity_type: "gene"
name: "paaE"
source_database: "NCBI RefSeq"
source_id: "gene-b1392"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1392"
  - "paaE"
---

# paaE

`gene.b1392`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1392`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaE (gene.b1392) is a gene entity. It encodes paaE (protein.P76081). Encoded protein function: FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit E is a reductase with a preference for NADPH and FAD, capable of reducing cytochrome c. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21247899, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6713-MONOMER. EcoCyc synonyms: ydbR. Genomic coordinates: 1456430-1457500. EcoCyc protein note: PaaE has similarity to class IA-like reductases, members of the ferredoxin-NADP+ reductase (FNR) family of proteins . PaaE carries a [2Fe-2S] cluster similar to that of spinach ferredoxin . PaaE: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76081|protein.P76081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaE; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaE; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaE; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004657,ECOCYC:G6713,GeneID:945962`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1456430-1457500:+; feature_type=gene
