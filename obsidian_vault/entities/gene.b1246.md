---
entity_id: "gene.b1246"
entity_type: "gene"
name: "oppD"
source_database: "NCBI RefSeq"
source_id: "gene-b1246"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1246"
  - "oppD"
---

# oppD

`gene.b1246`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1246`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oppD (gene.b1246) is a gene entity. It encodes oppD (protein.P76027). Encoded protein function: FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for energy coupling to the transport system (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}. EcoCyc product frame: OPPD-MONOMER. Genomic coordinates: 1304754-1305767. EcoCyc protein note: OppD is one of two predicted ATP-binding subunits of a high affinity uptake system for oligopeptides (with preference for tripeptides - including murein tripeptides* - and tetrapeptides); OppD contains signature motifs conserved in ATP-binding cassette (ABC) domains . * uptake of murein tripeptide requires the periplasmic murein tripeptide binding protein, MppA

## Biological Role

Repressed by fur (protein.P0A9A9), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76027|protein.P76027]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=oppD; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=oppD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004178,ECOCYC:EG10677,GeneID:945802`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1304754-1305767:+; feature_type=gene
