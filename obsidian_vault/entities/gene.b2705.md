---
entity_id: "gene.b2705"
entity_type: "gene"
name: "srlD"
source_database: "NCBI RefSeq"
source_id: "gene-b2705"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2705"
  - "srlD"
---

# srlD

`gene.b2705`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2705`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srlD (gene.b2705) is a gene entity. It encodes srlD (protein.P05707). Encoded protein function: Sorbitol-6-phosphate 2-dehydrogenase (EC 1.1.1.140) (Glucitol-6-phosphate dehydrogenase) (Ketosephosphate reductase) EcoCyc product frame: SORB6PDEHYDROG-MONOMER. EcoCyc synonyms: gutD. Genomic coordinates: 2827737-2828516.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05707|protein.P05707]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=srlD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008896,ECOCYC:EG10971,GeneID:948937`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2827737-2828516:+; feature_type=gene
