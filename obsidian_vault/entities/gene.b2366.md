---
entity_id: "gene.b2366"
entity_type: "gene"
name: "dsdA"
source_database: "NCBI RefSeq"
source_id: "gene-b2366"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2366"
  - "dsdA"
---

# dsdA

`gene.b2366`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2366`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsdA (gene.b2366) is a gene entity. It encodes dsdA (protein.P00926). Encoded protein function: D-serine dehydratase (EC 4.3.1.18) (D-serine deaminase) (DSD) EcoCyc product frame: DSERDEAM-MONOMER. Genomic coordinates: 2479202-2480530. EcoCyc protein note: It was established long ago that E. coli is able to deaminate serine and that the activity is inducible by D-serine . D-serine ammonia-lyase (DsdA) catalyzes the deamination of D-serine to form pyruvate and ammonia. D-serine has a bacteriostatic effect on E. coli; thus, when D-serine is present, detoxification is necessary for cell growth . Once the cell expresses DsdA, D-serine can be utilized as the sole source of carbon and nitrogen . Toxicity of D-serine in minimal medium appears to be due to an effect on biosynthesis of L-serine and pantothenate . The cofactor requirements and reaction mechanism of the enzyme have been investigated. Binding of the pyridoxal phosphate (PLP) cofactor has been studied in detail . The reaction involves a transient Schiff base intermediate of α-aminoacrylate and PLP . The G279D and G281D mutations eliminate enzyme activity due to altered interactions with PLP . More conservative substitutions at G278, G279, and G281 result in reduced or altered enzymatic activity...

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00926|protein.P00926]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007804,ECOCYC:EG10249,GeneID:946837`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2479202-2480530:+; feature_type=gene
