---
entity_id: "gene.b3788"
entity_type: "gene"
name: "rffG"
source_database: "NCBI RefSeq"
source_id: "gene-b3788"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3788"
  - "rffG"
---

# rffG

`gene.b3788`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3788`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rffG (gene.b3788) is a gene entity. It encodes rffG (protein.P27830). Encoded protein function: FUNCTION: Catalyzes the dehydration of dTDP-D-glucose to form dTDP-6-deoxy-D-xylo-4-hexulose via a three-step process involving oxidation, dehydration and reduction. {ECO:0000269|PubMed:11380254, ECO:0000269|PubMed:11601973, ECO:0000269|PubMed:7559340}. EcoCyc product frame: DTDPGLUCDEHYDRAT2-MONOMER. EcoCyc synonyms: rff. Genomic coordinates: 3972522-3973589. EcoCyc protein note: dTDP-glucose 4,6-dehydratase 2 (RffG) is involved in the biosynthesis of enterobacterial common antigen (ECA). This enzyme catalyzes the conversion of dTDP-α-D-glucose into dTDP-4-keto-6-deoxyglucose. This reaction occurs in three steps: dehydrogenation, dehydration, and rereduction. The coenzyme NAD+ mediates the dehydrogenation and rereduction steps of the reaction. . dTDP-glucose 4,6-dehydratase is encoded by the rffG gene which is paralogous to rfbB. The product of rfbB is another dTDP-glucose 4,6-dehydratase which catalyzes the same reaction as RffG, but functions in the rhamnose biosynthesis pathway . A model of the active site has been generated and site directed mutagenesis studies have identified several residues which are essential for catalysis . Specific residues which are the acid and base catalysts for the dehydration step have been determined .

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27830|protein.P27830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012376,ECOCYC:EG11453,GeneID:948300`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3972522-3973589:+; feature_type=gene
