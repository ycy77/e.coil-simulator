---
entity_id: "gene.b3401"
entity_type: "gene"
name: "hslO"
source_database: "NCBI RefSeq"
source_id: "gene-b3401"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3401"
  - "hslO"
---

# hslO

`gene.b3401`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3401`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hslO (gene.b3401) is a gene entity. It encodes hslO (protein.P0A6Y5). Encoded protein function: FUNCTION: Redox regulated molecular chaperone. Protects both thermally unfolding and oxidatively damaged proteins from irreversible aggregation. Plays an important role in the bacterial defense system toward oxidative stress. EcoCyc product frame: G7744-MONOMER. EcoCyc synonyms: yrfI. Genomic coordinates: 3529774-3530652. EcoCyc protein note: hslO encodes the zinc-dependent, redox regulated chaperone known as Hsp33. Hsp33 is thought to function as a 'holdase' - a chaperone that binds tightly to unfolding proteins under stress conditions with subsequent release to chaperone 'foldases' (such as the DnaK system) when non-stress conditions resume. hslO expression is induced by heat shock (7 mins at 50°C); expression is stimulated by Eσ32 in an in vitro transcription-translation system . Purified Hsp33 suppresses thermal aggregation of the model substrates citrate synthase and firefly luciferase in vitro; purified Hsp33 exists in an equilibrium between reduced and oxidized species; chaperone activity is activated under oxidizing conditions...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Y5|protein.P0A6Y5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hslO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011096,ECOCYC:G7744,GeneID:947178`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3529774-3530652:+; feature_type=gene
