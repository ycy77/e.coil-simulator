---
entity_id: "gene.b2220"
entity_type: "gene"
name: "atoC"
source_database: "NCBI RefSeq"
source_id: "gene-b2220"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2220"
  - "atoC"
---

# atoC

`gene.b2220`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2220`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atoC (gene.b2220) is a gene entity. It encodes atoC (protein.Q06065). Encoded protein function: FUNCTION: Member of the two-component regulatory system AtoS/AtoC. In the presence of acetoacetate, AtoS/AtoC stimulates the expression of the atoDAEB operon, leading to short chain fatty acid catabolism and activation of the poly-(R)-3-hydroxybutyrate (cPHB) biosynthetic pathway. Also induces the operon in response to spermidine (PubMed:16153782, PubMed:16564134, PubMed:17475408, PubMed:2883171). Involved in the regulation of motility and chemotaxis, via transcriptional induction of the flagellar regulon (PubMed:22083893). AtoC acts by binding directly to the promoter region of the target genes (PubMed:17616594). In addition to its role as a transcriptional regulator, functions as a post-translational regulator that inhibits polyamine biosynthesis via regulation of ornithine decarboxylase (ODC) (PubMed:8346225). {ECO:0000269|PubMed:16153782, ECO:0000269|PubMed:16564134, ECO:0000269|PubMed:17475408, ECO:0000269|PubMed:17616594, ECO:0000269|PubMed:22083893, ECO:0000269|PubMed:2883171, ECO:0000269|PubMed:8346225}. EcoCyc product frame: PHOSPHO-ATOC. Genomic coordinates: 2321866-2323251. EcoCyc protein note: AtoC, also known as antizyme protein (Az), is a protein that regulates processes at the transcriptional and posttranslational levels...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q06065|protein.Q06065]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007343,ECOCYC:EG11668,GeneID:947444`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2321866-2323251:+; feature_type=gene
