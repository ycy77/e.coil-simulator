---
entity_id: "gene.b3724"
entity_type: "gene"
name: "phoU"
source_database: "NCBI RefSeq"
source_id: "gene-b3724"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3724"
  - "phoU"
---

# phoU

`gene.b3724`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3724`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoU (gene.b3724) is a gene entity. It encodes phoU (protein.P0A9K7). Encoded protein function: FUNCTION: Part of the phosphate (Pho) regulon, which plays a key role in phosphate homeostasis. Encoded together with proteins of the phosphate-specific transport (Pst) system in the polycistronic pstSCAB-phoU operon. PhoU is essential for the repression of the Pho regulon at high phosphate conditions. In this role, it may bind, possibly as a chaperone, to PhoR, PhoB or a PhoR-PhoB complex to promote dephosphorylation of phospho-PhoB, or inhibit formation of the PhoR-PhoB transitory complex. Is also part of complex networks important for bacterial virulence, tolerance to antibiotics and stress response. {ECO:0000269|PubMed:17420206, ECO:0000269|PubMed:6310121}. EcoCyc product frame: EG10735-MONOMER. EcoCyc synonyms: phoT, pst. Genomic coordinates: 3906853-3907578.

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9K7|protein.P0A9K7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phoU; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=phoU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012177,ECOCYC:EG10735,GeneID:948233`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3906853-3907578:-; feature_type=gene
