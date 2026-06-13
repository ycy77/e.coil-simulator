---
entity_id: "gene.b0270"
entity_type: "gene"
name: "yagG"
source_database: "NCBI RefSeq"
source_id: "gene-b0270"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0270"
  - "yagG"
---

# yagG

`gene.b0270`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0270`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagG (gene.b0270) is a gene entity. It encodes yagG (protein.P75683). Encoded protein function: Putative glycoside/cation symporter YagG EcoCyc product frame: B0270-MONOMER. Genomic coordinates: 285395-286777. EcoCyc protein note: yagGH is predicted to be a member of the EG20253-MONOMER "XylR" regulon; its products may mediate transport (YagG) and hydrolysis (YagH) of xylooligosaccharides; putative XylR and CRP binding sites are identified upstream of yagGH . yagG may be part of a single yagEFGH operon which is under control of G6144-MONOMER "XynR" - the regulator of xylonate catabolism; YagG is a putative D-XYLONATE uptake transporter . YagG is a member of the GPH family of glycoside-pentoside-hexuronide transporters .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75683|protein.P75683]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000929,ECOCYC:G6142,GeneID:944947`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:285395-286777:+; feature_type=gene
