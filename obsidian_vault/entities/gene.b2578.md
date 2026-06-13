---
entity_id: "gene.b2578"
entity_type: "gene"
name: "eamB"
source_database: "NCBI RefSeq"
source_id: "gene-b2578"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2578"
  - "eamB"
---

# eamB

`gene.b2578`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2578`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eamB (gene.b2578) is a gene entity. It encodes eamB (protein.P38101). Encoded protein function: FUNCTION: Exporter of O-acetylserine (OAS) and cysteine. {ECO:0000269|PubMed:12562784}. EcoCyc product frame: EG12445-MONOMER. EcoCyc synonyms: yfiK. Genomic coordinates: 2715423-2716010. EcoCyc protein note: EamB (formerly YfiK) is an integral membrane protein . In a strain that is insensitive to feedback inhibition by L-cysteine, overexpression of eamB causes accumulation of L-cysteine and O-acetylserine in the culture medium; overexpression of eamB counteracts the toxicity associated with increased levels of O-acetylserine and increases resistance to the glutamine antagonist, L-AZASERINE; EamB appears to act independently of EG11639-MONOMER "EamA", an alternate O-acetylserine and cysteine efflux permease; the physiological function of EamB is not clear . In the Transporter Classification Database , EamB is a member of the Resistance to Homoserine/Threonine (RhtB) Family (see also ).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38101|protein.P38101]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008487,ECOCYC:EG12445,GeneID:947065`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2715423-2716010:+; feature_type=gene
