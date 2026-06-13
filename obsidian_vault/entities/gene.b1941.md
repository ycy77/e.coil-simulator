---
entity_id: "gene.b1941"
entity_type: "gene"
name: "fliI"
source_database: "NCBI RefSeq"
source_id: "gene-b1941"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1941"
  - "fliI"
---

# fliI

`gene.b1941`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1941`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliI (gene.b1941) is a gene entity. It encodes fliI (protein.P52612). Encoded protein function: FUNCTION: Probable catalytic subunit of a protein translocase for flagellum-specific export, or a proton translocase involved in local circuits at the flagellum. May be involved in a specialized protein export pathway that proceeds without signal peptide cleavage. EcoCyc product frame: G377-MONOMER. EcoCyc synonyms: fla, flaAIII, flaC. Genomic coordinates: 2016554-2017927. EcoCyc protein note: FliI is a cytoplasmic component of the flagellar export apparatus and serves as the ATPase of the apparatus, providing the energy for translocation of export substrates across the cytoplasmic membrane . The structure of FliI missing the N-terminal 18 amino acids was determined by X-ray crystallography to a resolution of 2.4 Å .

## Biological Role

Repressed by pdeL (protein.P21514), csgD (protein.P52106).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52612|protein.P52612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=fliI; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006460,ECOCYC:G377,GeneID:946457`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2016554-2017927:+; feature_type=gene
