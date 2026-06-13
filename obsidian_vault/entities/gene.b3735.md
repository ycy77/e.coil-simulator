---
entity_id: "gene.b3735"
entity_type: "gene"
name: "atpH"
source_database: "NCBI RefSeq"
source_id: "gene-b3735"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3735"
  - "atpH"
---

# atpH

`gene.b3735`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3735`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpH (gene.b3735) is a gene entity. It encodes atpH (protein.P0ABA4). Encoded protein function: FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation.; FUNCTION: This protein is part of the stalk that links CF(0) to CF(1). It either transmits conformational changes from CF(0) to CF(1) or is implicated in proton conduction. EcoCyc product frame: ATPH-MONOMER. EcoCyc synonyms: papE, uncH. Genomic coordinates: 3919870-3920403. EcoCyc protein note: The delta subunit is required for binding the F1 complex to the F0 complex. It may also block proton conduction through the Fo complex.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABA4|protein.P0ABA4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpH; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012215,ECOCYC:EG10105,GeneID:948254`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3919870-3920403:-; feature_type=gene
