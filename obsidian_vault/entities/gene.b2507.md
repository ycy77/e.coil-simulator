---
entity_id: "gene.b2507"
entity_type: "gene"
name: "guaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2507"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2507"
  - "guaA"
---

# guaA

`gene.b2507`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2507`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

guaA (gene.b2507) is a gene entity. It encodes guaA (protein.P04079). Encoded protein function: FUNCTION: Catalyzes the synthesis of GMP from XMP. EcoCyc product frame: GMP-SYN-MONOMER. Genomic coordinates: 2630958-2632535.

## Biological Role

Repressed by dnaA (protein.P03004), fis (protein.P0A6R3), purR (protein.P0ACP7). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04079|protein.P04079]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=guaA; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=guaA; function=-
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=guaA; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=guaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008254,ECOCYC:EG10420,GeneID:947334`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2630958-2632535:-; feature_type=gene
