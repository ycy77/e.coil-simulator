---
entity_id: "gene.b1488"
entity_type: "gene"
name: "ddpX"
source_database: "NCBI RefSeq"
source_id: "gene-b1488"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1488"
  - "ddpX"
---

# ddpX

`gene.b1488`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1488`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddpX (gene.b1488) is a gene entity. It encodes ddpX (protein.P77790). Encoded protein function: FUNCTION: Catalyzes hydrolysis of the D-alanyl-D-alanine dipeptide. May have a role in cell-wall turnover. {ECO:0000255|HAMAP-Rule:MF_01924, ECO:0000269|PubMed:9751644}. EcoCyc product frame: G6782-MONOMER. EcoCyc synonyms: vanX, yddT. Genomic coordinates: 1562495-1563076. EcoCyc protein note: VanX is a D-Ala-D-Ala dipeptidase, which catalyzes hydrolysis of the D-alanyl-D-alanine dipeptide required for wild-type peptidoglycan biosynthesis . VanX activity has been characterized . VanX-related proteins are involved in the production of a variant peptidoglycan that results in resistance of pathogenic bacteria to the antibiotic vancomycin; see . VanX may act in murein recycling . VanX allows D-Ala-D-Ala to be utilized as a carbon source, which may have significance with respect to survival at stationary phase . Regulation has been described . The vanX gene has sequences indicative of RpoS regulation . Review: .

## Enriched Pathways

- `eco01502` Vancomycin resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77790|protein.P77790]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004960,ECOCYC:G6782,GeneID:945532`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1562495-1563076:-; feature_type=gene
