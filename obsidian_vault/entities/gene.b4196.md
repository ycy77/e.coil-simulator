---
entity_id: "gene.b4196"
entity_type: "gene"
name: "ulaD"
source_database: "NCBI RefSeq"
source_id: "gene-b4196"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4196"
  - "ulaD"
---

# ulaD

`gene.b4196`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4196`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaD (gene.b4196) is a gene entity. It encodes ulaD (protein.P39304). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of 3-keto-L-gulonate-6-P into L-xylulose-5-P. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000269|PubMed:11741871}. EcoCyc product frame: G7858-MONOMER. EcoCyc synonyms: yjfV, sgaH. Genomic coordinates: 4422186-4422836.

## Biological Role

Repressed by ulaR (protein.P0A9W0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39304|protein.P39304]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ulaD; function=+
- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `S` - regulator=UlaR; target=ulaD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013729,ECOCYC:G7858,GeneID:948714`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4422186-4422836:+; feature_type=gene
