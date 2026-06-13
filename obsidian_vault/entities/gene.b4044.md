---
entity_id: "gene.b4044"
entity_type: "gene"
name: "dinF"
source_database: "NCBI RefSeq"
source_id: "gene-b4044"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4044"
  - "dinF"
---

# dinF

`gene.b4044`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4044`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinF (gene.b4044) is a gene entity. It encodes dinF (protein.P28303). Encoded protein function: DNA damage-inducible protein F EcoCyc product frame: DINF-MONOMER. Genomic coordinates: 4257742-4259121. EcoCyc protein note: DinF is a member of the Multi Antimicrobial Extrusion (MATE) Family of transporters ; DinF is implicated in protection from reactive oxygen species (ROS) possibly via the export of oxidizing species . Expression of dinF is DNA damage (UV or mitomycin C) inducible . dinF forms an operon with the SOS response regulator, lexA . DinF contains 12 predicted transmembrane domains ; multicopy expression of dinF decreases intracellular ROS (reactive oxygen species) levels and protects cells from H2O2-induced killing; DinF is implicated in protection against bile salts; multicopy expression of dinF confers a slight resistance to bile salts .

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28303|protein.P28303]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dinF; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=dinF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013243,ECOCYC:EG11491,GeneID:948554`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4257742-4259121:+; feature_type=gene
