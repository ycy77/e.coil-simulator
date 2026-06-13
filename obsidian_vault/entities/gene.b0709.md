---
entity_id: "gene.b0709"
entity_type: "gene"
name: "dtpD"
source_database: "NCBI RefSeq"
source_id: "gene-b0709"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0709"
  - "dtpD"
---

# dtpD

`gene.b0709`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0709`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dtpD (gene.b0709) is a gene entity. It encodes dtpD (protein.P75742). Encoded protein function: FUNCTION: Probable proton-dependent permease that transports dipeptides. {ECO:0000250}. EcoCyc product frame: B0709-MONOMER. EcoCyc synonyms: ybgH. Genomic coordinates: 741075-742556. EcoCyc protein note: DtpD is a member of the Proton-dependent Oligopeptide Transporter (POT) family within the Major Facilitator Superfamily (MFS) . DtpD, purified from E. coli strain O157:H7, is monomeric when solubilized in detergent; the overexpressed protein mediates the uptake of a labeled dipeptide mimic (6-aminohexanoic acid); the transporter displays a preference for dipeptides with a cationic amino acid in the in the C-terminal position (dipeptides with lysine or arginine in the C-terminal position inhibit uptake of 6-aminohexanoic acid whereas dipeptides with lysine or arginine at the N-terminus do not) . DtpB contains two pseudosymmetric domains and is believed to function by an alternating access mechanism; a crystal structure of DtpD in the inward facing conformation (ie central cavity open towards the cytosol) is available .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75742|protein.P75742]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002420,ECOCYC:G6378,GeneID:947368`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:741075-742556:-; feature_type=gene
