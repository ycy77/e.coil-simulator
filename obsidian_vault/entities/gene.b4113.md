---
entity_id: "gene.b4113"
entity_type: "gene"
name: "basR"
source_database: "NCBI RefSeq"
source_id: "gene-b4113"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4113"
  - "basR"
---

# basR

`gene.b4113`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4113`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

basR (gene.b4113) is a gene entity. It encodes basR (protein.P30843). Encoded protein function: FUNCTION: Member of the two-component regulatory system BasS/BasR. BasR induces the transcription of the ugd, ais, arnBCADTEF and eptA-basRS loci, all involved in resistance to polymyxin (By similarity). {ECO:0000250}. EcoCyc product frame: PHOSPHO-BASR. EcoCyc synonyms: pmrA. Genomic coordinates: 4333282-4333950. EcoCyc protein note: The transcriptional regulatory protein BasR appears to be involved in resistance to colistin and to the bacteriocin plantaricin BM-1 . Proteome analysis suggested that BasR directly or indirectly represses the expression of 26 proteins and activates the expression of 58 proteins involved in several cellular processes, including the tricarboxylic acid cycle . BasR is part of the two-component BasS/BasR signal transduction system . BasS functions as a membrane-associated protein kinase that phosphorylates BasR in response to elevated levels of Fe(III) which can permeabilize the outer membrane and result in cell death . Phosphorylation of BasR increases the affinity for its specific DNA binding sites, leading to the transcriptional expression of several genes involved in modification of lipopolysaccharide to prevent excessiveFe(III) binding . basR expression is necessary for lipid A modifications when E. coli is grown in low concentrations of Mg2+...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30843|protein.P30843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013466,ECOCYC:EG11615,GeneID:948631`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4333282-4333950:-; feature_type=gene
