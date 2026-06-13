---
entity_id: "gene.b0950"
entity_type: "gene"
name: "pqiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0950"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0950"
  - "pqiA"
---

# pqiA

`gene.b0950`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0950`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pqiA (gene.b0950) is a gene entity. It encodes pqiA (protein.P0AFL9). Encoded protein function: FUNCTION: Component of a transport pathway that contributes to membrane integrity. {ECO:0000269|PubMed:27795327}. EcoCyc product frame: G6490-MONOMER. EcoCyc synonyms: pqi5, pqi5A. Genomic coordinates: 1012001-1013254. EcoCyc protein note: PqiA is an inner membrane protein with six transmembrane regions . pqiA, pqiB and pqiC form an operon which is a member of the soxRS regulon ; expression is induced during exponential growth, by paraquat and other agents known to produce superoxide radicals within cells, such as menadione, phenazine methosulfate, and plumbagin, but not by hydrogen peroxide, ethanol nor heat shock . Expression increases under carbon or phosphate starvation or during stationary phase in an RpoS dependent manner; expression is regulated independently by SoxS and RpoS . A pqiA mutant has no obvious phenotype, including no change in resistance to oxidants...

## Biological Role

Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFL9|protein.P0AFL9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pqiA; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=pqiA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=pqiA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pqiA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003219,ECOCYC:G6490,GeneID:944999`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1012001-1013254:+; feature_type=gene
