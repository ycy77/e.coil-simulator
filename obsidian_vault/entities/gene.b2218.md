---
entity_id: "gene.b2218"
entity_type: "gene"
name: "rcsC"
source_database: "NCBI RefSeq"
source_id: "gene-b2218"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2218"
  - "rcsC"
---

# rcsC

`gene.b2218`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2218`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcsC (gene.b2218) is a gene entity. It encodes rcsC (protein.P0DMC5). Encoded protein function: FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsC functions as a membrane-associated protein kinase that phosphorylates RcsD in response to environmental signals. The phosphoryl group is then transferred to the response regulator RcsB. RcsC also has phosphatase activity. The system controls expression of genes involved in colanic acid capsule synthesis, biofilm formation and cell division. {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:10564486, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11758943, ECO:0000269|PubMed:11807084, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:14651646}. EcoCyc product frame: MONOMER0-4194. Genomic coordinates: 2317027-2319876. EcoCyc protein note: Represents the His-479 phosphorylated form of RCSC-MONOMER RcsC - the histidine kinase of the Rcs signal transduction system...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DMC5|protein.P0DMC5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007336,ECOCYC:EG10822,GeneID:948993`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2317027-2319876:-; feature_type=gene
