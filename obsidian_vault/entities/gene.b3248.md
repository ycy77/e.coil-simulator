---
entity_id: "gene.b3248"
entity_type: "gene"
name: "yhdE"
source_database: "NCBI RefSeq"
source_id: "gene-b3248"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3248"
  - "yhdE"
---

# yhdE

`gene.b3248`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3248`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdE (gene.b3248) is a gene entity. It encodes yhdE (protein.P25536). Encoded protein function: FUNCTION: Nucleoside triphosphate pyrophosphatase that hydrolyzes dTTP and UTP (PubMed:24210219, PubMed:25658941, PubMed:28811554). Can also hydrolyze TTP and the modified nucleotides 5-methyl-UTP (m(5)UTP), pseudo-UTP and 5-methyl-CTP (m(5)CTP). Has weak activity with CTP (PubMed:24210219, PubMed:25658941). May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids (PubMed:24210219, PubMed:25658941). Important in maintenance of cell shape (PubMed:25658941). {ECO:0000269|PubMed:24210219, ECO:0000269|PubMed:25658941, ECO:0000269|PubMed:28811554}. EcoCyc product frame: EG11298-MONOMER. Genomic coordinates: 3397785-3398378.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25536|protein.P25536]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010653,ECOCYC:EG11298,GeneID:947753`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3397785-3398378:-; feature_type=gene
