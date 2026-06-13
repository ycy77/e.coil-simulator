---
entity_id: "protein.P0A6Q6"
entity_type: "protein"
name: "fabZ"
source_database: "UniProt"
source_id: "P0A6Q6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabZ sefA yaeA b0180 JW0175"
---

# fabZ

`protein.P0A6Q6`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Q6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in unsaturated fatty acids biosynthesis. Catalyzes the dehydration of short chain beta-hydroxyacyl-ACPs and long chain saturated and unsaturated beta-hydroxyacyl-ACPs. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7806516, ECO:0000269|PubMed:8910376}.

## Biological Role

Catalyzes (3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydro-lyase (reaction.R04428), (3R)-3-hydroxydodecanoyl-[acyl-carrier-protein] hydro-lyase (reaction.R04965). Component of 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in unsaturated fatty acids biosynthesis. Catalyzes the dehydration of short chain beta-hydroxyacyl-ACPs and long chain saturated and unsaturated beta-hydroxyacyl-ACPs. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7806516, ECO:0000269|PubMed:8910376}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04428|reaction.R04428]] `KEGG` `database` - via EC:4.2.1.59
- `catalyzes` --> [[reaction.R04965|reaction.R04965]] `KEGG` `database` - via EC:4.2.1.59
- `is_component_of` --> [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0180|gene.b0180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Q6`
- `KEGG:ecj:JW0175;eco:b0180;ecoc:C3026_00825;`
- `GeneID:86862690;93777245;944888;`
- `GO:GO:0005737; GO:0006633; GO:0009245; GO:0016020; GO:0019171; GO:0042802`
- `EC:4.2.1.59`

## Notes

3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase) ((3R)-hydroxymyristoyl-ACP dehydrase) (17 kDa actomyosin component) (Beta-hydroxyacyl-ACP dehydratase)
