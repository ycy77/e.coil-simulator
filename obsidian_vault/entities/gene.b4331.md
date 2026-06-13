---
entity_id: "gene.b4331"
entity_type: "gene"
name: "kptA"
source_database: "NCBI RefSeq"
source_id: "gene-b4331"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4331"
  - "kptA"
---

# kptA

`gene.b4331`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4331`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kptA (gene.b4331) is a gene entity. It encodes kptA (protein.P39380). Encoded protein function: FUNCTION: Removes the 2'-phosphate from RNA via an intermediate in which the phosphate is ADP-ribosylated by NAD followed by a presumed transesterification to release the RNA and generate ADP-ribose 1''-2''-cyclic phosphate (APPR>P). May function as an ADP-ribosylase. {ECO:0000269|PubMed:9915792}. EcoCyc product frame: G7928-MONOMER. EcoCyc synonyms: yjiI. Genomic coordinates: 4560930-4561484. EcoCyc protein note: KptA exhibits tRNA 2'-phosphotransferase activity. However, 2' phopsphorylated RNA is a splicing intermediate; thus, this substrate is not likely to have physiological relevance in E. coli . KptA has similarity to Saccharomyces cerevisiae Tpt1, a tRNA splicing enzyme. Unlike Tpt1, KptA accumulates the ADP-ribosylated RNA reaction intermediate . Comparative genomics suggests that KptA may play a role in NAD metabolism .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39380|protein.P39380]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014204,ECOCYC:G7928,GeneID:948858`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4560930-4561484:+; feature_type=gene
