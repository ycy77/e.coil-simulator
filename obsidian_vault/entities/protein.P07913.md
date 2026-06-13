---
entity_id: "protein.P07913"
entity_type: "protein"
name: "tdh"
source_database: "UniProt"
source_id: "P07913"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00627}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdh b3616 JW3591"
---

# tdh

`protein.P07913`

## Static

- Type: `protein`
- Source: `UniProt:P07913`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00627}.

## Enriched Summary

FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-threonine to 2-amino-3-ketobutyrate. To a lesser extent, also catalyzes the oxidation of D-allo-threonine and L-threonine amide, but not that of D-threonine and L-allothreonine. Cannot utilize NADP(+) instead of NAD(+). {ECO:0000269|PubMed:6780553}.

## Biological Role

Component of threonine dehydrogenase (complex.ecocyc.THREODEHYD-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-threonine to 2-amino-3-ketobutyrate. To a lesser extent, also catalyzes the oxidation of D-allo-threonine and L-threonine amide, but not that of D-threonine and L-allothreonine. Cannot utilize NADP(+) instead of NAD(+). {ECO:0000269|PubMed:6780553}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.THREODEHYD-CPLX|complex.ecocyc.THREODEHYD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3616|gene.b3616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07913`
- `KEGG:ecj:JW3591;eco:b3616;ecoc:C3026_19605;`
- `GeneID:948139;`
- `GO:GO:0005737; GO:0005829; GO:0006564; GO:0006566; GO:0006567; GO:0008198; GO:0008270; GO:0008743; GO:0016491; GO:0019518; GO:0030145; GO:0046870`
- `EC:1.1.1.103`

## Notes

L-threonine 3-dehydrogenase (TDH) (EC 1.1.1.103) (L-threonine dehydrogenase)
