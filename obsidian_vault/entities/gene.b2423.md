---
entity_id: "gene.b2423"
entity_type: "gene"
name: "cysW"
source_database: "NCBI RefSeq"
source_id: "gene-b2423"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2423"
  - "cysW"
---

# cysW

`gene.b2423`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2423`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysW (gene.b2423) is a gene entity. It encodes cysW (protein.P0AEB0). Encoded protein function: FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: CYSW-MONOMER. Genomic coordinates: 2540804-2541679. EcoCyc protein note: CysW is one of two predicted inner membrane subunits of an ATP-dependent sulfate/thiosulfate uptake system; CysW contains 50% hydrophobic residues

## Biological Role

Activated by rpoD (protein.P00579), cysB (protein.P0A9F3).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEB0|protein.P0AEB0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysW; function=+
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cysW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007988,ECOCYC:EG10198,GeneID:2847743`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2540804-2541679:-; feature_type=gene
