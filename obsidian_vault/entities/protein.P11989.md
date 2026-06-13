---
entity_id: "protein.P11989"
entity_type: "protein"
name: "bglG"
source_database: "UniProt"
source_id: "P11989"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bglG bglC b3723 JW3701"
---

# bglG

`protein.P11989`

## Static

- Type: `protein`
- Source: `UniProt:P11989`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Mediates the positive regulation of the beta-glucoside (bgl) operon by functioning as a transcriptional antiterminator. This is an RNA-binding protein that recognizes a specific sequence located just upstream of two termination sites within the operon.

## Biological Role

Component of transcriptional antiterminator BglG (complex.ecocyc.CPLX0-2861), BglG - his101 phosphorylated (complex.ecocyc.CPLX0-7657), BglG - his208 phosphorylated (complex.ecocyc.CPLX0-8117).

## Annotation

FUNCTION: Mediates the positive regulation of the beta-glucoside (bgl) operon by functioning as a transcriptional antiterminator. This is an RNA-binding protein that recognizes a specific sequence located just upstream of two termination sites within the operon.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2861|complex.ecocyc.CPLX0-2861]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7657|complex.ecocyc.CPLX0-7657]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8117|complex.ecocyc.CPLX0-8117]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3723|gene.b3723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11989`
- `KEGG:ecj:JW3701;eco:b3723;ecoc:C3026_20180;`
- `GeneID:948235;`
- `GO:GO:0003723; GO:0045893`

## Notes

Cryptic beta-glucoside bgl operon antiterminator
