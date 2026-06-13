---
entity_id: "gene.b0752"
entity_type: "gene"
name: "zitB"
source_database: "NCBI RefSeq"
source_id: "gene-b0752"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0752"
  - "zitB"
---

# zitB

`gene.b0752`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0752`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zitB (gene.b0752) is a gene entity. It encodes zitB (protein.P75757). Encoded protein function: FUNCTION: Involved in zinc efflux across the cytoplasmic membrane, thus reducing zinc accumulation in the cytoplasm and rendering bacteria more resistant to zinc. It may contribute to zinc homeostasis at low concentrations of zinc, whereas ZntA is required for growth at more toxic concentrations. EcoCyc product frame: B0752-MONOMER. EcoCyc synonyms: ybgR. Genomic coordinates: 783882-784823. EcoCyc protein note: ZitB (formerly known as YbgR) is a probable Zn2+ transporter. It is a member of the cation diffusion facilitator family of metal ion efflux proteins . Metal ion uptake and solid state NMR studies indicate that ZitB maybe able to transport not only zinc but also cadmium, nickel and copper . Studies have shown that disruption of zntA and zitB results in a greater degree of Zn2+ sensitivity than disruption of zntA alone . Furthermore, overexpression of zitB results in a significant increase in Zn2+ resistance and a decrease in Zn2+ accumulation. Thus, ZitB probably functions as a Zn2+ efflux system possibly playing a role in zinc homeostasis at low Zn2+ levels. Transcription is Zn2+ inducible, based on zitB-lacZ gene fusion studies . zitB is constitutively expressed and plays a role as a first-line defense against excess zinc...

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75757|protein.P75757]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002549,ECOCYC:G6393,GeneID:945348`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:783882-784823:-; feature_type=gene
