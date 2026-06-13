---
entity_id: "gene.b4242"
entity_type: "gene"
name: "mgtA"
source_database: "NCBI RefSeq"
source_id: "gene-b4242"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4242"
  - "mgtA"
---

# mgtA

`gene.b4242`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4242`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mgtA (gene.b4242) is a gene entity. It encodes mgtA (protein.P0ABB8). Encoded protein function: FUNCTION: Mediates magnesium influx to the cytosol (PubMed:40550995). Essential for bacterial growth during magnesium depletion (PubMed:40550995). {ECO:0000269|PubMed:40550995}. EcoCyc product frame: MGTA-MONOMER. EcoCyc synonyms: atmA, corB, mgt, mtg. Genomic coordinates: 4467625-4470321.

## Biological Role

Activated by rpoD (protein.P00579), zraR (protein.P14375), phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABB8|protein.P0ABB8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mgtA; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `C` - regulator=PhoP; target=mgtA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013883,ECOCYC:EG12525,GeneID:948778`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4467625-4470321:+; feature_type=gene
