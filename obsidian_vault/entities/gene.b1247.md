---
entity_id: "gene.b1247"
entity_type: "gene"
name: "oppF"
source_database: "NCBI RefSeq"
source_id: "gene-b1247"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1247"
  - "oppF"
---

# oppF

`gene.b1247`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1247`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oppF (gene.b1247) is a gene entity. It encodes oppF (protein.P77737). Encoded protein function: FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for energy coupling to the transport system (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}. EcoCyc product frame: OPPF-MONOMER. Genomic coordinates: 1305764-1306768. EcoCyc protein note: OppF is one of two predicted ATP-binding subunits of a high affinity uptake system for oligopeptides (with preference for tripeptides - including murein tripeptides* - and tetrapeptides); OppF contains signature motifs conserved in ATP-binding cassette (ABC) domains . * uptake of murein tripeptide requires the periplasmic murein tripeptide binding protein, MppA

## Biological Role

Repressed by fur (protein.P0A9A9), lrp (protein.P0ACJ0). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77737|protein.P77737]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=oppF; function=-+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=oppF; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=oppF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004182,ECOCYC:EG10678,GeneID:945818`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1305764-1306768:+; feature_type=gene
