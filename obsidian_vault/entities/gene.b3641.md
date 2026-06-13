---
entity_id: "gene.b3641"
entity_type: "gene"
name: "slmA"
source_database: "NCBI RefSeq"
source_id: "gene-b3641"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3641"
  - "slmA"
---

# slmA

`gene.b3641`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3641`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

slmA (gene.b3641) is a gene entity. It encodes slmA (protein.P0C093). Encoded protein function: FUNCTION: Required for nucleoid occlusion (NO) phenomenon, which prevents Z-ring formation and cell division over the nucleoid. Acts as a DNA-associated cell division inhibitor that binds simultaneously chromosomal DNA and FtsZ, and disrupts the assembly of FtsZ polymers. SlmA-DNA-binding sequences (SBS) are dispersed on non-Ter regions of the chromosome, preventing FtsZ polymerization at these regions. {ECO:0000255|HAMAP-Rule:MF_01839, ECO:0000269|PubMed:15916962, ECO:0000269|PubMed:21113127, ECO:0000269|PubMed:21321206}. EcoCyc product frame: EG11191-MONOMER. EcoCyc synonyms: yicB, ttk. Genomic coordinates: 3814494-3815090.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C093|protein.P0C093]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011902,ECOCYC:EG11191,GeneID:948158`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3814494-3815090:+; feature_type=gene
