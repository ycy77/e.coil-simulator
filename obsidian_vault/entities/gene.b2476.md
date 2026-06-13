---
entity_id: "gene.b2476"
entity_type: "gene"
name: "purC"
source_database: "NCBI RefSeq"
source_id: "gene-b2476"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2476"
  - "purC"
---

# purC

`gene.b2476`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2476`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purC (gene.b2476) is a gene entity. It encodes purC (protein.P0A7D7). Encoded protein function: FUNCTION: Converts 4-carboxy-5-aminoimidazole ribonucleotide (CAIR) to 4-(N-succinylcarboxamide)-5-aminoimidazole ribonucleotide (SAICAR). {ECO:0000269|PubMed:1534690}. EcoCyc product frame: SAICARSYN-MONOMER. EcoCyc synonyms: ade(g), ade. Genomic coordinates: 2596905-2597618.

## Biological Role

Repressed by purR (protein.P0ACP7).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7D7|protein.P0A7D7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008156,ECOCYC:EG10791,GeneID:946957`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2596905-2597618:-; feature_type=gene
