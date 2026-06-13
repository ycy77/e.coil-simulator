---
entity_id: "gene.b1939"
entity_type: "gene"
name: "fliG"
source_database: "NCBI RefSeq"
source_id: "gene-b1939"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1939"
  - "fliG"
---

# fliG

`gene.b1939`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1939`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliG (gene.b1939) is a gene entity. It encodes fliG (protein.P0ABZ1). Encoded protein function: FUNCTION: FliG is one of three proteins (FliG, FliN, FliM) that forms the rotor-mounted switch complex (C ring), located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation. EcoCyc product frame: FLIG-FLAGELLAR-SWITCH-PROTEIN. EcoCyc synonyms: flaAII.2, flaBII. Genomic coordinates: 2014880-2015875. EcoCyc protein note: FliG is one of three components of the flagellar motor's "switch complex." FliG proteins consist of N-terminal (N), middle (M) and C-terminal (C) domains separated by short flexible linkers (helixNM and helixMC); the M and C domains each contain an Armadillo-repeat motif (ARMM and ARMC). FliG is monomeric in solution but forms a multimeric ring structure during assembly of the flagellar complex; FliG monomers are linked together by intermolecular ARMM-ARMC interactions; the FliG ring assembles using a domain-swap polymerization mechanism (see ). For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Repressed by pdeL (protein.P21514), csgD (protein.P52106).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABZ1|protein.P0ABZ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=fliG; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006456,ECOCYC:EG11654,GeneID:946451`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2014880-2015875:+; feature_type=gene
