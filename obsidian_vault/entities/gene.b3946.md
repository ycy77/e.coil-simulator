---
entity_id: "gene.b3946"
entity_type: "gene"
name: "fsaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3946"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3946"
  - "fsaB"
---

# fsaB

`gene.b3946`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3946`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fsaB (gene.b3946) is a gene entity. It encodes fsaB (protein.P32669). Encoded protein function: FUNCTION: Catalyzes the reversible formation of fructose 6-phosphate from dihydroxyacetone and D-glyceraldehyde 3-phosphate via an aldolization reaction. Can utilize hydroxyacetone as an alternative donor substrate. Is also able to catalyze the direct self-aldol addition of glycolaldehyde. Is less catalytically efficient than the isozyme FsaA. Does not display transaldolase activity. {ECO:0000269|PubMed:11120740, ECO:0000269|Ref.6}. EcoCyc product frame: EG11905-MONOMER. EcoCyc synonyms: yijG, talC. Genomic coordinates: 4139046-4139708.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32669|protein.P32669]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012915,ECOCYC:EG11905,GeneID:948439`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4139046-4139708:-; feature_type=gene
