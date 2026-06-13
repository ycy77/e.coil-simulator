---
entity_id: "gene.b2346"
entity_type: "gene"
name: "mlaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2346"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2346"
  - "mlaA"
---

# mlaA

`gene.b2346`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2346`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlaA (gene.b2346) is a gene entity. It encodes mlaA (protein.P76506). Encoded protein function: FUNCTION: Involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. {ECO:0000269|PubMed:19383799}. EcoCyc product frame: G7216-MONOMER. EcoCyc synonyms: vacJ. Genomic coordinates: 2464252-2465007. EcoCyc protein note: MlaA is an outer membrane lipoprotein implicated in a retrograde phospholipid trafficking pathway that is thought to maintain outer membrane lipid asymmetry by removing mislocalized outer leaflet phospholipids and transporting them back to the inner membrane; the Mla system comprises MlaA, the ABC-45-CPLX "MlaFEDB" complex in the inner membrane and a periplasmic protein, G7659-MONOMER "MlaC" . Evidence that the Mla system functions for anterograde phospholipid movement has also been reported . A ΔmlaA mutant has permeability defects of the outer membrane; the mutant strain shows no defects in LPS or outer membrane protein levels but does have increased sensitivity to SDS-EDTA; a ΔmlaA mutation in combination with any of ΔmlaF/E/D or ΔmlaC exhibits the same phenotype...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76506|protein.P76506]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007745,ECOCYC:G7216,GeneID:945582`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2464252-2465007:-; feature_type=gene
