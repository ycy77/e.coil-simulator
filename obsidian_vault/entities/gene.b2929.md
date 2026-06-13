---
entity_id: "gene.b2929"
entity_type: "gene"
name: "fumE"
source_database: "NCBI RefSeq"
source_id: "gene-b2929"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2929"
  - "fumE"
---

# fumE

`gene.b2929`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2929`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fumE (gene.b2929) is a gene entity. It encodes fumE (protein.P11663). Encoded protein function: FUNCTION: In vitro catalyzes the addition of water to fumarate, forming malate. Cannot catalyze the reverse reaction. Cannot use the cis-isomer maleate as substrate. {ECO:0000269|PubMed:27941785}. EcoCyc product frame: EG11162-MONOMER. EcoCyc synonyms: yggD. Genomic coordinates: 3074686-3075195. EcoCyc protein note: The fumarase activity of FumE was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . FumE: "fumarase E"

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11663|protein.P11663]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009612,ECOCYC:EG11162,GeneID:946861`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3074686-3075195:-; feature_type=gene
