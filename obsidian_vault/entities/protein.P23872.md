---
entity_id: "protein.P23872"
entity_type: "protein"
name: "aes"
source_database: "UniProt"
source_id: "P23872"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9576853}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aes ybaC b0476 JW0465"
---

# aes

`protein.P23872`

## Static

- Type: `protein`
- Source: `UniProt:P23872`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9576853}.

## Enriched Summary

FUNCTION: Displays esterase activity towards short chain fatty esters (acyl chain length of up to 8 carbons). Able to hydrolyze triacetylglycerol (triacetin) and tributyrylglycerol (tributyrin), but not trioleylglycerol (triolein) or cholesterol oleate. Negatively regulates MalT activity by antagonizing maltotriose binding. Inhibits MelA galactosidase activity. {ECO:0000269|PubMed:11867639, ECO:0000269|PubMed:12374803, ECO:0000269|PubMed:9576853}.

## Biological Role

Component of acetylesterase (complex.ecocyc.CPLX0-8033).

## Annotation

FUNCTION: Displays esterase activity towards short chain fatty esters (acyl chain length of up to 8 carbons). Able to hydrolyze triacetylglycerol (triacetin) and tributyrylglycerol (tributyrin), but not trioleylglycerol (triolein) or cholesterol oleate. Negatively regulates MalT activity by antagonizing maltotriose binding. Inhibits MelA galactosidase activity. {ECO:0000269|PubMed:11867639, ECO:0000269|PubMed:12374803, ECO:0000269|PubMed:9576853}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8033|complex.ecocyc.CPLX0-8033]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0476|gene.b0476]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23872`
- `KEGG:ecj:JW0465;eco:b0476;ecoc:C3026_02340;`
- `GeneID:947514;`
- `GO:GO:0005737; GO:0008126; GO:0016787; GO:0034338; GO:0042803`
- `EC:3.1.1.-`

## Notes

Acetyl esterase (EC 3.1.1.-) (EcE)
