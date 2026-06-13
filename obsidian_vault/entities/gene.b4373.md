---
entity_id: "gene.b4373"
entity_type: "gene"
name: "rimI"
source_database: "NCBI RefSeq"
source_id: "gene-b4373"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4373"
  - "rimI"
---

# rimI

`gene.b4373`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4373`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimI (gene.b4373) is a gene entity. It encodes rimI (protein.P0A944). Encoded protein function: FUNCTION: Acetylates the N-terminal alanine of ribosomal protein bS18 (PubMed:2828880, PubMed:6991870). Also acts as a N-epsilon-lysine acetyltransferase that catalyzes acetylation of several proteins (PubMed:30352934). {ECO:0000269|PubMed:2828880, ECO:0000269|PubMed:30352934, ECO:0000269|PubMed:6991870}. EcoCyc product frame: EG10850-MONOMER. Genomic coordinates: 4608185-4608631. EcoCyc protein note: RimI is an alanine acetyltransferase that is specific for EG10917-MONOMER . It also functions as an Nε-lysine acetyltransferase that targets 14 unique lysine residues in 11 unique proteins . A rimI mutant exhibits a defect in acetylation of the N-terminal alanine of ribosomal protein S18, but shows no defect in acetylation of ribosomal proteins S5 or L12 . Overexpression of RimI in an acetylation-gutted strain (Δ pta patZ acs cobB) leads to the appearance of acetylated proteins in an anti-acetyllysine Western blot. Mutagenesis of a predicted catalytic residue in RimI, Y115A, eliminates the acetylation signal observed with the wild-type protein . RimI and RimJ share C-terminal similarity .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A944|protein.P0A944]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014342,ECOCYC:EG10850,GeneID:948894`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4608185-4608631:+; feature_type=gene
