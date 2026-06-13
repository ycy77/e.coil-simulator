---
entity_id: "gene.b1963"
entity_type: "gene"
name: "drpB"
source_database: "NCBI RefSeq"
source_id: "gene-b1963"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1963"
  - "drpB"
---

# drpB

`gene.b1963`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1963`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

drpB (gene.b1963) is a gene entity. It encodes drpB (protein.P76334). Encoded protein function: FUNCTION: A non-essential division protein that localizes to the septal ring in low ionic strength medium. {ECO:0000255|HAMAP-Rule:MF_00857}.; FUNCTION: Localizes to the septal ring in about 30% of observed cells before cell constriction occurs; localization occurs in low ionic strength medium (0 NaCl) and requires FtsZ but not FtsEX. Overexpression partially restores correct FtsI localization to the division septum in an ftsEX deletion. Isolated as a multicopy suppressor of an ftsEX deletion mutant; it does not suppress other cell division defects (e.g. ftsA, ftsI, ftsQ or ftsZ). {ECO:0000269|PubMed:32900831}. EcoCyc product frame: G7051-MONOMER. EcoCyc synonyms: yedR. Genomic coordinates: 2033119-2033421. EcoCyc protein note: DrpB is a non-essential protein involved in cell division that localizes to the septal ring. Localization requires FtsZ, but not FtsEX, and is dependent on growth in a medium with low osmotic strength . Proteins interacting with DrpB were identified by BACTH assays and include DamX, FtsI, FtsN, FtsQ, YmgF, DedD, FtsA, as well as MalF, MalG and PBP2; however, the likelihood of false positives in this assay is high . DrpB is predicted to contain two transmembrane helices, with both the N- and C-terminus of the protein located in the cytoplasm...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76334|protein.P76334]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006514,ECOCYC:G7051,GeneID:946477`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2033119-2033421:-; feature_type=gene
