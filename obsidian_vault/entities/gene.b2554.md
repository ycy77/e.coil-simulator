---
entity_id: "gene.b2554"
entity_type: "gene"
name: "glrR"
source_database: "NCBI RefSeq"
source_id: "gene-b2554"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2554"
  - "glrR"
---

# glrR

`gene.b2554`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2554`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glrR (gene.b2554) is a gene entity. It encodes glrR (protein.P0AFU4). Encoded protein function: FUNCTION: Member of the two-component regulatory system GlrR/GlrK that up-regulates transcription of the glmY sRNA when cells enter the stationary growth phase. Regulates glmY transcription by binding to three conserved sites in the purL-glmY intergenic region. {ECO:0000269|PubMed:19843219}. EcoCyc product frame: MONOMER0-4147. EcoCyc synonyms: yfhA, qseF. Genomic coordinates: 2687469-2688803. EcoCyc protein note: GlrR is the response regulator of the two-component GlrKR signal transduction system, and it has extensive homology to the NtrC family of activators . GlrR contains a σ54 interaction domain which binds to a DNA region located more than 100bp upstream of glmY. Transcription of a glmY-lacZ fusion from the σ54 promoter is abolished in a GlrR null strain. In an indirect way, GlrR negatively regulates genes involved in the synthesis of inorganic polyphosphate (polyP) . Inhibition of glrR expression by CRISPRi reduced cellular fitness under treatment with the antibiotic carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . Purified GlrR can be phosphorylated in vitro by the cognate histidine kinase GlrK as well as by the non-cognate histidine kinases UhpB, RstB, and BaeS . GlrR: "glmY-regulating response regulator"

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFU4|protein.P0AFU4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008400,ECOCYC:EG11285,GeneID:947042`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2687469-2688803:-; feature_type=gene
