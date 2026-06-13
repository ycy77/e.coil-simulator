---
entity_id: "gene.b0581"
entity_type: "gene"
name: "ybdK"
source_database: "NCBI RefSeq"
source_id: "gene-b0581"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0581"
  - "ybdK"
---

# ybdK

`gene.b0581`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0581`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdK (gene.b0581) is a gene entity. It encodes ybdK (protein.P77213). Encoded protein function: FUNCTION: ATP-dependent carboxylate-amine ligase which exhibits weak glutamate--cysteine ligase activity. However, because of the low catalytic rate, the question remains whether L-cysteine is the actual biological substrate. {ECO:0000255|HAMAP-Rule:MF_01609, ECO:0000269|PubMed:15211520}. EcoCyc product frame: G6326-MONOMER. Genomic coordinates: 606265-607383.

## Biological Role

Repressed by nac (protein.Q47005). Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77213|protein.P77213]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybdK; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybdK; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0001992,ECOCYC:G6326,GeneID:947246`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:606265-607383:-; feature_type=gene
