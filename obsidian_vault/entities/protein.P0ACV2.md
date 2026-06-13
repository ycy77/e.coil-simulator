---
entity_id: "protein.P0ACV2"
entity_type: "protein"
name: "lpxP"
source_database: "UniProt"
source_id: "P0ACV2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01943, ECO:0000305}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01943}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxP ddg b2378 JW2375"
---

# lpxP

`protein.P0ACV2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACV2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01943, ECO:0000305}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01943}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of palmitoleate from palmitoleoyl-[acyl-carrier-protein] (ACP) to Kdo(2)-lipid IV(A) to form Kdo(2)-(palmitoleoyl)-lipid IV(A). Required for the biosynthesis of a distinct molecular species of lipid A, which is present only in cells grown at low temperatures. It may confer a selective advantage to cells growing at lower temperatures by making the outer membrane a more effective barrier to harmful chemicals. {ECO:0000269|PubMed:10092655, ECO:0000269|PubMed:11830594}. In wild-type E. coli grown at 12°C, two-thirds of the lipid A molecules contain palmitoleate instead of laurate . Palmitoleoyl acyltransferase (LpxP) is the sole enzyme that catalyzes the incorporation of palmitoleate into lipid A in E. coli . lpxP expression is induced by cold shock . An lpxP mutant does not exhibit an obvious growth defect even when grown at 12°C; however, the mutant is hypersensitive to certain antibiotics at low temperatures . A triple lpxL lpxM lpxP mutant lacking all secondary acyl chains of lipid A grows slowly in minimal medium, but is not viable at temperatures above 32°C in rich medium . Overexpression of msbA suppresses the growth defect of the triple mutant under fast-growing conditions . Reviews:

## Biological Role

Catalyzes (9Z)-hexadec-9-enoyl-[acyl-carrier protein]:KDO2-lipid IVA O-palmitoleoyltransferase (reaction.R10906), PALMITOTRANS-RXN (reaction.ecocyc.PALMITOTRANS-RXN).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of palmitoleate from palmitoleoyl-[acyl-carrier-protein] (ACP) to Kdo(2)-lipid IV(A) to form Kdo(2)-(palmitoleoyl)-lipid IV(A). Required for the biosynthesis of a distinct molecular species of lipid A, which is present only in cells grown at low temperatures. It may confer a selective advantage to cells growing at lower temperatures by making the outer membrane a more effective barrier to harmful chemicals. {ECO:0000269|PubMed:10092655, ECO:0000269|PubMed:11830594}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R10906|reaction.R10906]] `KEGG` `database` - via EC:2.3.1.242
- `catalyzes` --> [[reaction.ecocyc.PALMITOTRANS-RXN|reaction.ecocyc.PALMITOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2378|gene.b2378]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACV2`
- `KEGG:ecj:JW2375;eco:b2378;ecoc:C3026_13225;`
- `GeneID:75202553;946847;`
- `GO:GO:0005886; GO:0008951; GO:0009103; GO:0009245; GO:0009409; GO:0016020; GO:0016746; GO:0036104`
- `EC:2.3.1.242`

## Notes

Lipid A biosynthesis palmitoleoyltransferase (EC 2.3.1.242) (Kdo(2)-lipid IV(A) palmitoleoyltransferase)
