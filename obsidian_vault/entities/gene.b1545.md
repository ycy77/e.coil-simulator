---
entity_id: "gene.b1545"
entity_type: "gene"
name: "pinQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1545"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1545"
  - "pinQ"
---

# pinQ

`gene.b1545`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1545`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pinQ (gene.b1545) is a gene entity. It encodes pinQ (protein.P77170). Encoded protein function: Serine recombinase PinQ (EC 3.1.22.-) (EC 6.5.1.-) (DNA-invertase PinQ) (Putative DNA-invertase from lambdoid prophage Qin) (Site-specific recombinase PinQ) EcoCyc product frame: G6819-MONOMER. EcoCyc synonyms: ydfL. Genomic coordinates: 1633622-1634212. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 6, 2020.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77170|protein.P77170]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=pinQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005164,ECOCYC:G6819,GeneID:946088`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1633622-1634212:+; feature_type=gene
