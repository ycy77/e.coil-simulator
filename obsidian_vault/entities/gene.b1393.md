---
entity_id: "gene.b1393"
entity_type: "gene"
name: "paaF"
source_database: "NCBI RefSeq"
source_id: "gene-b1393"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1393"
  - "paaF"
---

# paaF

`gene.b1393`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1393`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaF (gene.b1393) is a gene entity. It encodes paaF (protein.P76082). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of enzymatically produced 2,3-dehydroadipyl-CoA into 3-hydroxyadipyl-CoA. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6714-MONOMER. EcoCyc synonyms: ydbR, ydbS. Genomic coordinates: 1457497-1458264. EcoCyc protein note: PaaF is a predicted 2,3-dehydroadipyl-CoA hydratase involved in phenylacetate catabolism. The enzyme from Pseudomonas sp. strain Y2 has been biochemically characterized . A paaF mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaF: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76082|protein.P76082]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaF; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaF; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaF; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaF; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004659,ECOCYC:G6714,GeneID:946011`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1457497-1458264:+; feature_type=gene
