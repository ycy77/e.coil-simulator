---
entity_id: "gene.b2424"
entity_type: "gene"
name: "cysU"
source_database: "NCBI RefSeq"
source_id: "gene-b2424"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2424"
  - "cysU"
---

# cysU

`gene.b2424`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2424`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysU (gene.b2424) is a gene entity. It encodes cysU (protein.P16701). Encoded protein function: FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: CYST-MONOMER. EcoCyc synonyms: cysT. Genomic coordinates: 2541679-2542512. EcoCyc protein note: CysU is one of two predicted inner membrane subunits of an ATP-dependent sulfate/thiosulfate uptake system; CysU contains 50% hydrophobic residues

## Biological Role

Activated by rpoD (protein.P00579), cysB (protein.P0A9F3).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16701|protein.P16701]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysU; function=+
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cysU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007990,ECOCYC:EG10197,GeneID:946882`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2541679-2542512:-; feature_type=gene
