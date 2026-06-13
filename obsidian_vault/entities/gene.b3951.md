---
entity_id: "gene.b3951"
entity_type: "gene"
name: "pflD"
source_database: "NCBI RefSeq"
source_id: "gene-b3951"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3951"
  - "pflD"
---

# pflD

`gene.b3951`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3951`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pflD (gene.b3951) is a gene entity. It encodes pflD (protein.P32674). Encoded protein function: FUNCTION: Probably shows dehydratase activity. {ECO:0000305|PubMed:28183913}. EcoCyc product frame: EG11910-MONOMER. EcoCyc synonyms: yijL. Genomic coordinates: 4143995-4146292. EcoCyc protein note: PflD was identified by sequence similarity as a homolog of pyruvate formate-lyase . Effects of a pflD knockout have been studied; the fermentation pattern under microaerobic conditions is similar to wild type . The expression level of pflD in response to a dissolved oxygen tension gradient has been measured .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32674|protein.P32674]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012934,ECOCYC:EG11910,GeneID:948454`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4143995-4146292:+; feature_type=gene
