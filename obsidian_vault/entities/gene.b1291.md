---
entity_id: "gene.b1291"
entity_type: "gene"
name: "sapD"
source_database: "NCBI RefSeq"
source_id: "gene-b1291"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1291"
  - "sapD"
---

# sapD

`gene.b1291`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1291`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sapD (gene.b1291) is a gene entity. It encodes sapD (protein.P0AAH4). Encoded protein function: FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides (PubMed:27803167). Stimulates K(+)-uptake proteins TrkG and TrkH to import K(+), may act via ATP-binding rather than ATP hydrolysis (PubMed:11700350). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:27803167}. EcoCyc product frame: SAPD-MONOMER. EcoCyc synonyms: trkE. Genomic coordinates: 1352636-1353628. EcoCyc protein note: SapD is one of two ATP-binding proteins of a predicted ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of a ΔsapD strain is significantly reduced compared to wild type . SapD contains signature motifs conserved in ATP-binding cassette (ABC) proteins . SapD (also known as TrkE) has been implicated in conferring ATP dependence to the K+ uptake proteins EG11020 "TrkG" and TRKH-MONOMER "TrkH" which are not related to the ABC superfamily...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAH4|protein.P0AAH4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004342,ECOCYC:EG12304,GeneID:946203`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1352636-1353628:-; feature_type=gene
