---
entity_id: "gene.b0674"
entity_type: "gene"
name: "asnB"
source_database: "NCBI RefSeq"
source_id: "gene-b0674"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0674"
  - "asnB"
---

# asnB

`gene.b0674`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0674`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asnB (gene.b0674) is a gene entity. It encodes asnB (protein.P22106). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent conversion of aspartate into asparagine, using glutamine as a source of nitrogen. Can also use ammonia as the nitrogen source in vitro, albeit with lower efficiency. As nucleotide substrates, ATP and dATP are utilized at a similar rate in both the glutamine- and ammonia-dependent reactions, whereas GTP utilization is only 15% that of ATP, and CTP, UTP, ITP and XTP are very poor or not substrates. Also exhibits glutaminase activity. {ECO:0000269|PubMed:20853825, ECO:0000269|PubMed:6102982, ECO:0000269|PubMed:7907328}. EcoCyc product frame: ASNSYNB-MONOMER. Genomic coordinates: 697513-699177.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22106|protein.P22106]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002292,ECOCYC:EG10092,GeneID:945281`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:697513-699177:-; feature_type=gene
