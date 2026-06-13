---
entity_id: "gene.b2035"
entity_type: "gene"
name: "wbbH"
source_database: "NCBI RefSeq"
source_id: "gene-b2035"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2035"
  - "wbbH"
---

# wbbH

`gene.b2035`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2035`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wbbH (gene.b2035) is a gene entity. It encodes wbbH (protein.P37748). Encoded protein function: FUNCTION: May function in vitro as a polymerase that catalyzes the polymerization of the O-antigen repeat units on the periplasmic face of the inner membrane, leading to the formation of the lipid-linked O-antigen molecule (Probable). However, E.coli K12 strains do not normally produce the O-antigen in vivo due to mutations in the rfb gene cluster (Probable). K12 strains are phenotypically rough, their lipopolysaccharide having a complete core structure, but no O-antigen (Probable). {ECO:0000305, ECO:0000305|PubMed:7517390, ECO:0000305|PubMed:7517391}. EcoCyc product frame: EG11982-MONOMER. EcoCyc synonyms: yefF, rfc, wzyB. Genomic coordinates: 2106060-2107226. EcoCyc protein note: wzyB (also called wbbH) encodes the O-antigen polymerase of a Wzx/Wzy-dependent pathway of O-antigen synthesis; Wzy family polymerases are integral membrane proteins that transfer growing lipid-linked O-polysaccharides onto the non-reducing end of a newly flipped Und-PP-linked repeat unit (see ). E. coli K-12 is phenotypically rough and does not express O-antigen due to mutations in the rfb region; E. coli K-12 MG1655 contains the rfb-50 mutation - an IS5 element which disrupts EG11986 wbbL encoding rhamnose transferase; an engineered strain of E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37748|protein.P37748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006753,ECOCYC:EG11982,GeneID:945179`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2106060-2107226:-; feature_type=gene
