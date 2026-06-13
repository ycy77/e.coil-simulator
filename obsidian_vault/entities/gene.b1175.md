---
entity_id: "gene.b1175"
entity_type: "gene"
name: "minD"
source_database: "NCBI RefSeq"
source_id: "gene-b1175"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1175"
  - "minD"
---

# minD

`gene.b1175`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1175`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

minD (gene.b1175) is a gene entity. It encodes minD (protein.P0AEZ3). Encoded protein function: FUNCTION: ATPase required for the correct placement of the division site. Cell division inhibitors MinC and MinD act in concert to form an inhibitor capable of blocking formation of the polar Z ring septums. Rapidly oscillates between the poles of the cell to destabilize FtsZ filaments that have formed before they mature into polar Z rings. {ECO:0000269|PubMed:1836760, ECO:0000269|PubMed:22380631}. EcoCyc product frame: EG10597-MONOMER. EcoCyc synonyms: minB. Genomic coordinates: 1224549-1225361. EcoCyc protein note: The EG10596-MONOMER "MinC"-MinD-EG10598-MONOMER "MinE" system acts to direct septation to the proper (central) site in the dividing E. coli cell; the Min proteins are involved in a pole-to-pole oscillating system that restricts Z-ring formation to midcell. MinD recruits MinC to the membrane to form the MinC-MinD complex, which inhibits septum formation, and MinE acts to localize and restrict inhibition to the inappropriate septation sites . MinDE is also implicated in a generic mechanism which regulates the positioning of membrane proteins in cells; MinDE form a propagating diffusion barrier which regulates the positioning of functionally unrelated membrane-bound molecules in vitro...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEZ3|protein.P0AEZ3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003938,ECOCYC:EG10597,GeneID:945741`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1224549-1225361:-; feature_type=gene
