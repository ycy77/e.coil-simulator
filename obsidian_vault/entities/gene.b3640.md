---
entity_id: "gene.b3640"
entity_type: "gene"
name: "dut"
source_database: "NCBI RefSeq"
source_id: "gene-b3640"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3640"
  - "dut"
---

# dut

`gene.b3640`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3640`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dut (gene.b3640) is a gene entity. It encodes dut (protein.P06968). Encoded protein function: FUNCTION: This enzyme is involved in nucleotide metabolism: it produces dUMP, the immediate precursor of thymidine nucleotides and it decreases the intracellular concentration of dUTP so that uracil cannot be incorporated into DNA. {ECO:0000269|PubMed:9261872}. EcoCyc product frame: DUTP-PYROP-MONOMER. EcoCyc synonyms: dnaS, sof. Genomic coordinates: 3813929-3814387.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06968|protein.P06968]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011899,ECOCYC:EG10251,GeneID:948607`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3813929-3814387:+; feature_type=gene
