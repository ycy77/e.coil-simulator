---
entity_id: "gene.b1174"
entity_type: "gene"
name: "minE"
source_database: "NCBI RefSeq"
source_id: "gene-b1174"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1174"
  - "minE"
---

# minE

`gene.b1174`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1174`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

minE (gene.b1174) is a gene entity. It encodes minE (protein.P0A734). Encoded protein function: FUNCTION: Prevents the cell division inhibition by proteins MinC and MinD at internal division sites while permitting inhibition at polar sites. This ensures cell division at the proper site by restricting the formation of a division septum at the midpoint of the long axis of the cell. {ECO:0000269|PubMed:22380631}. EcoCyc product frame: EG10598-MONOMER. EcoCyc synonyms: minB. Genomic coordinates: 1224279-1224545. EcoCyc protein note: The EG10596-MONOMER "MinC"-EG10597-MONOMER "MinD"-MinE system acts to direct septation to the proper (central) site in the dividing E. coli cell; the Min proteins are involved in a pole-to-pole oscillating system that restricts Z-ring formation to midcell. MinE is considered to be the 'topological specificity factor' that relieves MinCD inhibition of cell division specifically at mid-cell. MinDE is also implicated in a generic mechanism which regulates the positioning of membrane proteins in cells; MinDE form a propagating diffusion barrier which regulates the positioning of functionally unrelated membrane-bound molecules in vitro . MinDE constitutes the minimal set of proteins to drive the formation of FtsA-FtsZ cytoskeletal patterns on supported lipid bilayers...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A734|protein.P0A734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003935,ECOCYC:EG10598,GeneID:945740`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1224279-1224545:-; feature_type=gene
