---
entity_id: "gene.b2954"
entity_type: "gene"
name: "rdgB"
source_database: "NCBI RefSeq"
source_id: "gene-b2954"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2954"
  - "rdgB"
---

# rdgB

`gene.b2954`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2954`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rdgB (gene.b2954) is a gene entity. It encodes rdgB (protein.P52061). Encoded protein function: FUNCTION: Pyrophosphatase that catalyzes the hydrolysis of nucleoside triphosphates to their monophosphate derivatives, with a high preference for the non-canonical purine nucleotides XTP (xanthosine triphosphate), dITP (deoxyinosine triphosphate) and ITP (PubMed:12297000, PubMed:17976651). Can also efficiently hydrolyze 2'-deoxy-N-6-hydroxylaminopurine triphosphate (dHAPTP) (PubMed:17090528). Seems to function as a house-cleaning enzyme that removes non-canonical purine nucleotides from the nucleotide pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions (PubMed:12297000, PubMed:12730170, PubMed:17090528). To a much lesser extent, is also able to hydrolyze GTP, dGTP and dUTP, but shows very low activity toward the canonical nucleotides dATP, dCTP and dTTP and toward 8-oxo-dGTP, purine deoxyribose triphosphate, 2-aminopurine deoxyribose triphosphate and 2,6-diaminopurine deoxyribose triphosphate (PubMed:12297000, PubMed:17090528). {ECO:0000255|HAMAP-Rule:MF_01405, ECO:0000269|PubMed:12297000, ECO:0000269|PubMed:12730170, ECO:0000269|PubMed:17090528, ECO:0000269|PubMed:17976651}...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52061|protein.P52061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rdgB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009692,ECOCYC:G7530,GeneID:947429`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3096681-3097274:+; feature_type=gene
