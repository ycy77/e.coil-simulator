---
entity_id: "gene.b0242"
entity_type: "gene"
name: "proB"
source_database: "NCBI RefSeq"
source_id: "gene-b0242"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0242"
  - "proB"
---

# proB

`gene.b0242`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0242`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proB (gene.b0242) is a gene entity. It encodes proB (protein.P0A7B5). Encoded protein function: FUNCTION: Catalyzes the transfer of a phosphate group to glutamate to form L-glutamate 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_00456, ECO:0000269|PubMed:6319365}. EcoCyc product frame: GLUTKIN-MONOMER. EcoCyc synonyms: pro(2), pro2. Genomic coordinates: 260388-261491.

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7B5|protein.P0A7B5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000830,ECOCYC:EG10768,GeneID:946425`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:260388-261491:+; feature_type=gene
