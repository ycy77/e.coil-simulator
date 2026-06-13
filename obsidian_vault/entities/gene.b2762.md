---
entity_id: "gene.b2762"
entity_type: "gene"
name: "cysH"
source_database: "NCBI RefSeq"
source_id: "gene-b2762"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2762"
  - "cysH"
---

# cysH

`gene.b2762`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2762`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysH (gene.b2762) is a gene entity. It encodes cysH (protein.P17854). Encoded protein function: FUNCTION: Catalyzes the formation of sulfite from phosphoadenosine 5'-phosphosulfate (PAPS) using thioredoxin as an electron donor. {ECO:0000255|HAMAP-Rule:MF_00063, ECO:0000269|PubMed:7588765}. EcoCyc product frame: PAPSSULFOTRANS-MONOMER. Genomic coordinates: 2887578-2888312.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17854|protein.P17854]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009057,ECOCYC:EG10189,GeneID:947230`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2887578-2888312:-; feature_type=gene
