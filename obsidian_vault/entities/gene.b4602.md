---
entity_id: "gene.b4602"
entity_type: "gene"
name: "cydH"
source_database: "NCBI RefSeq"
source_id: "gene-b4602"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4602"
  - "cydH"
---

# cydH

`gene.b4602`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4602`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cydH (gene.b4602) is a gene entity. It encodes ynhF (protein.A5A618). Encoded protein function: Uncharacterized protein YnhF EcoCyc product frame: MONOMER0-2822. EcoCyc synonyms: ynhF, cydY. Genomic coordinates: 1737456-1737545. EcoCyc protein note: CydH (also called CydY) is a small, noncatalytic, single transmembrane accessory subunit of CYT-D-UBIOX-CPLX . In the cryo-EM structure of cytochrome bd-I, CydH binds to a hydrophobic cleft in CydA . CydH appears to block dioxygen access to heme b595 . CydH is a chloroform-soluble protein that extracts with the lipid fraction of E. coli . CydH contains a predicted transmembrane segment, and the protein can be found in the membrane fraction . Experimental topology analysis suggests that CydH may be inserted into the membrane with dual orientation . CydH is expressed during both exponential growth and stationary phase . The amount of CydH protein is approximately 4-fold greater when cells are grown under oxygen limited conditions compared to aerobic growth in rich media . Tandem mass spectrometry indicates that the formyl group attached to the N-terminal methionine is retained .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A5A618|protein.A5A618]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285185,ECOCYC:G0-10594,GeneID:5061505`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1737456-1737545:-; feature_type=gene
