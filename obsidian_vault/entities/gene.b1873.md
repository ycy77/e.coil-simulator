---
entity_id: "gene.b1873"
entity_type: "gene"
name: "torY"
source_database: "NCBI RefSeq"
source_id: "gene-b1873"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1873"
  - "torY"
---

# torY

`gene.b1873`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1873`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torY (gene.b1873) is a gene entity. It encodes torY (protein.P52005). Encoded protein function: FUNCTION: Part of the anaerobic respiratory chain of trimethylamine-N-oxide reductase TorZ. Required for electron transfer to the TorZ terminal enzyme. EcoCyc product frame: G7023-MONOMER. EcoCyc synonyms: yecK. Genomic coordinates: 1957032-1958132. EcoCyc protein note: The periplasmic oxidoreductase G7022-MONOMER "TorZ" and membrane anchored pentaheme c-type cytochrome TorY constitute an anaerobic respiratory system that can use several N and S-oxides, including TMAO and biotin sulfoxide as terminal electron acceptors . TorY is a c-type cytochrome that is anchored to the inner membrane; 5 predicted heme binding sites (CXXCH) have been identified. TorY has 36% identity with EG11815-MONOMER . torYZ expression is very low and is not induced by TMAO or DMSO .

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52005|protein.P52005]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006246,ECOCYC:G7023,GeneID:946490`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1957032-1958132:-; feature_type=gene
