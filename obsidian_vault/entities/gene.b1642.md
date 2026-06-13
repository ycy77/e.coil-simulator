---
entity_id: "gene.b1642"
entity_type: "gene"
name: "slyA"
source_database: "NCBI RefSeq"
source_id: "gene-b1642"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1642"
  - "slyA"
---

# slyA

`gene.b1642`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1642`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

slyA (gene.b1642) is a gene entity. It encodes slyA (protein.P0A8W2). Encoded protein function: FUNCTION: Transcription regulator that can specifically activate or repress expression of target genes. Activates expression of genes such as molecular chaperones (groL, groS, dnaK, grpE, and cbpA), proteins involved in acid resistance (hdeA, hdeB, and gadA), the starvation lipoprotein slp, virulence protein hlyE/clyA. Represses expression of genes involved in the histidine biosynthetic pathway such as hisA, hisB, hisD, hisF and hisG. Required for the activation of virulence genes. {ECO:0000255|HAMAP-Rule:MF_01819, ECO:0000269|PubMed:11053378, ECO:0000269|PubMed:12057949, ECO:0000269|PubMed:8861216}. EcoCyc product frame: G6882-MONOMER. Genomic coordinates: 1720390-1720824.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by slyA (protein.P0A8W2), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8W2|protein.P0A8W2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=slyA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005495,ECOCYC:G6882,GeneID:946167`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1720390-1720824:-; feature_type=gene
