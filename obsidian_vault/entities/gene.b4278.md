---
entity_id: "gene.b4278"
entity_type: "gene"
name: "insG"
source_database: "NCBI RefSeq"
source_id: "gene-b4278"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4278"
  - "insG"
---

# insG

`gene.b4278`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4278`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insG (gene.b4278) is a gene entity. It encodes insG (protein.P03835). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS4. EcoCyc product frame: G7900-MONOMER. EcoCyc synonyms: yi41. Genomic coordinates: 4502103-4503431. EcoCyc protein note: InsG is encoded by the IS4 transposable element. The phylogenetic distribution and properties of the IS4 family of transposases have been investigated . In an experiment set up to determine the transposition and excision rate of insertion elements in E. coli K-12, no transposition or excision events were detected for IS4 over the duration of the experiment (80,500 generations) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03835|protein.P03835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014021,ECOCYC:G7900,GeneID:948805`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4502103-4503431:-; feature_type=gene
