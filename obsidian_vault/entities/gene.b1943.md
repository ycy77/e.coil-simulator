---
entity_id: "gene.b1943"
entity_type: "gene"
name: "fliK"
source_database: "NCBI RefSeq"
source_id: "gene-b1943"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1943"
  - "fliK"
---

# fliK

`gene.b1943`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1943`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliK (gene.b1943) is a gene entity. It encodes fliK (protein.P52614). Encoded protein function: FUNCTION: Controls the length of the flagellar hook. EcoCyc product frame: G379-MONOMER. EcoCyc synonyms: flaE. Genomic coordinates: 2018386-2019513. EcoCyc protein note: FliK is a soluble component of the flagellar export apparatus. FliK has been shown to coordinate (in conjunction with FlhB) switching of substrate specificity of the export apparatus from rod/hook-type proteins to filament-type proteins . Upon completion of the flagellar hook structure, the C-terminal domain of FliK is able to communicate (though perhaps not directly) with the C-terminal cytoplasmic domain of integral membrane protein FlhB . This causes a change in subdomain interactions within FlhB which results in switching of export substrate specificity .

## Biological Role

Repressed by pdeL (protein.P21514), csgD (protein.P52106).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52614|protein.P52614]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=fliK; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006464,ECOCYC:G379,GeneID:946449`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2018386-2019513:+; feature_type=gene
