---
entity_id: "gene.b4664"
entity_type: "gene"
name: "ibsD"
source_database: "NCBI RefSeq"
source_id: "gene-b4664"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4664"
  - "ibsD"
---

# ibsD

`gene.b4664`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4664`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibsD (gene.b4664) is a gene entity. It encodes ibsD (protein.C1P616). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. EcoCyc product frame: MONOMER0-2856. Genomic coordinates: 3194766-3194825. EcoCyc protein note: The small open reading frame IbsD was detected by similarity to the open reading frames encoded on the opposite strand of the sib small RNAs . Based on similarity to IbsA and the transformation defect of a plasmid carrying sibD, overexpression of IbsD is predicted to be toxic to the cell . IbsD: "induction brings stasis"

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P616|protein.C1P616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ibsD; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10630,GeneID:7751628`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3194766-3194825:+; feature_type=gene
