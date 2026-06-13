---
entity_id: "gene.b1942"
entity_type: "gene"
name: "fliJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1942"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1942"
  - "fliJ"
---

# fliJ

`gene.b1942`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1942`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliJ (gene.b1942) is a gene entity. It encodes fliJ (protein.P52613). Encoded protein function: FUNCTION: The FliJ protein is a flagellar protein that affects chemotactic events. Mutations in FliJ results in failure to respond to chemotactic stimuli. EcoCyc product frame: G378-MONOMER. EcoCyc synonyms: flaO. Genomic coordinates: 2017946-2018389. EcoCyc protein note: FliJ is one of three soluble components of the flagellar export system, along with FliH and FliI . FliJ has several feature similarities with the type III cytoplasmic chaperone family .

## Biological Role

Repressed by pdeL (protein.P21514), csgD (protein.P52106).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52613|protein.P52613]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=fliJ; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006462,ECOCYC:G378,GeneID:946454`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2017946-2018389:+; feature_type=gene
