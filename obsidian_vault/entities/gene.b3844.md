---
entity_id: "gene.b3844"
entity_type: "gene"
name: "fre"
source_database: "NCBI RefSeq"
source_id: "gene-b3844"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3844"
  - "fre"
---

# fre

`gene.b3844`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3844`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fre (gene.b3844) is a gene entity. It encodes fre (protein.P0AEN1). Encoded protein function: FUNCTION: Catalyzes the reduction of soluble flavins by reduced pyridine nucleotides. {ECO:0000250|UniProtKB:Q9L6L9}. EcoCyc product frame: FMNREDUCT-MONOMER. EcoCyc synonyms: fadI, flrD, fsrC. Genomic coordinates: 4026527-4027228. EcoCyc protein note: Flavin reductase (Fre) catalyzes the reduction of free flavins (riboflavin, FMN, or FAD) by NADPH or NADH . The enzyme appears to be an important physiological source of superoxide radicals . The enzyme follows a sequential ordered reaction mechanism, with binding of NADPH followed by flavin binding . After both NADPH and riboflavin are bound, a charge-transfer complex of NADPH and riboflavin is formed as the first intermediate, followed by a second charge-transfer intermediate of enzyme-bound NADP+ and reduced riboflavin . The enzyme is A-side-specific, selectively transfering the pro-R hydrogen from the C-4 position of the nicotinamide group . Flavin reductase utilizes flavins only as substrates, not as cofactors. The interaction of the enzyme with its flavin substrates has been studied . FAD appears to interact with Fre at a site overlapping with the NAD(P)H-binding site, binding more tightly than either FMN or riboflavin...

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEN1|protein.P0AEN1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012559,ECOCYC:EG10334,GeneID:948325`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4026527-4027228:+; feature_type=gene
