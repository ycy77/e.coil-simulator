---
entity_id: "gene.b3018"
entity_type: "gene"
name: "plsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3018"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3018"
  - "plsC"
---

# plsC

`gene.b3018`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3018`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

plsC (gene.b3018) is a gene entity. It encodes plsC (protein.P26647). Encoded protein function: FUNCTION: Converts lysophosphatidic acid (LPA) into phosphatidic acid by incorporating an acyl moiety at the 2 position. This enzyme can utilize either acyl-CoA or acyl-ACP as the fatty acyl donor. {ECO:0000269|PubMed:2211622}. EcoCyc product frame: 1-ACYLGLYCEROL-3-P-ACYLTRANSFER-MONOMER. EcoCyc synonyms: parF. Genomic coordinates: 3162744-3163481. EcoCyc protein note: Membrane-bound 1-acylglycerol-3-phosphate O-acyltransferase (PlsC) catalyzes the second step in phospholipid biosynthesis and is thought to function in close proximity to the preceding enzyme, GLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsB) . PlsC is specific for acylation at the sn-2 position of ACYL-SN-GLYCEROL-3P and can utilize either acyl-acyl carrier protein (acyl-ACP) or acyl-coenzyme A (acyl-CoA) as the fatty acyl donor to form L-PHOSPHATIDATE (a phosphatidate, a phosphatidic acid) . PlsB and PlsC activity has been reconstituted in a cell-free liposome system . Fatty acids that are endogenously synthesized are attached to ACP, and exogenously added fatty acids are attached to CoA . In E. coli phospholipids, the sn-1 position is occupied mainly by either palmitate or cis-vaccenate, whereas the sn-2 position is predominantly palmitoleate or cis-vaccenate...

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26647|protein.P26647]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009910,ECOCYC:EG11377,GeneID:947496`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3162744-3163481:-; feature_type=gene
