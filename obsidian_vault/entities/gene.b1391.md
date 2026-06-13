---
entity_id: "gene.b1391"
entity_type: "gene"
name: "paaD"
source_database: "NCBI RefSeq"
source_id: "gene-b1391"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1391"
  - "paaD"
---

# paaD

`gene.b1391`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1391`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaD (gene.b1391) is a gene entity. It encodes paaD (protein.P76080). Encoded protein function: FUNCTION: Possible component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit D may have a function related to the maturation of the monooxygenase complex, rather than direct involvement in catalysis. PaaD could assist either in maturation of PaaE or PaaA. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6712-MONOMER. EcoCyc synonyms: ydbQ. Genomic coordinates: 1455925-1456422. EcoCyc protein note: PaaA, PaaB, PaaC, and PaaD were predicted to be subunits of a phenylacetate-CoA oxygenase involved in phenylacetate catabolism . Recent work with the enzyme from Pseudomonas sp. has shown that the PaaA, PaaB, PaaC and PaaE polypeptides copurify as a complex when overexpressed. PaaD is not part of the complex, nor is it required for the enzymatic activity of the complex. PaaD is hypothesized to participate in the formation of a predicted iron-sulfur cluster in the PaaE subunit . PaaD: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76080|protein.P76080]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaD; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaD; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaD; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004655,ECOCYC:G6712,GeneID:945959`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1455925-1456422:+; feature_type=gene
