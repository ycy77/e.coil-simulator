---
entity_id: "gene.b4234"
entity_type: "gene"
name: "yjgA"
source_database: "NCBI RefSeq"
source_id: "gene-b4234"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4234"
  - "yjgA"
---

# yjgA

`gene.b4234`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4234`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjgA (gene.b4234) is a gene entity. It encodes darP (protein.P0A8X0). Encoded protein function: FUNCTION: Member of a network of 50S ribosomal subunit biogenesis factors (ObgE, RluD, RsfS and DarP) which assembles along the 30S-50S interface, preventing incorrect 23S rRNA structures from forming (PubMed:33639093). Promotes peptidyl transferase center (PTC) maturation (PubMed:33639093). Binds pre-50S ribosomal subunits near the 23S rRNA L1 stalk, where it may mediate correct positioning of the L1 stalk (PubMed:33639093). Plays a dual role in the late stages of assembly of the 50S ribosomal subunit; promotes peptidyl transferase center (PTC) maturation by modulating the docking of 23S rRNA helix H68, and maintains the stability of helix H89 with the help of uL16 (rplP), facilitating the final maturation of the PTC (Probable) (PubMed:38842932). Overexpression slows growth at 37 degrees Celsius (PubMed:38842932). {ECO:0000255|HAMAP-Rule:MF_00765, ECO:0000269|PubMed:33639093, ECO:0000269|PubMed:38842932, ECO:0000305|PubMed:38842932}. EcoCyc product frame: EG11410-MONOMER. Genomic coordinates: 4457314-4457865. EcoCyc protein note: YjgA interacts with nucleotides in a number of specific positions within 23S rRNA, connecting the central protuberance with the L1 stalk and moving it from its neutral position by ~20 Å. YjgA may thus have a quality control function...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8X0|protein.P0A8X0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013850,ECOCYC:EG11410,GeneID:948751`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4457314-4457865:-; feature_type=gene
