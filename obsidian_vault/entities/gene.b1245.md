---
entity_id: "gene.b1245"
entity_type: "gene"
name: "oppC"
source_database: "NCBI RefSeq"
source_id: "gene-b1245"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1245"
  - "oppC"
---

# oppC

`gene.b1245`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1245`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oppC (gene.b1245) is a gene entity. It encodes oppC (protein.P0AFH6). Encoded protein function: FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for the translocation of the substrate across the membrane (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}. EcoCyc product frame: OPPC-MONOMER. Genomic coordinates: 1303834-1304742. EcoCyc protein note: OppC is one of two predicted integral membrane subunits of an ATP-dependent uptake system for oligopeptides (with preference for tripeptides - including murein tripeptides* - and tetrapeptides) . * uptake of murein tripeptide requires the periplasmic murein tripeptide binding protein, MppA

## Biological Role

Repressed by fur (protein.P0A9A9), lrp (protein.P0ACJ0), nac (protein.Q47005).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFH6|protein.P0AFH6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=oppC; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=oppC; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=oppC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004176,ECOCYC:EG10676,GeneID:945810`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1303834-1304742:+; feature_type=gene
