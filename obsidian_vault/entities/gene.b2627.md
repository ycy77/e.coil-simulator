---
entity_id: "gene.b2627"
entity_type: "gene"
name: "abpB"
source_database: "NCBI RefSeq"
source_id: "gene-b2627"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2627"
  - "abpB"
---

# abpB

`gene.b2627`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2627`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abpB (gene.b2627) is a gene entity. It encodes abpB (protein.P52126). Encoded protein function: FUNCTION: Part of an antiviral system composed of AbpA and AbpB; when both are expressed from a plasmid they confer resistance to phages T2, T4, T7 and lambda but not RB32 or RB69. Resistance is temperature dependent, it can be seen at 30 degrees Celsius but not at 37 or 42 degrees Celsius. The system impairs phage but not bacterial DNA synthesis (shown for T4, T7 and lambda). Partially suppressed by mutations in T4 gene 41, a replicative helicase. {ECO:0000269|PubMed:25224971}.; FUNCTION: Deletion or mutations in this gene were selected in directed evolution experiments for resistance to intense ionizing radiation (3000 Gy). {ECO:0000269|PubMed:24596148}. EcoCyc product frame: G7362-MONOMER. EcoCyc synonyms: yfjK. Genomic coordinates: 2761351-2763540. EcoCyc protein note: AbpB together with G7363-MONOMER operate together as a bacteriophage defense system against several types of bacteriophage. AbpAB defense system is activated by phage single-stranded binding (SSB) protein bound to E. coli ssDNA; it is also activated in the absence of phage infections by chemically interrupting E. coli's DNA replication or by deleting DNA repair factors RecB and RecC...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52126|protein.P52126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008648,ECOCYC:G7362,GeneID:947111`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2761351-2763540:-; feature_type=gene
