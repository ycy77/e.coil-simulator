---
entity_id: "gene.b2883"
entity_type: "gene"
name: "guaD"
source_database: "NCBI RefSeq"
source_id: "gene-b2883"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2883"
  - "guaD"
---

# guaD

`gene.b2883`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2883`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

guaD (gene.b2883) is a gene entity. It encodes guaD (protein.P76641). Encoded protein function: FUNCTION: Catalyzes the hydrolytic deamination of guanine, producing xanthine and ammonia. {ECO:0000269|PubMed:10913105}. EcoCyc product frame: G7502-MONOMER. EcoCyc synonyms: ygfP. Genomic coordinates: 3025766-3027085. EcoCyc protein note: Guanine deaminase is an aminohydrolase that converts guanine to xanthine and ammonia. This reaction removes guanine from the pool of guanine-containing metabolites, which helps to regulate cellular GTP and the guanylate nucleotide pool. Ammeline is an intermediate in the metabolism of melamine (see the MetaCyc pathway for PWY-5170). E. coli is able to metabolize ammeline to ammelide, but does not metabolize either melamine or ammelide. A guaD deletion mutant is deficient in ammeline deaminase activity .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76641|protein.P76641]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009465,ECOCYC:G7502,GeneID:947366`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3025766-3027085:+; feature_type=gene
