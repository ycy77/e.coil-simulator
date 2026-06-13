---
entity_id: "protein.P0ADF6"
entity_type: "protein"
name: "edd"
source_database: "UniProt"
source_id: "P0ADF6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "edd b1851 JW1840"
---

# edd

`protein.P0ADF6`

## Static

- Type: `protein`
- Source: `UniProt:P0ADF6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of 6-phospho-D-gluconate to 2-dehydro-3-deoxy-6-phospho-D-gluconate. {ECO:0000255|HAMAP-Rule:MF_02094, ECO:0000269|PubMed:17102132, ECO:0000269|PubMed:1846355}. Phosphogluconate dehydratase catalyzes the dehydration of D-gluconate 6-phosphate to 2-dehydro-3-deoxy-D-gluconate 6-phosphate. This is the first reaction of the ENTNER-DOUDOROFF-PWY " Entner-Doudoroff pathway" which constitutes the primary route of gluconate metabolism in E. coli. Phosphogluconate dehydratase is induced by growth of cells on gluconate . The enzyme is sensitive to oxidants such as superoxide and hydrogen peroxide due to its [4Fe-4S] iron-sulfur cluster content. It is also inactivated by iron chelators and thiol-reactive compounds. Fluoride ions protect the enzyme from the effects of oxidants . Under continuous culture conditions induction of phosphogluconate dehydratase is favored at low oxygen concentrations . Edd from E. coli K-12, a laboratory strain, has not been well characterized biochemically. However, using E. coli strains from the ECOR collection of natural isolates, the Km and Vmax of phosphogluconate dehydratase were determined along with the growth rate in gluconate minimal salts medium...

## Biological Role

Catalyzes PGLUCONDEHYDRAT-RXN (reaction.ecocyc.PGLUCONDEHYDRAT-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of 6-phospho-D-gluconate to 2-dehydro-3-deoxy-6-phospho-D-gluconate. {ECO:0000255|HAMAP-Rule:MF_02094, ECO:0000269|PubMed:17102132, ECO:0000269|PubMed:1846355}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PGLUCONDEHYDRAT-RXN|reaction.ecocyc.PGLUCONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1851|gene.b1851]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADF6`
- `KEGG:ecj:JW1840;eco:b1851;ecoc:C3026_10545;`
- `GeneID:86859389;946362;`
- `GO:GO:0004456; GO:0005829; GO:0009255; GO:0019521; GO:0046872; GO:0051539`
- `EC:4.2.1.12`

## Notes

Phosphogluconate dehydratase (EC 4.2.1.12) (6-phosphogluconate dehydratase) (Entner-Doudoroff dehydrase)
