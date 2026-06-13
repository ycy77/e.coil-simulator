---
entity_id: "protein.P0AEK2"
entity_type: "protein"
name: "fabG"
source_database: "UniProt"
source_id: "P0AEK2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabG b1093 JW1079"
---

# fabG

`protein.P0AEK2`

## Static

- Type: `protein`
- Source: `UniProt:P0AEK2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of beta-ketoacyl-ACP substrates to beta-hydroxyacyl-ACP products, the first reductive step in the elongation cycle of fatty acid biosynthesis. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:14996818, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8631920, ECO:0000269|PubMed:8910376}.

## Biological Role

Catalyzes (3R)-3-hydroxydodecanoyl-[acyl-carrier-protein]:NADP+ oxidoreductase (reaction.R04964), R07763 (reaction.R07763). Component of 3-oxoacyl-[acyl-carrier-protein] reductase FabG (complex.ecocyc.CPLX0-8005).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of beta-ketoacyl-ACP substrates to beta-hydroxyacyl-ACP products, the first reductive step in the elongation cycle of fatty acid biosynthesis. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:14996818, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8631920, ECO:0000269|PubMed:8910376}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04964|reaction.R04964]] `KEGG` `database` - via EC:1.1.1.100
- `catalyzes` --> [[reaction.R07763|reaction.R07763]] `KEGG` `database` - via EC:1.1.1.100
- `is_component_of` --> [[complex.ecocyc.CPLX0-8005|complex.ecocyc.CPLX0-8005]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1093|gene.b1093]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEK2`
- `KEGG:ecj:JW1079;eco:b1093;ecoc:C3026_06610;`
- `GeneID:93776315;945645;`
- `GO:GO:0004316; GO:0005829; GO:0006633; GO:0008610; GO:0009102; GO:0016616; GO:0030497; GO:0042802; GO:0046872; GO:0050661; GO:0051287`
- `EC:1.1.1.100`

## Notes

3-oxoacyl-[acyl-carrier-protein] reductase FabG (EC 1.1.1.100) (3-ketoacyl-acyl carrier protein reductase) (Beta-Ketoacyl-acyl carrier protein reductase) (Beta-ketoacyl-ACP reductase)
