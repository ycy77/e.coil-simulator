---
entity_id: "protein.P39400"
entity_type: "protein"
name: "lgoD"
source_database: "UniProt"
source_id: "P39400"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lgoD yjjN b4358 JW5793"
---

# lgoD

`protein.P39400`

## Static

- Type: `protein`
- Source: `UniProt:P39400`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of L-galactonate to D-tagaturonate. Required for growth on L-galactonate as the sole carbon source. In vitro, can also use L-gulonate. {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:24861318}. LgoD is an L-galactonate oxidoreductase that is required for growth on L-galactonate as the sole carbon source under high-throughput growth conditions with limited aeration . LgoD did not show dehydrogenase activity in a high-throughput screen of purified proteins; however, L-galactonate was not tested as a substrate . LgoD may be the L-galactonate oxidoreductase involved in the degradation of L-galactonate that was described in . Expression of lgoD is increased during growth on L-galactonate compared to growth on L-lactate . UxuR appears to regulate lgoD expression .

## Biological Role

Catalyzes L-galactonate:NAD+ 5-oxidoreductase (reaction.R12146), RXN0-5229 (reaction.ecocyc.RXN0-5229). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of L-galactonate to D-tagaturonate. Required for growth on L-galactonate as the sole carbon source. In vitro, can also use L-gulonate. {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:24861318}.

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R12146|reaction.R12146]] `KEGG` `database` - via EC:1.1.1.414
- `catalyzes` --> [[reaction.ecocyc.RXN0-5229|reaction.ecocyc.RXN0-5229]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4358|gene.b4358]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39400`
- `KEGG:ecj:JW5793;eco:b4358;ecoc:C3026_23545;`
- `GeneID:93777490;948883;`
- `GO:GO:0005829; GO:0006566; GO:0008270; GO:0008743; GO:0016616; GO:0034195`
- `EC:1.1.1.414`

## Notes

L-galactonate-5-dehydrogenase (EC 1.1.1.414)
