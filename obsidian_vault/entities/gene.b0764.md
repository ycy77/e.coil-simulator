---
entity_id: "gene.b0764"
entity_type: "gene"
name: "modB"
source_database: "NCBI RefSeq"
source_id: "gene-b0764"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0764"
  - "modB"
---

# modB

`gene.b0764`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0764`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

modB (gene.b0764) is a gene entity. It encodes modB (protein.P0AF01). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for molybdenum; probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: MODB-MONOMER. EcoCyc synonyms: chlJ, tslJ. Genomic coordinates: 795862-796551. EcoCyc protein note: ModB is the predicted integral membrane subunit of an ABC transporter that mediates the high affinity uptake of molybdate. modB encodes a hydrophobic protein with 5 predicted transmembrane regions .

## Biological Role

Repressed by modE (protein.P0A9G8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF01|protein.P0AF01]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=modB; function=+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=modB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002603,ECOCYC:EG10002,GeneID:945361`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:795862-796551:+; feature_type=gene
