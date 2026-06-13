---
entity_id: "gene.b0479"
entity_type: "gene"
name: "fsr"
source_database: "NCBI RefSeq"
source_id: "gene-b0479"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0479"
  - "fsr"
---

# fsr

`gene.b0479`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0479`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fsr (gene.b0479) is a gene entity. It encodes fsr (protein.P52067). Encoded protein function: FUNCTION: Confers the resistance against fosmidomycin. EcoCyc product frame: FSR-MONOMER. Genomic coordinates: 503476-504696. EcoCyc protein note: Fsr is a putative fosmidomycin efflux protein. Expression of cloned fsr in a wild-type strain of E. coli K-12 confers resistance to this antibiotic; Fsr contains 12 putative transmembrane regions . Expression of cloned mdtG in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a 32-fold increase in resistance to fosmidomycin and a two-fold increase in resistance to trimethoprim but does not impact the resistance to a range of other antibiotics, dyes and toxic compounds . In the Transporter Classification Database, Fsr is a member of the Fosmidomycin Resistance (Fsr) Family within the Major Facilitator Superfamily . fsr is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52067|protein.P52067]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001661,ECOCYC:G6256,GeneID:945119`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:503476-504696:-; feature_type=gene
