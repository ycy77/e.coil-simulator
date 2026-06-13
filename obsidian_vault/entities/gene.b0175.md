---
entity_id: "gene.b0175"
entity_type: "gene"
name: "cdsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0175"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0175"
  - "cdsA"
---

# cdsA

`gene.b0175`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0175`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cdsA (gene.b0175) is a gene entity. It encodes cdsA (protein.P0ABG1). Encoded protein function: FUNCTION: Transferase that catalyzes the synthesis of a CDP-diacylglycerol (CDP-DAG), the activated form of a phosphatidate (PubMed:2995359, PubMed:30936205). It is essential for phospholipid biosynthesis (PubMed:2995359). It is also involved in the biosynthesis of MPIase, a glycolipid essential for membrane protein integration and cell growth (PubMed:30718729, PubMed:30739787). It displays a preference for phosphatidic acids bearing at least one double bond in their fatty acyl moieties (PubMed:2995359). It can use CTP and dCTP, but not ATP, UTP, dATP, dTTP and dGTP (PubMed:2995359). The reaction is reversible in vitro (PubMed:2995359). {ECO:0000269|PubMed:2995359, ECO:0000269|PubMed:30718729, ECO:0000269|PubMed:30739787, ECO:0000269|PubMed:30936205}. EcoCyc product frame: CDPDIGLYSYN-MONOMER. EcoCyc synonyms: cds. Genomic coordinates: 195677-196534. EcoCyc protein note: CDP-diglyceride synthetase catalyzes the synthesis of CDPDIACYLGLYCEROL, the activated form of L-PHOSPHATIDATE (phosphatidic acid). CDPDIACYLGLYCEROL "CDP-diacylglycerol" is positioned at a branchpoint in the lipid biosynthetic pathway where it reacts with GLYCEROL-3P to form L-1-PHOSPHATIDYL-GLYCEROL-P, or with SER to form L-1-PHOSPHATIDYL-SERINE...

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABG1|protein.P0ABG1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000600,ECOCYC:EG10139,GeneID:944876`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:195677-196534:+; feature_type=gene
