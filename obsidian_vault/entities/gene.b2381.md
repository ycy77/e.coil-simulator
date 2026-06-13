---
entity_id: "gene.b2381"
entity_type: "gene"
name: "pyrR"
source_database: "NCBI RefSeq"
source_id: "gene-b2381"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2381"
  - "pyrR"
---

# pyrR

`gene.b2381`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2381`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrR (gene.b2381) is a gene entity. It encodes ypdB (protein.P0AE39). Encoded protein function: FUNCTION: Member of the two-component regulatory system YpdA/YpdB, which is part of a nutrient-sensing regulatory network composed of YpdA/YpdB, the high-affinity pyruvate signaling system BtsS/BtsR and their respective target proteins, YhjX and BtsT. YpdB regulates expression of yhjX by binding to its promoter region. Activation of the YpdA/YpdB signaling cascade also promotes BtsS/BtsR-mediated btsT expression. {ECO:0000269|PubMed:23222720, ECO:0000269|PubMed:24659770}. EcoCyc product frame: MONOMER0-4288. EcoCyc synonyms: ypdB. Genomic coordinates: 2500383-2501117. EcoCyc protein note: Based on genomic SELEX (gSELEX) screening, gel shift assay, and reporter assay, it was determined that PyrR is a dual regulator that acts as an activator for yhjX and yhcC and as a repressor for six other targets (pbpC, yfjD, gltBC, yghW, astCADBE, and xthA) . There is unique cross-talk between low-affinity PyrSR and high-affinity BtsSR, which control the same exometabolite (pyruvate) but different sets of targets for pyruvate uptake and reutilization . A mutant with deletion of both ypdA and ypdB does not show a significant phenotype when measured by phenotype microarray . While wild-type E...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE39|protein.P0AE39]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007857,ECOCYC:G7244,GeneID:947395`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2500383-2501117:+; feature_type=gene
