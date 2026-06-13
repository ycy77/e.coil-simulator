---
entity_id: "gene.b3424"
entity_type: "gene"
name: "glpG"
source_database: "NCBI RefSeq"
source_id: "gene-b3424"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3424"
  - "glpG"
---

# glpG

`gene.b3424`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3424`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpG (gene.b3424) is a gene entity. It encodes glpG (protein.P09391). Encoded protein function: FUNCTION: Rhomboid-type serine protease that catalyzes intramembrane proteolysis. {ECO:0000269|PubMed:16216077, ECO:0000269|PubMed:17099694}. EcoCyc product frame: EG10397-MONOMER. Genomic coordinates: 3560622-3561452. EcoCyc protein note: GlpG is an intramembrane protease of the rhomboid family. Rhomboid proteases were first described in Drosophila and rhomboid-like genes are ubiquitous in prokaryotic genomes; rhomboid proteases are intramembrane, non-classical serine proteases which cleave membrane proteins; GlpG catalysis has been intensively studied and described but its physiological role is not well understood. GlpG cleaves the three Drosophila rhomboid substrates Spitz, Keren and Gurken in a mammalian cell transfection assay . Purified GlpG cleaves the model substrate, Drosophila Gurken-TMD; cleavage does not require ATP . GlpG cleaves an engineered, single spanning membrane protein of type I orientation (Nout-Cin) in vitro and in vivo; substrate features and recognition motifs that facilitate GlpG cleavage have been explored . GlpG cleaves truncated forms of a multispanning membrane protein (MdfA) in vivo and in vitro but intact MdfA is resistant to cleavage...

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09391|protein.P09391]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011179,ECOCYC:EG10397,GeneID:947936`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3560622-3561452:-; feature_type=gene
