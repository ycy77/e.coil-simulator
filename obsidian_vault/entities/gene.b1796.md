---
entity_id: "gene.b1796"
entity_type: "gene"
name: "yoaG"
source_database: "NCBI RefSeq"
source_id: "gene-b1796"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1796"
  - "yoaG"
---

# yoaG

`gene.b1796`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1796`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaG (gene.b1796) is a gene entity. It encodes yoaG (protein.P64496). Encoded protein function: Protein YoaG EcoCyc product frame: G6982-MONOMER. Genomic coordinates: 1879403-1879585. EcoCyc protein note: A yoaG mutant is more sensitive to hydrogen peroxide and cadmium than wild type and shows increased biofilm formation compared to wild type . yoaG is thought to form an operon together with yeaR. Transcription of yoaG is induced in response to nitrate ; yeaR transcription was also shown to be induced in response to nitrite and nitric oxide .

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579), narL (protein.P0AF28).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64496|protein.P64496]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yoaG; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=yoaG; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=yoaG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005976,ECOCYC:G6982,GeneID:946314`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1879403-1879585:-; feature_type=gene
