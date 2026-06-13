---
entity_id: "protein.P0C0U4"
entity_type: "protein"
name: "rimK"
source_database: "UniProt"
source_id: "P0C0U4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rimK b0852 JW0836"
---

# rimK

`protein.P0C0U4`

## Static

- Type: `protein`
- Source: `UniProt:P0C0U4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: An L-glutamate ligase that catalyzes the ATP-dependent post-translational addition of glutamate residues to the C-terminus of ribosomal protein bS6 (RpsF). Is also able to catalyze the synthesis of poly-alpha-glutamate in vitro, via ATP hydrolysis from unprotected glutamate as substrate. The number of glutamate residues added to either RpsF or to poly-alpha-glutamate changes with pH. {ECO:0000255|HAMAP-Rule:MF_01552, ECO:0000269|PubMed:21278279, ECO:0000269|PubMed:2570347}.

## Biological Role

Component of ribosomal protein S6 modification protein (complex.ecocyc.CPLX0-7946).

## Annotation

FUNCTION: An L-glutamate ligase that catalyzes the ATP-dependent post-translational addition of glutamate residues to the C-terminus of ribosomal protein bS6 (RpsF). Is also able to catalyze the synthesis of poly-alpha-glutamate in vitro, via ATP hydrolysis from unprotected glutamate as substrate. The number of glutamate residues added to either RpsF or to poly-alpha-glutamate changes with pH. {ECO:0000255|HAMAP-Rule:MF_01552, ECO:0000269|PubMed:21278279, ECO:0000269|PubMed:2570347}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7946|complex.ecocyc.CPLX0-7946]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0852|gene.b0852]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0U4`
- `KEGG:ecj:JW0836;eco:b0852;ecoc:C3026_05315;`
- `GeneID:93776570;945484;`
- `GO:GO:0005524; GO:0005737; GO:0006412; GO:0009432; GO:0018169; GO:0042802; GO:0046872`
- `EC:6.3.2.-`

## Notes

Ribosomal protein bS6--L-glutamate ligase (EC 6.3.2.-) (Polyglutamate synthase) (Ribosomal protein bS6 modification protein)
