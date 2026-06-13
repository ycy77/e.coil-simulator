---
entity_id: "gene.b2183"
entity_type: "gene"
name: "rsuA"
source_database: "NCBI RefSeq"
source_id: "gene-b2183"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2183"
  - "rsuA"
---

# rsuA

`gene.b2183`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2183`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsuA (gene.b2183) is a gene entity. It encodes rsuA (protein.P0AA43). Encoded protein function: FUNCTION: Responsible for synthesis of pseudouridine from uracil-516 in 16S ribosomal RNA. {ECO:0000269|PubMed:10376875, ECO:0000269|PubMed:7612632}. EcoCyc product frame: EG12044-MONOMER. EcoCyc synonyms: yejD. Genomic coordinates: 2279788-2280483. EcoCyc protein note: RsuA is the pseudouridine synthase that is responsible for pseudouridylation of 16S rRNA at position 516 . In vitro, the enzyme does not modify free 16S rRNA. The preferred substrate is a 5'-terminal fragment of 16S rRNA complexed with 30S ribosomal proteins, suggesting that pseudouridylation occurs at an intermediate stage of 30S assembly in vivo . RsuA has the highest affinity to the 5'-terminal 16S fragment complexed with ribosomal protein S17 alone . Crystal structures of RsuA in complex with uracil or UMP have been solved. RsuA consists of an N-terminal domain with structural similarity to ribosomal protein S4, an extended linker region, and a C-terminal catalytic domain. Despite limited sequence similarity, the structure of RsuA is similar to that of TruA, a tRNA pseudouridine synthase . The N-terminal S4-like domain may be important for substrate recognition...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA43|protein.P0AA43]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007223,ECOCYC:EG12044,GeneID:945378`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2279788-2280483:-; feature_type=gene
