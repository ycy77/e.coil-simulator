---
entity_id: "gene.b4268"
entity_type: "gene"
name: "idnK"
source_database: "NCBI RefSeq"
source_id: "gene-b4268"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4268"
  - "idnK"
---

# idnK

`gene.b4268`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4268`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

idnK (gene.b4268) is a gene entity. It encodes idnK (protein.P39208). Encoded protein function: Thermosensitive gluconokinase (EC 2.7.1.12) (Gluconate kinase 1) EcoCyc product frame: GLUCONOKINI-MONOMER. EcoCyc synonyms: gntV. Genomic coordinates: 4494623-4495186. EcoCyc protein note: E. coli encodes two D-gluconate kinases which can be distinguished by their thermal sensitivity. The idnK-encoded enzyme, described here, is thermosensitive , and its primary function is in the L-idonate degradation pathway . When grown on D-gluconate, the gntK-encoded thermostable enzyme is prevalent . Gluconokinase activity is induced by growth on gluconate . Expression of idnK is catabolite repressed and induced by L-idonate or 5-ketogluconate . An idnK insertion mutant is unable to grow on L-idonate or 5-ketogluconate as the sole source of carbon, and an idnK gntK double mutant is also unable to grow on D-gluconate as the sole source of carbon . GntV: "gluconate" IdnK: "idonate" Review:

## Biological Role

Repressed by glaR (protein.P37338). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39208|protein.P39208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=idnK; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=idnK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013980,ECOCYC:EG12152,GeneID:946066`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4494623-4495186:+; feature_type=gene
