---
entity_id: "gene.b2496"
entity_type: "gene"
name: "hda"
source_database: "NCBI RefSeq"
source_id: "gene-b2496"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2496"
  - "hda"
---

# hda

`gene.b2496`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2496`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hda (gene.b2496) is a gene entity. It encodes hda (protein.P69931). Encoded protein function: FUNCTION: Mediates the interactions of DNA replication initiator protein DnaA with DNA polymerase subunit beta sliding clamp (dnaN) (PubMed:15150238). Stimulates hydrolysis of ATP-DnaA to ADP-DnaA, rendering DnaA inactive for reinitiation, a process called regulatory inhibition of DnaA or RIDA (PubMed:9674428, PubMed:18977760, PubMed:12730188, PubMed:22716942). ADP-binding activates Hda to hydrolyze DnaA-ATP; Hda monomers bind to ADP with about 200-fold greater affinity than for ATP (PubMed:18977760). RIDA function can be genetically separated from viability, suggesting this protein has another function as well (PubMed:22716942). {ECO:0000269|PubMed:11483528, ECO:0000269|PubMed:12730188, ECO:0000269|PubMed:15150238, ECO:0000269|PubMed:18977760, ECO:0000269|PubMed:22716942, ECO:0000269|PubMed:9674428}.; FUNCTION: Suppresses the toxic effect of overexpressing a TrfA N-terminal 163 residue fragment. Inhibits inner membrane-associated plasmid IncP-alpha RK2 replication probably by interacting with plasmid-encoded TrfA. {ECO:0000269|PubMed:12618445}. EcoCyc product frame: G7313-MONOMER. EcoCyc synonyms: idaB, yfgE. Genomic coordinates: 2618075-2618776...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69931|protein.P69931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008217,ECOCYC:G7313,GeneID:946977`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2618075-2618776:-; feature_type=gene
