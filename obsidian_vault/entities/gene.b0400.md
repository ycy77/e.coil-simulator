---
entity_id: "gene.b0400"
entity_type: "gene"
name: "phoR"
source_database: "NCBI RefSeq"
source_id: "gene-b0400"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0400"
  - "phoR"
---

# phoR

`gene.b0400`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0400`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoR (gene.b0400) is a gene entity. It encodes phoR (protein.P08400). Encoded protein function: FUNCTION: Member of the two-component regulatory system PhoR/PhoB involved in the phosphate regulon genes expression. PhoR may function as a membrane-associated protein kinase that phosphorylates PhoB in response to environmental signals. EcoCyc product frame: PHOR-MONOMER. EcoCyc synonyms: R1pho, phoR1, nmpB. Genomic coordinates: 417889-419184.

## Biological Role

Activated by phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08400|protein.P08400]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=phoR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001391,ECOCYC:EG10733,GeneID:945044`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:417889-419184:+; feature_type=gene
