---
entity_id: "gene.b2148"
entity_type: "gene"
name: "mglC"
source_database: "NCBI RefSeq"
source_id: "gene-b2148"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2148"
  - "mglC"
---

# mglC

`gene.b2148`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2148`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mglC (gene.b2148) is a gene entity. It encodes mglC (protein.P23200). Encoded protein function: FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:6807987}. EcoCyc product frame: MGLC-MONOMER. EcoCyc synonyms: mglP. Genomic coordinates: 2236743-2237753. EcoCyc protein note: MglC is the predicted integral membrane component of a D-galactose / D-galactoside ABC transporter. mglC mutants are unable to accumulate labeled methyl-β-D-galactopyranoside .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23200|protein.P23200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=mglC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007101,ECOCYC:EG10594,GeneID:949039`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2236743-2237753:-; feature_type=gene
