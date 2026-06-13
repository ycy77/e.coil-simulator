---
entity_id: "protein.P00370"
entity_type: "protein"
name: "gdhA"
source_database: "UniProt"
source_id: "P00370"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gdhA b1761 JW1750"
---

# gdhA

`protein.P00370`

## Static

- Type: `protein`
- Source: `UniProt:P00370`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible oxidative deamination of glutamate to alpha-ketoglutarate and ammonia. {ECO:0000269|PubMed:235298, ECO:0000269|PubMed:241744}.

## Biological Role

Catalyzes alpha-amino acid:NAD+ oxidoreductase (deaminating) (reaction.R00145), alpha-amino acid:NADP+ oxidoreductase (deaminating) (reaction.R00146), L-glutamate:NADP+ oxidoreductase (deaminating) (reaction.R00248). Component of glutamate dehydrogenase (complex.ecocyc.GDHA-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible oxidative deamination of glutamate to alpha-ketoglutarate and ammonia. {ECO:0000269|PubMed:235298, ECO:0000269|PubMed:241744}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00145|reaction.R00145]] `KEGG` `database` - via EC:1.4.1.4
- `catalyzes` --> [[reaction.R00146|reaction.R00146]] `KEGG` `database` - via EC:1.4.1.4
- `catalyzes` --> [[reaction.R00248|reaction.R00248]] `KEGG` `database` - via EC:1.4.1.4
- `is_component_of` --> [[complex.ecocyc.GDHA-CPLX|complex.ecocyc.GDHA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1761|gene.b1761]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00370`
- `KEGG:ecj:JW1750;eco:b1761;ecoc:C3026_10050;`
- `GeneID:946802;`
- `GO:GO:0004354; GO:0005737; GO:0005829; GO:0006536; GO:0006537; GO:0042802; GO:0097216; GO:1990148`
- `EC:1.4.1.4`

## Notes

NADP-specific glutamate dehydrogenase (NADP-GDH) (EC 1.4.1.4)
