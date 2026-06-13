---
entity_id: "gene.b1638"
entity_type: "gene"
name: "pdxH"
source_database: "NCBI RefSeq"
source_id: "gene-b1638"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1638"
  - "pdxH"
---

# pdxH

`gene.b1638`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1638`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxH (gene.b1638) is a gene entity. It encodes pdxH (protein.P0AFI7). Encoded protein function: FUNCTION: Catalyzes the oxidation of either pyridoxine 5'-phosphate (PNP) or pyridoxamine 5'-phosphate (PMP) into pyridoxal 5'-phosphate (PLP). {ECO:0000269|PubMed:11786019, ECO:0000269|PubMed:7860596, ECO:0000269|PubMed:9693059}. EcoCyc product frame: PDXH-MONOMER. Genomic coordinates: 1717351-1718007.

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFI7|protein.P0AFI7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005482,ECOCYC:EG11487,GeneID:946806`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1717351-1718007:-; feature_type=gene
