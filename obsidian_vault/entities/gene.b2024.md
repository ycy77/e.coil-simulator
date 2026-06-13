---
entity_id: "gene.b2024"
entity_type: "gene"
name: "hisA"
source_database: "NCBI RefSeq"
source_id: "gene-b2024"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2024"
  - "hisA"
---

# hisA

`gene.b2024`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2024`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisA (gene.b2024) is a gene entity. It encodes hisA (protein.P10371). Encoded protein function: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase) EcoCyc product frame: PRIBFAICARPISOM-MONOMER. Genomic coordinates: 2095125-2095862. EcoCyc protein note: N-(5'-phospho-L-ribosyl-formimino)-5-amino-1-(5'-phosphoribosyl)-4-imidazolecarboxamide isomerase (HisA) carries out the fourth step in histidine biosynthesis. HisA catalyzes an internal redox reaction known as an Amadori rearrangement . Spontaneous hisA mutants were investigated .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10371|protein.P10371]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hisA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006725,ECOCYC:EG10444,GeneID:946521`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2095125-2095862:+; feature_type=gene
