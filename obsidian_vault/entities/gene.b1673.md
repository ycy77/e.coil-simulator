---
entity_id: "gene.b1673"
entity_type: "gene"
name: "ydhV"
source_database: "NCBI RefSeq"
source_id: "gene-b1673"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1673"
  - "ydhV"
---

# ydhV

`gene.b1673`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1673`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhV (gene.b1673) is a gene entity. It encodes ydhV (protein.P76192). Encoded protein function: FUNCTION: Probably a ferredoxin oxidoreductase that catalyzes the oxidation of aldehydes. {ECO:0000269|PubMed:30945846}. EcoCyc product frame: G6901-MONOMER. Genomic coordinates: 1751728-1753830. EcoCyc protein note: YdhV contains a redox-active CPD-15874 bis-Mo-MPT cofactor. Bis-Mo-MPT, which lacks the linked GMP moieties of CPD-15873, has not previously been observed as the cofactor of a molybdoenzyme . YdhV is a putative member of the aldehyde ferredoxin oxidoreductase family of molybdoenzymes . Based on sequence similarity, the ydhYVWXUT operon may encode components of an oxidoreductase . A ydhY-T mutant does not show a growth defect under anaerobic conditions, although utilization of certain sources of sulfur is impaired . In a ΔtusA strain, expression of ydhV is decreased in mid-exponential phase and under aerobic conditions . Reviews:

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76192|protein.P76192]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ydhV; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ydhV; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=ydhV; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=ydhV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005587,ECOCYC:G6901,GeneID:948756`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1751728-1753830:-; feature_type=gene
