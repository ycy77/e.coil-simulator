---
entity_id: "protein.P77748"
entity_type: "protein"
name: "ydiJ"
source_database: "UniProt"
source_id: "P77748"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydiJ b1687 JW1677"
---

# ydiJ

`protein.P77748`

## Static

- Type: `protein`
- Source: `UniProt:P77748`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of D-2-hydroxyglutarate (D-2-HGA) to 2-oxoglutarate. Appears to be the only D2HGDH in E.coli, providing the way to recycle D-2-HGA produced during L-serine synthesis by SerA, by converting it back to 2-oxoglutarate. The physiological molecule that functions as the primary electron acceptor during D-2-HGA oxidation by YdiJ in E.coli is unknown. Shows strict substrate specificity towards D-2-HGA, since it has no detectable activity on L-2-hydroxyglutarate, L-malate, D-malate, L-lactate, D-lactate, L-tartrate, D-tartrate, L-glycerate, D-glycerate, glutarate, or pyruvate. {ECO:0000269|PubMed:36144368}.

## Biological Role

Component of D-2-hydroxyglutarate dehydrogenase (complex.ecocyc.CPLX0-9749).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of D-2-hydroxyglutarate (D-2-HGA) to 2-oxoglutarate. Appears to be the only D2HGDH in E.coli, providing the way to recycle D-2-HGA produced during L-serine synthesis by SerA, by converting it back to 2-oxoglutarate. The physiological molecule that functions as the primary electron acceptor during D-2-HGA oxidation by YdiJ in E.coli is unknown. Shows strict substrate specificity towards D-2-HGA, since it has no detectable activity on L-2-hydroxyglutarate, L-malate, D-malate, L-lactate, D-lactate, L-tartrate, D-tartrate, L-glycerate, D-glycerate, glutarate, or pyruvate. {ECO:0000269|PubMed:36144368}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9749|complex.ecocyc.CPLX0-9749]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1687|gene.b1687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77748`
- `KEGG:ecj:JW1677;eco:b1687;ecoc:C3026_09660;`
- `GeneID:946189;`
- `GO:GO:0004458; GO:0008720; GO:0046872; GO:0050660; GO:0051539; GO:0051990; GO:0071949; GO:1903457`
- `EC:1.1.99.39`

## Notes

D-2-hydroxyglutarate dehydrogenase (D2HGDH) (EC 1.1.99.39)
