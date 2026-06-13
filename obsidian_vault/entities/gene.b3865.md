---
entity_id: "gene.b3865"
entity_type: "gene"
name: "yihA"
source_database: "NCBI RefSeq"
source_id: "gene-b3865"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3865"
  - "yihA"
---

# yihA

`gene.b3865`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3865`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihA (gene.b3865) is a gene entity. It encodes engB (protein.P0A6P7). Encoded protein function: FUNCTION: Necessary for normal cell division and for the maintenance of normal septation. Depletion of this protein leads to a severe reduction in growth rate and to extensive filamentation, with a block beyond the stage of segregation. Essential for bacteria survival. {ECO:0000255|HAMAP-Rule:MF_00321, ECO:0000269|PubMed:10572302}. EcoCyc product frame: EG11203-MONOMER. EcoCyc synonyms: engB. Genomic coordinates: 4050133-4050765. EcoCyc protein note: YihA is essential for normal cell division . YihA is the founding member of a family of putative GTPases . Depletion causes late-stage cell cycle arrest with filamentous cell morphology, indicative of a defect in cell division . This filamentation is partially suppressed by FtsZ overproduction and is suppressed by FtsQI, FtsA, and FtsZ co-overproduction . YihA shows conserved GTPase motifs, indicating that YihA may have GTPase activity . Purified YihA protein specifically binds guanine nucleotides and has extremely low GTPase activity; mutational studies confirm that the predicted GTP-binding domain is involved in nucleotide binding . Reviews:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6P7|protein.P0A6P7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012623,ECOCYC:EG11203,GeneID:948358`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4050133-4050765:-; feature_type=gene
