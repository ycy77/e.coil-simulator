---
entity_id: "gene.b3493"
entity_type: "gene"
name: "pitA"
source_database: "NCBI RefSeq"
source_id: "gene-b3493"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3493"
  - "pitA"
---

# pitA

`gene.b3493`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3493`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pitA (gene.b3493) is a gene entity. It encodes pitA (protein.P0AFJ7). Encoded protein function: FUNCTION: Low-affinity inorganic phosphate transporter (PubMed:11489853, PubMed:328484, PubMed:6998957, PubMed:8110778). Mediates proton-driven uptake of soluble neutral metal phosphate (MeHP04) complexes (PubMed:8110778). It can use Mg(2+), Ca(2+), Co(2+) and Mn(2+) (PubMed:8110778). Activity impacts bacterial growth in low Mg(2+) conditions (PubMed:30276893). Is also involved in Zn(2+) uptake, probably via formation of a ZnHPO4 complex (PubMed:10713426). Can also transport arsenate (PubMed:328484). Involved in the uptake of tellurite (PubMed:23189244). {ECO:0000269|PubMed:10713426, ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:23189244, ECO:0000269|PubMed:30276893, ECO:0000269|PubMed:328484, ECO:0000269|PubMed:6998957, ECO:0000269|PubMed:8110778}. EcoCyc product frame: PITA-MONOMER. EcoCyc synonyms: pit. Genomic coordinates: 3637642-3639141. EcoCyc protein note: Early work in E. coli indicated that there are two genetically separable transport systems for inorganic phosphate (Pi) - a high affinity, low velocity Pst (phosphate specific transport) system (the ABC-27-CPLX) and a low affinity, high velocity Pit (Pi transport) system *. This latter system is constitutive in nature and catalyses an electrogenic metal phosphate:H+ symport...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFJ7|protein.P0AFJ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011407,ECOCYC:EG12230,GeneID:948009`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3637642-3639141:+; feature_type=gene
