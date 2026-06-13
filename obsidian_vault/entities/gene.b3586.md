---
entity_id: "gene.b3586"
entity_type: "gene"
name: "yiaV"
source_database: "NCBI RefSeq"
source_id: "gene-b3586"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3586"
  - "yiaV"
---

# yiaV

`gene.b3586`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3586`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaV (gene.b3586) is a gene entity. It encodes yiaV (protein.P37683). Encoded protein function: Inner membrane protein YiaV EcoCyc product frame: EG12290-MONOMER. Genomic coordinates: 3752963-3754099. EcoCyc protein note: YiaV is predicted to be an inner membrane protein with two transmembrane domains; experimental topology analysis suggests the C terminus is located in the periplasm . YiaV has also been predicted to be a bitopic (single pass) inner membrane protein . YiaV is a member of the Membrane Fusion Protein (MFP) Family A transposon insertion in the yiaW-aldB intergenic region has higher tolerance to kanamycin, while a mutant lacking that region is more sensitive to kanamycin than wild type. A yiaV deletion has no effect on kanamycin sensitivity .

## Biological Role

Activated by yiaU (protein.P37682).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37683|protein.P37683]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37682|protein.P37682]] `RegulonDB` `C` - regulator=YiaU; target=yiaV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011712,ECOCYC:EG12290,GeneID:948106`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3752963-3754099:-; feature_type=gene
