---
entity_id: "gene.b4669"
entity_type: "gene"
name: "ilvX"
source_database: "NCBI RefSeq"
source_id: "gene-b4669"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4669"
  - "ilvX"
---

# ilvX

`gene.b4669`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4669`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvX (gene.b4669) is a gene entity. It encodes ilvX (protein.C1P619). Encoded protein function: Uncharacterized protein IlvX EcoCyc product frame: MONOMER0-2868. Genomic coordinates: 3950507-3950557. EcoCyc protein note: The IlvX open reading frame was predicted based on the presence of a ribosome binding site in an intergenic region, and expression of the small protein was detected during stationary phase . As expected, levels of IlvX are higher during growth in minimal medium compared to rich medium .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P619|protein.C1P619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvX; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285213,ECOCYC:G0-10641,GeneID:7751639`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3950507-3950557:+; feature_type=gene
