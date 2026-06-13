---
entity_id: "gene.b0751"
entity_type: "gene"
name: "pnuC"
source_database: "NCBI RefSeq"
source_id: "gene-b0751"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0751"
  - "pnuC"
---

# pnuC

`gene.b0751`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0751`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pnuC (gene.b0751) is a gene entity. It encodes pnuC (protein.P0AFK2). Encoded protein function: FUNCTION: Required for nicotinamide riboside transport across the inner membrane. {ECO:0000269|PubMed:15561822}. EcoCyc product frame: PNUC-MONOMER. Genomic coordinates: 783166-783885. EcoCyc protein note: PnuC is a nicotinamide riboside (NR) transporter and member of the nicotinamide ribonucleoside uptake permease family. E. coli pnuC expressed in an Haemophilus influenzae pnuC mutant is able to take up NR but is not able to import nicotinamide mononucleotide (NMN) . PnuC was initially annotated as a nicotinamide mononucleotide (NMN) transporter based on its homology to the PnuC protein from Salmonella enterica . However more recent work in Salmonella has indicated that PnuC in this organism is also an NR transporter which is consistent with its characterisation in E. coli. In Salmonella the conversion of NMN to NR prior to transport is catalysed by the periplasmic acid phosphatase APHA-CPLX AphA . PnuC is monomeric in detergent solution . PnuC variants which are able to transport thiamine have been developed PnuC functions to salvage exogenous NR which is converted to NAD in a two-step reaction catalysed by NadR (see PWY3O-4106) and .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFK2|protein.P0AFK2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002547,ECOCYC:EG11700,GeneID:945350`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:783166-783885:+; feature_type=gene
