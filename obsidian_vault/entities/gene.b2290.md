---
entity_id: "gene.b2290"
entity_type: "gene"
name: "alaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2290"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2290"
  - "alaA"
---

# alaA

`gene.b2290`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2290`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alaA (gene.b2290) is a gene entity. It encodes alaA (protein.P0A959). Encoded protein function: FUNCTION: Involved in the biosynthesis of alanine. Catalyzes the transamination of pyruvate by glutamate, leading to the formation of L-alanine and 2-oxoglutarate. Is also able to catalyze the reverse reaction. {ECO:0000269|PubMed:20729367}. EcoCyc product frame: G7184-MONOMER. EcoCyc synonyms: yfbQ. Genomic coordinates: 2407561-2408778.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A959|protein.P0A959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007560,ECOCYC:G7184,GeneID:946772`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2407561-2408778:+; feature_type=gene
