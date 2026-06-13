---
entity_id: "gene.b1186"
entity_type: "gene"
name: "nhaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1186"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1186"
  - "nhaB"
---

# nhaB

`gene.b1186`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1186`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nhaB (gene.b1186) is a gene entity. It encodes nhaB (protein.P0AFA7). Encoded protein function: FUNCTION: Na(+)/H(+) antiporter that extrudes sodium in exchange for external protons (PubMed:1317851, PubMed:7929345, PubMed:8019504, PubMed:8093613). Catalyzes the exchange of 3 H(+) per 2 Na(+) (PubMed:7929345). Can also transport lithium (PubMed:8019504). Essential for regulation of intracellular pH under alkaline conditions (PubMed:7822245). Is necessary for growth on Na(+)/symport substrates such as glutamate and proline under conditions in which nhaA is not expressed, such as acidic pH and low Na(+) concentration (PubMed:8093613). {ECO:0000269|PubMed:1317851, ECO:0000269|PubMed:7822245, ECO:0000269|PubMed:7929345, ECO:0000269|PubMed:8019504, ECO:0000269|PubMed:8093613}. EcoCyc product frame: NHAB-MONOMER. Genomic coordinates: 1233176-1234717. EcoCyc protein note: nhaB encodes a Na+:H+ antiporter implicated in alkaline pH homeostasis. E. coli contains other transporters which mediate active proton uptake for alkaline pH homeostasis including CPLX0-7629 "NhaA" (the prominent Na+:H+ antiporter), CHAA-MONOMER "ChaA", CMR-MONOMER "MdfA" and YJIO-MONOMER "MdtM", each of which may function under varying conditions of external pH and cation composition (see ) Purified, reconstituted NhaB is an electrogenic antiporter with a stoichiometry of 3H+:2Na+...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFA7|protein.P0AFA7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003984,ECOCYC:EG11392,GeneID:944822`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1233176-1234717:-; feature_type=gene
