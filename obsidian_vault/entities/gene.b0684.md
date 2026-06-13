---
entity_id: "gene.b0684"
entity_type: "gene"
name: "fldA"
source_database: "NCBI RefSeq"
source_id: "gene-b0684"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0684"
  - "fldA"
---

# fldA

`gene.b0684`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0684`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fldA (gene.b0684) is a gene entity. It encodes fldA (protein.P61949). Encoded protein function: FUNCTION: Low-potential electron donor to a number of redox enzymes (Potential). Involved in the reactivation of inactive cob(II)alamin in methionine synthase. {ECO:0000269|PubMed:9730838, ECO:0000305}. EcoCyc product frame: OX-FLAVODOXIN1. Genomic coordinates: 710935-711465. EcoCyc protein note: Flavodoxins are small, acidic electron transfer proteins which contain FMN as a prosthetic group. They are only able to accept and donate electrons. Flavodoxin is an important member of the multi-enzyme complexes that are involved in the activation of anaerobic nucleoside reductase and pyruvate-formate lyase. Flavodoxins are functionally interchangeable with ferredoxins, but some enzymes are specific for one or the other. E. coli has at least two flavodoxins . FldA is essential under both aerobic and anaerobic growth conditions . The essential role for flavodoxin 1 under aerobic conditions is in the MEP pathway for isoprenoid biosynthesis (NONMEVIPP-PWY) . Crystal and solution structures of FldA have been solved .

## Biological Role

Activated by soxS (protein.P0A9E2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61949|protein.P61949]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=fldA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002332,ECOCYC:EG10318,GeneID:945293`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:710935-711465:-; feature_type=gene
