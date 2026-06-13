---
entity_id: "gene.b1290"
entity_type: "gene"
name: "sapF"
source_database: "NCBI RefSeq"
source_id: "gene-b1290"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1290"
  - "sapF"
---

# sapF

`gene.b1290`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1290`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sapF (gene.b1290) is a gene entity. It encodes sapF (protein.P0AAH8). Encoded protein function: FUNCTION: Part of a putrescine export transport system, does not play a role in resistance to antimicrobial peptides (PubMed:27803167). Does not stimulate K(+) uptake ability of TrkH on its own, but increases K(+) uptake by 20% in the presence of SapD; has no effect of TrkG (PubMed:11700350). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:27803167}. EcoCyc product frame: SAPF-MONOMER. Genomic coordinates: 1351828-1352634. EcoCyc protein note: SapF is one of two ATP-binding proteins of a predicted ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of a ΔsapF strain is significantly reduced compared to wild type . SapF contains signature motifs conserved in ATP-binding cassette (ABC) proteins .

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAH8|protein.P0AAH8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004339,ECOCYC:EG12305,GeneID:945335`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1351828-1352634:-; feature_type=gene
