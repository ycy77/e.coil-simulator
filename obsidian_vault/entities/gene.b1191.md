---
entity_id: "gene.b1191"
entity_type: "gene"
name: "cvrA"
source_database: "NCBI RefSeq"
source_id: "gene-b1191"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1191"
  - "cvrA"
---

# cvrA

`gene.b1191`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1191`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cvrA (gene.b1191) is a gene entity. It encodes cvrA (protein.P76007). Encoded protein function: FUNCTION: K(+)/H(+) antiporter that extrudes potassium in exchange for external protons and maintains the internal concentration of potassium under toxic levels (By similarity). Participates in control of cell volume in low-osmolarity conditions. {ECO:0000255|HAMAP-Rule:MF_01075, ECO:0000269|PubMed:11700351}. EcoCyc product frame: YCGO-MONOMER. EcoCyc synonyms: ycgO. Genomic coordinates: 1240335-1242071. EcoCyc protein note: CvrA (formerly YcgO) belongs to the Monovalent Cation:Proton Antiporter-1 (CPA1) Family - members of which typically catalyse Na+:H+ antiport . CvrA has been implicated in K+ efflux and may function as a K+:H+ antiporter with a role in adaptive stress relief . YcgO is not involved in respiration-driven Na+ transport; Na+ export is not affected in a ΔycgO strain . A ΔycgO strain is sensitive to low osmolarity; growth inhibition is observed in low salt media. A ΔycgO strain has disrupted alkali cation transport when grown at low osmolarity; a ΔycgO strain has decreased intracellular K+ levels when grown at low osmolarity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76007|protein.P76007]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003999,ECOCYC:G6620,GeneID:945755`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1240335-1242071:-; feature_type=gene
