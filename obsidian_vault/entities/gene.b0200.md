---
entity_id: "gene.b0200"
entity_type: "gene"
name: "gmhB"
source_database: "NCBI RefSeq"
source_id: "gene-b0200"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0200"
  - "gmhB"
---

# gmhB

`gene.b0200`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0200`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gmhB (gene.b0200) is a gene entity. It encodes gmhB (protein.P63228). Encoded protein function: FUNCTION: Converts the D-glycero-beta-D-manno-heptose 1,7-bisphosphate (beta-HBP) intermediate into D-glycero-beta-D-manno-heptose 1-phosphate by removing the phosphate group at the C-7 position. {ECO:0000269|PubMed:11751812, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:20050615, ECO:0000269|PubMed:31449400}. EcoCyc product frame: EG11736-MONOMER. EcoCyc synonyms: yaeD. Genomic coordinates: 222833-223408. EcoCyc protein note: gmhB encodes the D,D-heptose 1,7-bisphosphate phosphatase of the ADP-heptose biosynthesis pathway. GmhB belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. A gmhB deletion strain has a partial defect in LPS core synthesis, but is not completely heptoseless . GmhB has a narrow substrate range, with activity that is specific for ketohexose and ketoheptose bisphosphates, and shows high catalytic efficiency towards its physiological substrate . Crystal structures of apo-GmhB and several liganded forms have been solved, guiding construction of site-directed mutants that provide insight into substrate recognition elements in the catalytic site and suggest a reaction intermediate...

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63228|protein.P63228]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000675,ECOCYC:EG11736,GeneID:944879`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:222833-223408:+; feature_type=gene
