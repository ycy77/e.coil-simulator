---
entity_id: "gene.b1609"
entity_type: "gene"
name: "rstB"
source_database: "NCBI RefSeq"
source_id: "gene-b1609"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1609"
  - "rstB"
---

# rstB

`gene.b1609`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1609`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rstB (gene.b1609) is a gene entity. It encodes rstB (protein.P18392). Encoded protein function: FUNCTION: Member of the two-component regulatory system RstB/RstA. RstB functions as a membrane-associated protein kinase that phosphorylates RstA (Probable). {ECO:0000305|PubMed:15522865}. EcoCyc product frame: PHOSPHO-RSTB. EcoCyc synonyms: uspT. Genomic coordinates: 1682882-1684183. EcoCyc protein note: RstB is the sensor histidine kinase of the RstBA two-component signal transduction system . rstB and rstA - encoding its cognate response regulator - are transcribed together in an operon that is induced under low Mg2+ growth conditions through the PhoPQ two-component system EcoCyc protein note: This is the phosphorylated form of RSTB-MONOMER RstB - the sensor histidine kinase of the RstBA two-component signal transduction system.

## Biological Role

Activated by phoP (protein.P23836).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18392|protein.P18392]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=rstB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005372,ECOCYC:EG11233,GeneID:948870`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1682882-1684183:+; feature_type=gene
