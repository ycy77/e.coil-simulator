---
entity_id: "gene.b1244"
entity_type: "gene"
name: "oppB"
source_database: "NCBI RefSeq"
source_id: "gene-b1244"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1244"
  - "oppB"
---

# oppB

`gene.b1244`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1244`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oppB (gene.b1244) is a gene entity. It encodes oppB (protein.P0AFH2). Encoded protein function: FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for the translocation of the substrate across the membrane (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}. EcoCyc product frame: OPPB-MONOMER. Genomic coordinates: 1302899-1303819. EcoCyc protein note: OppB is one of two predicted integral membrane subunits of an ATP-dependent uptake system for oligopeptides (with preference for tripeptides - including murein tripeptides* - and tetrapeptides) . * uptake of murein tripeptide requires the periplasmic murein tripeptide binding protein, MppA

## Biological Role

Repressed by fur (protein.P0A9A9), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFH2|protein.P0AFH2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=oppB; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=oppB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004174,ECOCYC:EG10675,GeneID:945823`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1302899-1303819:+; feature_type=gene
