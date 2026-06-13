---
entity_id: "gene.b1890"
entity_type: "gene"
name: "motA"
source_database: "NCBI RefSeq"
source_id: "gene-b1890"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1890"
  - "motA"
---

# motA

`gene.b1890`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1890`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

motA (gene.b1890) is a gene entity. It encodes motA (protein.P09348). Encoded protein function: FUNCTION: MotA and MotB comprise the stator element of the flagellar motor complex. Required for rotation of the flagellar motor. Probable transmembrane proton channel. Overexpression of MotA, with or without MotB, restores motility in a pdeH disruption, (a c-di-GMP phosphodiesterase) suggesting there is an interaction (direct or indirect) between the c-di-GMP-binding flagellar brake protein YcgR and the flagellar stator. {ECO:0000269|PubMed:20346719}. EcoCyc product frame: MOTA-FLAGELLAR-MOTOR-STATOR-PROTEIN. EcoCyc synonyms: flaJ. Genomic coordinates: 1976252-1977139. EcoCyc protein note: MotA and MOTB-FLAGELLAR-MOTOR-STATOR-PROTEIN MotB comprise the stator unit of the flagellar motor complex; MotAB complexes are anchored in the peptidoglycan and form a proton conducting channel across the inner membrane; movement of protons down their concentration gradient via the stator provides the energy for torque generation in the flagellar motor. Early studies in E. coli K-12 derived strains characterized mot mutants which are paralysed (cells possess flagella but are non-motile) and defined the 'Mocha' operon which includes the motA, motB and cheA cistrons . Inducing expression of cloned, wild-type motA restores torque to paralysed motA mutants...

## Biological Role

Repressed by cpxR (protein.P0AE88).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09348|protein.P09348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=motA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006299,ECOCYC:EG10601,GeneID:947564`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1976252-1977139:-; feature_type=gene
