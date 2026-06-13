---
entity_id: "gene.b1889"
entity_type: "gene"
name: "motB"
source_database: "NCBI RefSeq"
source_id: "gene-b1889"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1889"
  - "motB"
---

# motB

`gene.b1889`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1889`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

motB (gene.b1889) is a gene entity. It encodes motB (protein.P0AF06). Encoded protein function: FUNCTION: MotA and MotB comprise the stator element of the flagellar motor complex. Required for the rotation of the flagellar motor. Probably a linker that fastens the torque-generating machinery to the cell wall. Overexpression of this protein with MotA improves motility in a pdeH disruption, (a c-di-GMP phosphodiesterase) suggesting there is an interaction (direct or indirect) between the c-di-GMP-binding flagellar brake protein YcgR and the flagellar stator. {ECO:0000269|PubMed:20346719}. EcoCyc product frame: MOTB-FLAGELLAR-MOTOR-STATOR-PROTEIN. EcoCyc synonyms: flaJ. Genomic coordinates: 1975329-1976255. EcoCyc protein note: MotB and MOTA-FLAGELLAR-MOTOR-STATOR-PROTEIN MotA comprise the stator element of the flagellar motor complex. MotAB complexes are anchored in the peptidoglycan and form a proton conducting channel across the inner membrane; movement of protons down their concentration gradient via the stator provides the energy for torque generation in the flagellar motor. Early studies in E. coli K-12 derived strains characterized mot mutants which are paralysed (cells possess flagella but are non-motile) and defined the 'Mocha' operon which includes the motA, motB and cheA cistrons...

## Biological Role

Repressed by cpxR (protein.P0AE88).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF06|protein.P0AF06]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=motB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006297,ECOCYC:EG10602,GeneID:946402`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1975329-1976255:-; feature_type=gene
