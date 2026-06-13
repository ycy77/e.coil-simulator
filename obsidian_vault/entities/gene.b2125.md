---
entity_id: "gene.b2125"
entity_type: "gene"
name: "btsR"
source_database: "NCBI RefSeq"
source_id: "gene-b2125"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2125"
  - "btsR"
---

# btsR

`gene.b2125`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2125`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btsR (gene.b2125) is a gene entity. It encodes btsR (protein.P0AFT5). Encoded protein function: FUNCTION: Member of the two-component regulatory system BtsS/BtsR, which is part of a nutrient-sensing regulatory network composed of BtsS/BtsR, the low-affinity pyruvate signaling system YpdA/YpdB and their respective target proteins, BtsT and YhjX. Responds to depletion of nutrients, specifically serine, and the concomitant presence of extracellular pyruvate. BtsR regulates expression of btsT by binding to its promoter region. Activation of the BtsS/BtsR signaling cascade also suppresses YpdA/YpdB-mediated yhjX induction. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:28469239}. EcoCyc product frame: MONOMER0-4276. EcoCyc synonyms: yehT. Genomic coordinates: 2212243-2212962. EcoCyc protein note: BtsR, formerly YehT, belongs to the LytTR response regulator (RR) of the two-component system that is involved in the stationary-phase control network . An exhaustive search of the Escherichia coli genome found a single motif for the BtsR transcriptional regulator, located upstream of the G7942 gene; therefore, it seems to be the only target regulated by the EG12007/EG12006 system...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFT5|protein.P0AFT5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007023,ECOCYC:EG12006,GeneID:949024`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2212243-2212962:-; feature_type=gene
