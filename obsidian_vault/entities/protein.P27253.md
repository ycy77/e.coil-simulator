---
entity_id: "protein.P27253"
entity_type: "protein"
name: "scpA"
source_database: "UniProt"
source_id: "P27253"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "scpA sbm yliK b2917 JW2884"
---

# scpA

`protein.P27253`

## Static

- Type: `protein`
- Source: `UniProt:P27253`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion of succinyl-CoA and methylmalonyl-CoA. Could be part of a pathway that converts succinate to propionate. {ECO:0000269|PubMed:10769117, ECO:0000269|PubMed:11955068}. Methylmalonyl-CoA mutase (MCM) catalyzes the reversible, stereospecific interconversion of methylmalonyl-CoA to succinyl-CoA . The enzyme may participate in a pathway of succinate decarboxylation whose metabolic role is unknown . MCM and the YgfD (ArgK) protein interact both in vivo and in vitro . Sbm: "sleeping beauty mutase"

## Biological Role

Catalyzes (R)-methylmalonyl-CoA CoA-carbonylmutase (reaction.R00833). Component of methylmalonyl-CoA mutase (complex.ecocyc.CPLX0-7741).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of succinyl-CoA and methylmalonyl-CoA. Could be part of a pathway that converts succinate to propionate. {ECO:0000269|PubMed:10769117, ECO:0000269|PubMed:11955068}.

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00833|reaction.R00833]] `KEGG` `database` - via EC:5.4.99.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7741|complex.ecocyc.CPLX0-7741]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2917|gene.b2917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27253`
- `KEGG:ecj:JW2884;eco:b2917;ecoc:C3026_15985;`
- `GeneID:945576;`
- `GO:GO:0004494; GO:0005737; GO:0019678; GO:0031419; GO:0046872`
- `EC:5.4.99.2`

## Notes

Methylmalonyl-CoA mutase (MCM) (EC 5.4.99.2)
