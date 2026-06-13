---
entity_id: "gene.b3803"
entity_type: "gene"
name: "hemX"
source_database: "NCBI RefSeq"
source_id: "gene-b3803"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3803"
  - "hemX"
---

# hemX

`gene.b3803`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3803`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemX (gene.b3803) is a gene entity. It encodes hemX (protein.P09127). Encoded protein function: Protein HemX (ORF X) EcoCyc product frame: HEMX-MONOMER. Genomic coordinates: 3987885-3989066. EcoCyc protein note: The HemX protein was suggested to be a uroporphyrinogen III methylase . However, the function of the protein has not been experimentally determined. HemX exists as a homooligomer in the inner membrane . HemX is predicted to be a bitopic inner membrane protein .

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09127|protein.P09127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012419,ECOCYC:EG10433,GeneID:948446`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3987885-3989066:-; feature_type=gene
