---
entity_id: "gene.b0767"
entity_type: "gene"
name: "pgl"
source_database: "NCBI RefSeq"
source_id: "gene-b0767"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0767"
  - "pgl"
---

# pgl

`gene.b0767`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0767`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgl (gene.b0767) is a gene entity. It encodes pgl (protein.P52697). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 6-phosphogluconolactone to 6-phosphogluconate. {ECO:0000269|PubMed:15576773}. EcoCyc product frame: 6PGLUCONOLACT-MONOMER. EcoCyc synonyms: ybhE. Genomic coordinates: 798586-799581. EcoCyc protein note: 6-phosphogluconolactonase is an enzyme of the oxidative pentose phosphate pathway. A pgl mutant strain grows only slightly slower than wild type on glucose as the sole source of carbon . Growth on glucose may be due to non-enzymatic hydrolysis of D-6-P-GLUCONO-DELTA-LACTONE or a bypass pathway that involves dephosphorylation and export of gluconolactone, hydrolysis to gluconate, followed by gluconate re-import and phosphorylation . When grown on maltose medium, strains lacking Pgl activity turn blue after iodine treatment . The phenotype of a pgl deletion strain can be complemented by expression of the pgl gene from Pseudomonas putida, although there is no detectable similarity between the two genes . A metabolic flux balance experiment revealed that the inefficient growth when pgl is deleted results solely from the extracellular bypass mechanism . Unlike some other enzymes that participate in the pentose phosphate pathway, Pgl is robust towards oxidative inactivation by peroxyl radicals...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52697|protein.P52697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002611,ECOCYC:G6397,GeneID:946398`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:798586-799581:+; feature_type=gene
