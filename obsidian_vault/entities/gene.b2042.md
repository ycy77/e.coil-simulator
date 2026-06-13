---
entity_id: "gene.b2042"
entity_type: "gene"
name: "galF"
source_database: "NCBI RefSeq"
source_id: "gene-b2042"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2042"
  - "galF"
---

# galF

`gene.b2042`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2042`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galF (gene.b2042) is a gene entity. It encodes galF (protein.P0AAB6). Encoded protein function: UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (Alpha-D-glucosyl-1-phosphate uridylyltransferase) (UDP-glucose pyrophosphorylase) (UDPGP) (Uridine diphosphoglucose pyrophosphorylase) EcoCyc product frame: G7093-MONOMER. EcoCyc synonyms: wcaN, yefG. Genomic coordinates: 2113434-2114327. EcoCyc protein note: GalF is a protein with 58% sequence identity to GLUC1PURIDYLTRANS-MONOMER GalU. The potential biochemical activity and in vivo role of GalF has long been unclear. Recent biochemical and mutagenesis data showed that GalF has vestigial UTP:glucose-1-phosphate uridylyltransferase activity, with a specific activity 10000-fold lower than GalU. Mutagenesis of predicted active site residues towards the GalU sequence increases activity, and overexpression of GalF allows delayed growth on galactose as the source of carbon in a galU mutant . GalF was initially suggested to be a subunit of a GalU/GalF protein complex involved in COLANSYN-PWY. In the uropathogenic E. coli strain VW187 (O7:K1), GalF has been shown to interact physically with GalU, as well as enhancing its thermal stability and increasing its enzymatic activity . Based on these results, it was thought to be part of a GalU/GalF complex in that strain, and was predicted to be involved in a similar complex in E...

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAB6|protein.P0AAB6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006771,ECOCYC:G7093,GeneID:946560`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2113434-2114327:-; feature_type=gene
