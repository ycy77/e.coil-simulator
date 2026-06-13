---
entity_id: "gene.b0772"
entity_type: "gene"
name: "ybhC"
source_database: "NCBI RefSeq"
source_id: "gene-b0772"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0772"
  - "ybhC"
---

# ybhC

`gene.b0772`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0772`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhC (gene.b0772) is a gene entity. It encodes ybhC (protein.P46130). Encoded protein function: FUNCTION: Putative thioesterase. Does not bind pectin, and has no pectinesterase activity. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:19452549}. EcoCyc product frame: EG12875-MONOMER. Genomic coordinates: 805998-807281. EcoCyc protein note: YbhC is an outer membrane lipoprotein . Sequence similarity suggests that it is a member of the Outer Membrane Porin (OPR) Family . Phylogenetic analysis places YbhC into a distinct subclade of the carbohydrate esterase 8 (CE8) family . Esterase/thioesterase activity of YbhC was discovered in a high-throughput screen of purified proteins . This activity could not be reproduced by . YbhC is enriched in the membrane fraction of minicells (versus rod cells) purifed from an E. coli minicell mutant and is a polar protein candidate . A crystal structure of a truncated form of YbhC lacking the membrane anchor has been solved at 1.7 Å resolution . Overexpression of yhbC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide .

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46130|protein.P46130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002629,ECOCYC:EG12875,GeneID:945381`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:805998-807281:-; feature_type=gene
