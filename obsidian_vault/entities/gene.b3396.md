---
entity_id: "gene.b3396"
entity_type: "gene"
name: "mrcA"
source_database: "NCBI RefSeq"
source_id: "gene-b3396"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3396"
  - "mrcA"
---

# mrcA

`gene.b3396`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3396`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mrcA (gene.b3396) is a gene entity. It encodes mrcA (protein.P02918). Encoded protein function: FUNCTION: Cell wall formation. Synthesis of cross-linked peptidoglycan from the lipid intermediates. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a penicillin-sensitive transpeptidase C-terminal domain (cross-linking of the peptide subunits). {ECO:0000269|PubMed:7006606}. EcoCyc product frame: EG10748-MONOMER. EcoCyc synonyms: ponA. Genomic coordinates: 3522871-3525423. EcoCyc protein note: PBP1A, the product of the mrcA gene, is a bifunctional peptidoglycan synthase with transglycosylase and transpeptidase activity. PBP1A is implicated in cytoskeleton independent glycan synthesis in E. coli K-12; PBP1A does not exhibit any EG10608-MONOMER MreB-like directional motion . PBP1A is required for maximal fitness in alkaline conditions (pH 6.5-8.2); PBP1A activity is reduced in acidic conditions . Purified PBP1A produces murein with an average length of 20 disaccharide units and with approximately 20% of peptides involved in cross-links; purified PBP1A requires glycan polymers with monomeric peptides for transpeptidation reactions and can integrate newly synthesized glycan chains into existing sacculi...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02918|protein.P02918]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011082,ECOCYC:EG10748,GeneID:947907`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3522871-3525423:+; feature_type=gene
