---
entity_id: "gene.b1190"
entity_type: "gene"
name: "dadX"
source_database: "NCBI RefSeq"
source_id: "gene-b1190"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1190"
  - "dadX"
---

# dadX

`gene.b1190`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1190`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dadX (gene.b1190) is a gene entity. It encodes dadX (protein.P29012). Encoded protein function: FUNCTION: Isomerizes L-alanine to D-alanine which is then oxidized to pyruvate by DadA. {ECO:0000250}. EcoCyc product frame: ALARACECAT-MONOMER. EcoCyc synonyms: alnA, alnB, dadB. Genomic coordinates: 1238879-1239949.

## Biological Role

Repressed by lrp (protein.P0ACJ0), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29012|protein.P29012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dadX; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=dadX; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=dadX; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=dadX; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0003997,ECOCYC:EG11408,GeneID:945754`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1238879-1239949:+; feature_type=gene
