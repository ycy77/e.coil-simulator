---
entity_id: "gene.b0928"
entity_type: "gene"
name: "aspC"
source_database: "NCBI RefSeq"
source_id: "gene-b0928"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0928"
  - "aspC"
---

# aspC

`gene.b0928`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0928`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aspC (gene.b0928) is a gene entity. It encodes aspC (protein.P00509). Encoded protein function: Aspartate aminotransferase (AspAT) (EC 2.6.1.1) (Transaminase A) EcoCyc product frame: ASPAMINOTRANS-MONOMER. Genomic coordinates: 984519-985709.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00509|protein.P00509]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003150,ECOCYC:EG10096,GeneID:945553`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:984519-985709:-; feature_type=gene
