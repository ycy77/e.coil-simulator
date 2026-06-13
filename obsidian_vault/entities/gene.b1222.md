---
entity_id: "gene.b1222"
entity_type: "gene"
name: "narX"
source_database: "NCBI RefSeq"
source_id: "gene-b1222"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1222"
  - "narX"
---

# narX

`gene.b1222`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1222`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narX (gene.b1222) is a gene entity. It encodes narX (protein.P0AFA2). Encoded protein function: FUNCTION: Acts as a sensor for nitrate/nitrite and transduces signal of nitrate availability to the NarL protein and of both nitrate/nitrite to the NarP protein. NarX probably activates NarL and NarP by phosphorylation in the presence of nitrate. NarX also plays a negative role in controlling NarL activity, probably through dephosphorylation in the absence of nitrate. EcoCyc product frame: NARX-MONOMER. EcoCyc synonyms: frdR, narR, frd1. Genomic coordinates: 1275822-1277618.

## Biological Role

Repressed by fnr (protein.P0A9E5), nac (protein.Q47005). Activated by modE (protein.P0A9G8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFA2|protein.P0AFA2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=narX; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=narX; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=narX; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004099,ECOCYC:EG10646,GeneID:945788`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1275822-1277618:-; feature_type=gene
