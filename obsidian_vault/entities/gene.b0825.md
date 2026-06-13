---
entity_id: "gene.b0825"
entity_type: "gene"
name: "fsaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0825"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0825"
  - "fsaA"
---

# fsaA

`gene.b0825`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0825`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fsaA (gene.b0825) is a gene entity. It encodes fsaA (protein.P78055). Encoded protein function: FUNCTION: Catalyzes the reversible formation of fructose 6-phosphate from dihydroxyacetone (DHA) and D-glyceraldehyde 3-phosphate via an aldolization reaction. Can utilize several aldehydes as acceptor compounds in vitro, and hydroxyacetone (HA) or 1-hydroxy-butan-2-one as alternative donor substrate. Is also able to catalyze the direct stereoselective self-aldol addition of glycolaldehyde to furnish D-(-)-threose, and cross-aldol reactions of glycolaldehyde to other aldehyde acceptors. Is not able to cleave fructose, fructose 1-phosphate, glucose 6-phosphate, sedoheptulose 1,7-bisphosphate, xylulose 5-phosphate, ribulose 5-phosphate, and fructose 1,6-bisphosphate; cannot use dihydroxyacetone phosphate as donor compound nor D-glyceraldehyde as acceptor. Does not display transaldolase activity. {ECO:0000269|PubMed:11120740, ECO:0000269|PubMed:17985886, ECO:0000269|PubMed:19554584, ECO:0000269|Ref.6}. EcoCyc product frame: G6428-MONOMER. EcoCyc synonyms: ybiZ, fsa, mipB. Genomic coordinates: 863642-864304.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P78055|protein.P78055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002818,ECOCYC:G6428,GeneID:945449`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:863642-864304:+; feature_type=gene
