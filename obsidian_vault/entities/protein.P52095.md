---
entity_id: "protein.P52095"
entity_type: "protein"
name: "ldcC"
source_database: "UniProt"
source_id: "P52095"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ldcC ldc ldcH b0186 JW0181"
---

# ldcC

`protein.P52095`

## Static

- Type: `protein`
- Source: `UniProt:P52095`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Plays a role in lysine utilization by acting as a lysine decarboxylase. {ECO:0000269|PubMed:9339543}. There are two lysine decarboxylases in E. coli, encoded by the cadA and ldcC genes. The ldcC gene product, lysine decarboxylase 2 (LdcC), differs from the cadA-encoded enzyme in that it is weakly expressed, is more thermosensitive and has activity over a broad range of pH with a higher pH optimum than CadA . A 3D cryo-EM reconstruction of LdcC has been compared to that of CadA; the C-terminal β-sheet provides a sequence signature that allows classification of enzymes into LdcC-like vs. CadA-like and explains why only CadA, but not LdcC, can interact with RavA . ldcC is expressed at very low levels and shows RpoS-dependent induction during stationary phase . The alarmone (p)ppGpp inhibits LdcC activity . Expression of ldcC is downregulated under simulated microgravity conditions . A mutant that is missing all eight genes involved in polyamine biosynthesis, ΔspeABCDEF cadA ldcC, grows aerobically at a reduced rate. However, polyamines are required for growth under anaerobic conditions and at very high oxygen levels . LdcC: "lysine decarboxylase, constitutive" Review:

## Biological Role

Catalyzes L-lysine carboxy-lyase (cadaverine-forming) (reaction.R00462). Component of lysine decarboxylase 2 (complex.ecocyc.LDC2-CPLX).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Plays a role in lysine utilization by acting as a lysine decarboxylase. {ECO:0000269|PubMed:9339543}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00462|reaction.R00462]] `KEGG` `database` - via EC:4.1.1.18
- `is_component_of` --> [[complex.ecocyc.LDC2-CPLX|complex.ecocyc.LDC2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b0186|gene.b0186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52095`
- `KEGG:ecj:JW0181;eco:b0186;ecoc:C3026_00855;`
- `GeneID:944887;`
- `GO:GO:0005737; GO:0006554; GO:0008923; GO:0042802`
- `EC:4.1.1.18`

## Notes

Constitutive lysine decarboxylase (LDCC) (EC 4.1.1.18)
