---
entity_id: "gene.b1298"
entity_type: "gene"
name: "puuD"
source_database: "NCBI RefSeq"
source_id: "gene-b1298"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1298"
  - "puuD"
---

# puuD

`gene.b1298`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1298`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuD (gene.b1298) is a gene entity. It encodes puuD (protein.P76038). Encoded protein function: FUNCTION: Involved in the breakdown of putrescine via hydrolysis of the gamma-glutamyl linkage of gamma-glutamyl-gamma-aminobutyrate. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:16499623}. EcoCyc product frame: G6645-MONOMER. EcoCyc synonyms: ycjL. Genomic coordinates: 1361120-1361884. EcoCyc protein note: PuuD was identified as the γ-glutamyl-γ-aminobutyrate hydrolase in a putrescine utilization pathway. The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . PuuD is highly expressed in early stationary phase; expression of puuD is induced by growth on putrescine as the sole source of nitrogen and during the transition of anaerobic to aerobic cultures . Addition of succinate or NH4Cl to the medium reduces PuuD expression . A strain carrying a mutation in puuD can not grow on putrescine as the sole source of nitrogen and accumulates γ-glutamyl-γ-aminobutyrate . PuuD: "putrescine utilization pathway" Review:

## Biological Role

Repressed by arcA (protein.P0A9Q1), puuR (protein.P0A9U6). Activated by fimZ (protein.P0AEL8).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76038|protein.P76038]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AEL8|protein.P0AEL8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=puuD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `C` - regulator=PuuR; target=puuD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004369,ECOCYC:G6645,GeneID:945882`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1361120-1361884:+; feature_type=gene
