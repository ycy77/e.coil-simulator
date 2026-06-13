---
entity_id: "gene.b3736"
entity_type: "gene"
name: "atpF"
source_database: "NCBI RefSeq"
source_id: "gene-b3736"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3736"
  - "atpF"
---

# atpF

`gene.b3736`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3736`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpF (gene.b3736) is a gene entity. It encodes atpF (protein.P0ABA0). Encoded protein function: FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation. {ECO:0000255|HAMAP-Rule:MF_01398}.; FUNCTION: Component of the F(0) channel, it forms part of the peripheral stalk, linking F(1) to F(0). {ECO:0000255|HAMAP-Rule:MF_01398}. EcoCyc product frame: ATPF-MONOMER. EcoCyc synonyms: papF, uncF. Genomic coordinates: 3920418-3920888.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABA0|protein.P0ABA0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012217,ECOCYC:EG10103,GeneID:948247`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3920418-3920888:-; feature_type=gene
