---
entity_id: "gene.b3801"
entity_type: "gene"
name: "aslA"
source_database: "NCBI RefSeq"
source_id: "gene-b3801"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3801"
  - "aslA"
---

# aslA

`gene.b3801`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3801`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aslA (gene.b3801) is a gene entity. It encodes aslA (protein.P25549). Encoded protein function: FUNCTION: No E.coli strains have been observed to have an arylsulfatase activity. A 'latent' activity has been observed by heterologous expression of a genomic region linked to tynA, but it does not map near aslA. {ECO:0000269|PubMed:361719}. EcoCyc product frame: ARYLSULFAT-MONOMER. EcoCyc synonyms: gppB, atsA. Genomic coordinates: 3984352-3986007. EcoCyc protein note: AslA is a putative Ser-type sulfatase . Although no tested E. coli strain contained measurable arylsulfatase activity, a "latent" arylsulfatase activity was discovered by heterologous expression of a genomic region linked to tynA , which does not map near aslA. Review:

## Enriched Pathways

- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25549|protein.P25549]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012411,ECOCYC:EG10089,GeneID:949015`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3984352-3986007:-; feature_type=gene
