---
entity_id: "gene.b1599"
entity_type: "gene"
name: "mdtI"
source_database: "NCBI RefSeq"
source_id: "gene-b1599"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1599"
  - "mdtI"
---

# mdtI

`gene.b1599`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1599`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtI (gene.b1599) is a gene entity. It encodes mdtI (protein.P69210). Encoded protein function: FUNCTION: Catalyzes the excretion of spermidine. Can also confer resistance to deoxycholate and SDS. {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:18039771}. EcoCyc product frame: B1599-MONOMER. EcoCyc synonyms: ydgE. Genomic coordinates: 1672820-1673149. EcoCyc protein note: MdtI is one of two integral membrane subunits which constitute a heterodimeric multidrug / spermidine efflux transporter. MdtI (Em109) shares 33% sequence identity with the multidrug efflux pump, EmrE; purified MdtJ doesn't bind TPP+ and cannot form mixed oligomers with EmrE in vitro . Expression of chromosomal mdtJI is very low in both the presence and absence of spermidine .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69210|protein.P69210]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mdtI; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=mdtI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005343,ECOCYC:G6857,GeneID:947333`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1672820-1673149:-; feature_type=gene
