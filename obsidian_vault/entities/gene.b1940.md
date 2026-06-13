---
entity_id: "gene.b1940"
entity_type: "gene"
name: "fliH"
source_database: "NCBI RefSeq"
source_id: "gene-b1940"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1940"
  - "fliH"
---

# fliH

`gene.b1940`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1940`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliH (gene.b1940) is a gene entity. It encodes fliH (protein.P31068). Encoded protein function: FUNCTION: Needed for flagellar regrowth and assembly. EcoCyc product frame: EG11656-MONOMER. EcoCyc synonyms: flaAII.3, flaBIII. Genomic coordinates: 2015868-2016554. EcoCyc protein note: FliH is a cytoplasmic protein which exists as a dimer in solution and forms a stable heterotrimeric complex with FliI, inhibiting its ATPase activity .

## Biological Role

Repressed by pdeL (protein.P21514), csgD (protein.P52106).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31068|protein.P31068]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=fliH; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006458,ECOCYC:EG11656,GeneID:946456`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2015868-2016554:+; feature_type=gene
