---
entity_id: "gene.b4337"
entity_type: "gene"
name: "mdtM"
source_database: "NCBI RefSeq"
source_id: "gene-b4337"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4337"
  - "mdtM"
---

# mdtM

`gene.b4337`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4337`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtM (gene.b4337) is a gene entity. It encodes mdtM (protein.P39386). Encoded protein function: FUNCTION: Proton-dependent efflux pump (PubMed:22426385, PubMed:23221628, PubMed:23701827, PubMed:24684269). Confers resistance to a broad spectrum of chemically unrelated substrates (PubMed:11566977, PubMed:22426385, PubMed:23221628, PubMed:23701827, PubMed:24684269). Overexpression confers resistance to acriflavine, chloramphenicol, norfloxacin, ethidium bromide and tetraphenylphosphonium bromide (TPP) (PubMed:11566977, PubMed:22426385). Can also export a broad range of quaternary ammonium compounds (QACs) and contribute to the intrinsic resistance of E.coli to these antimicrobial compounds (PubMed:23221628). In addition to its role in multidrug resistance, MdtM likely plays a physiological role in alkaline pH homeostasis and in resistance to bile salts (PubMed:23701827, PubMed:24684269, PubMed:28962921). May function in alkaline pH homeostasis when millimolar concentrations of sodium or potassium are present in the growth medium (PubMed:23701827). When overexpressed, can confer a tolerance to alkaline pH values up to 9.75 (PubMed:23701827)...

## Biological Role

Activated by slyA (protein.P0A8W2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39386|protein.P39386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=mdtM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014221,ECOCYC:EG12576,GeneID:948861`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4567287-4568519:-; feature_type=gene
