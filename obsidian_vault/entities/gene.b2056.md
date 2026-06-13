---
entity_id: "gene.b2056"
entity_type: "gene"
name: "wcaD"
source_database: "NCBI RefSeq"
source_id: "gene-b2056"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2056"
  - "wcaD"
---

# wcaD

`gene.b2056`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2056`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaD (gene.b2056) is a gene entity. It encodes wcaD (protein.P71238). Encoded protein function: Putative colanic acid polymerase EcoCyc product frame: G7101-MONOMER. Genomic coordinates: 2129661-2130878. EcoCyc protein note: wcaD is located within a cluster of genes that are responsible for production of the extracellular polysaccharide, CPD-21504 "colanic acid" (CA); WcaD is predicted to be an integral inner membrane protein and it may have a role in polymerising the CA hexasaccharide unit . A ΔwcaD mutant of an rcsA overexpressing, CA producing strain of E. coli K-12 MG1655 grows as misshapen rods and spheres and accumulates the pyruvylated hexasaccharide CPD-21522 repeat unit of CA; further deletion of EG11424 waaL, encoding O-antigen ligase, in this strain results in extensive cell lysis . The Keio collection wcaD mutant is sensitive to lithium (<90% growth at 200mM Li) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71238|protein.P71238]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006809,ECOCYC:G7101,GeneID:946550`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2129661-2130878:-; feature_type=gene
