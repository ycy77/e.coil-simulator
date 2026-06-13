---
entity_id: "gene.b1434"
entity_type: "gene"
name: "sutR"
source_database: "NCBI RefSeq"
source_id: "gene-b1434"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1434"
  - "sutR"
---

# sutR

`gene.b1434`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1434`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sutR (gene.b1434) is a gene entity. It encodes sutR (protein.P77626). Encoded protein function: FUNCTION: Regulates the expression of 12-16 transcription units involved in various steps of sulfur utilization. Represses expression of pfkB, fliZ, cysE, ydcO and its own expression. Activates expression of ypfN. Acts by binding to SutR boxes. {ECO:0000269|PubMed:25406449}. EcoCyc product frame: G6745-MONOMER. EcoCyc synonyms: ydcN. Genomic coordinates: 1506172-1506708. EcoCyc protein note: SutR (formely YdcN) regulates a set of genes involved in the utilization of sulfur . SutR is a small transcription factor with a helix-turn-helix (HTH) motif and belongs to the Cro-C1-type superfamily . Based on genomic SELEX screen analysis, it was identified as a highly probable regulator for 12-16 operons involved in various steps of sulfur utilization, playing an important role in the coordination of expression of the genes involved in this metabolic pathway . Genes identified by SELEX analysis include the following: paoC, xseB, thiI, ydcO, sutR, ynfG, ydiY, pfkB, fliZ, ypfN, yfgM, yfiC, tdcF, cysE, and yjcS. Four peaks were located in type A spacers of divergent transcription units (TUs), and eight peaks were identified within type B spacers upstream of one TU but downstream of the preceding TUs...

## Biological Role

Repressed by sutR (protein.P77626). Activated by sutR (protein.P77626).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77626|protein.P77626]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=sutR; function=-+
- `represses` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=sutR; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0004783,ECOCYC:G6745,GeneID:946000`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1506172-1506708:+; feature_type=gene
