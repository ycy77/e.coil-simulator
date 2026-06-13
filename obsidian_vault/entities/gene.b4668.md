---
entity_id: "gene.b4668"
entity_type: "gene"
name: "ibsB"
source_database: "NCBI RefSeq"
source_id: "gene-b4668"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4668"
  - "ibsB"
---

# ibsB

`gene.b4668`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4668`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibsB (gene.b4668) is a gene entity. It encodes ibsB (protein.C1P608). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. EcoCyc product frame: MONOMER0-2858. Genomic coordinates: 2153681-2153737. EcoCyc protein note: The small open reading frame IbsB was detected by similarity to the open reading frames encoded on the opposite strand of the sib small RNAs . Based on similarity to IbsA and the transformation defect of a plasmid carrying sibB, overexpression of IbsB is predicted to be toxic to the cell . The SibB/IbsB locus was found in a genome-wide CRISPRi screen for genes that enable decoupling of growth and GFP accumulation . IbsB: "induction brings stasis"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P608|protein.C1P608]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-10632,GeneID:7751626`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2153681-2153737:-; feature_type=gene
