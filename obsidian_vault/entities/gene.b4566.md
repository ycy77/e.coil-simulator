---
entity_id: "gene.b4566"
entity_type: "gene"
name: "topAI"
source_database: "NCBI RefSeq"
source_id: "gene-b4566"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4566"
  - "topAI"
---

# topAI

`gene.b4566`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4566`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

topAI (gene.b4566) is a gene entity. It encodes yjhX (protein.Q2EEU2). Encoded protein function: UPF0386 protein YjhX EcoCyc product frame: MONOMER0-2695. EcoCyc synonyms: yjhX. Genomic coordinates: 4533796-4534053. EcoCyc protein note: Overexpression of TopAI is toxic; concurrent expression of YjhQ relieves TopAI toxicity. TopAI directly interacts with a DNA-EG11013-MONOMER complex and inhibits topoisomerase activity. topAI and G7917 genes encode a type II toxin-antitoxin system . topAI is translationally repressed and has a long upstream region with a Rho utilization (Rut) sequence which can be occupied by Rho when translation is repressed. Upregulation of topAI occurs as a result of mutations in the EG10845 gene or mutations in 23S rRNA (specifically in domain IV, helix 69 or in domain V, helix 80). Translational stress, such as the presence of ribosome-targeting antibiotics, can also alleviate the translational repression. A small RNA upstream of the topAI gene (named G0-17140) was identified as a cis-acting regulatory element that is required for inducing expression of the TopAI operon in the presence of ribosome-targeting antibiotics . TopAI: "TopA inhibitor"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2EEU2|protein.Q2EEU2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285087,ECOCYC:G0-10473,GeneID:1450297`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4533796-4534053:-; feature_type=gene
