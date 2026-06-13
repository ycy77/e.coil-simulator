---
entity_id: "gene.b1293"
entity_type: "gene"
name: "sapB"
source_database: "NCBI RefSeq"
source_id: "gene-b1293"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1293"
  - "sapB"
---

# sapB

`gene.b1293`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1293`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sapB (gene.b1293) is a gene entity. It encodes sapB (protein.P0AGH3). Encoded protein function: FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides. {ECO:0000269|PubMed:27803167}. EcoCyc product frame: SAPB-MONOMER. Genomic coordinates: 1354505-1355470. EcoCyc protein note: SapB is one of two integral membrane subunits of a predicted ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of a ΔsapB strain is significantly reduced compared to wild type .

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGH3|protein.P0AGH3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004350,ECOCYC:G2001,GeneID:946191`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1354505-1355470:-; feature_type=gene
