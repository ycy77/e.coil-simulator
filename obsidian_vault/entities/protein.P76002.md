---
entity_id: "protein.P76002"
entity_type: "protein"
name: "pliG"
source_database: "UniProt"
source_id: "P76002"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:20734102}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pliG ycgK b1178 JW1167"
---

# pliG

`protein.P76002`

## Static

- Type: `protein`
- Source: `UniProt:P76002`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:20734102}.

## Enriched Summary

FUNCTION: Inhibits activity of g-type lysozyme, which confers increased lysozyme tolerance to the bacterium. {ECO:0000269|PubMed:20734102}. The PliG protein inhibits activity of g-type lysozyme in vitro . pliG deletion mutants show increased sensitivity to g-type lysozyme in the presence of EDTA . PliG contains a conserved bacterial prepeptidase C terminal (PPC) domain . Structural and mutational data has identified a putative lysozyme interaction interface . Targeting of YcgK to the Sec-translocase for transport across the inner membrane is SecB-dependent . pliG: periplasmic lysozme inhibitor of g-type lysozyme . Related review:

## Annotation

FUNCTION: Inhibits activity of g-type lysozyme, which confers increased lysozyme tolerance to the bacterium. {ECO:0000269|PubMed:20734102}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1178|gene.b1178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76002`
- `KEGG:ecj:JW1167;eco:b1178;ecoc:C3026_06940;`
- `GeneID:946963;`
- `GO:GO:0006952; GO:0030288; GO:0060241`

## Notes

Inhibitor of g-type lysozyme
