---
entity_id: "gene.b1158"
entity_type: "gene"
name: "pinE"
source_database: "NCBI RefSeq"
source_id: "gene-b1158"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1158"
  - "pinE"
---

# pinE

`gene.b1158`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1158`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pinE (gene.b1158) is a gene entity. It encodes pinE (protein.P03014). Encoded protein function: FUNCTION: This protein catalyzes the inversion of an 1800-bp E.coli DNA fragment, the P region, which can exist in either orientation. The function of the inversion is not yet clear. EcoCyc product frame: EG10737-MONOMER. EcoCyc synonyms: pin. Genomic coordinates: 1209685-1210239. EcoCyc protein note: Pin is a site-specific DNA recombinase that is a part of the e14 prophage element. Pin is a site-specific DNA recombinase, similar to the Gin recombinase of phage Mu. It is responsible for the inversion of the P region, an adjacent chunk of DNA containing EG12877, G6598, EG11120 and G6599 . Pin is part of e14, a UV-excisable element that is probably the remains of a prophage . Pin allows phase variation when Salmonella H1 and H2 regions are artificially introduced into E. coli .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03014|protein.P03014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003888,ECOCYC:EG10737,GeneID:945721`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1209685-1210239:+; feature_type=gene
