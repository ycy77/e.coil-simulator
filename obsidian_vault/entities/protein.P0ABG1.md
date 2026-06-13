---
entity_id: "protein.P0ABG1"
entity_type: "protein"
name: "cdsA"
source_database: "UniProt"
source_id: "P0ABG1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cdsA cds b0175 JW5810"
---

# cdsA

`protein.P0ABG1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABG1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Transferase that catalyzes the synthesis of a CDP-diacylglycerol (CDP-DAG), the activated form of a phosphatidate (PubMed:2995359, PubMed:30936205). It is essential for phospholipid biosynthesis (PubMed:2995359). It is also involved in the biosynthesis of MPIase, a glycolipid essential for membrane protein integration and cell growth (PubMed:30718729, PubMed:30739787). It displays a preference for phosphatidic acids bearing at least one double bond in their fatty acyl moieties (PubMed:2995359). It can use CTP and dCTP, but not ATP, UTP, dATP, dTTP and dGTP (PubMed:2995359). The reaction is reversible in vitro (PubMed:2995359). {ECO:0000269|PubMed:2995359, ECO:0000269|PubMed:30718729, ECO:0000269|PubMed:30739787, ECO:0000269|PubMed:30936205}. CDP-diglyceride synthetase catalyzes the synthesis of CDPDIACYLGLYCEROL, the activated form of L-PHOSPHATIDATE (phosphatidic acid). CDPDIACYLGLYCEROL "CDP-diacylglycerol" is positioned at a branchpoint in the lipid biosynthetic pathway where it reacts with GLYCEROL-3P to form L-1-PHOSPHATIDYL-GLYCEROL-P, or with SER to form L-1-PHOSPHATIDYL-SERINE. It is the source of the phosphatidyl group for all of the major phospholipids in E. coli . The properties of both the partially purified and purified enzyme have been studied. Mutants in cdsA contain significantly elevated levels of L-PHOSPHATIDATE (phosphatidic acid) in vivo...

## Biological Role

Catalyzes CDPDIGLYSYN-RXN (reaction.ecocyc.CDPDIGLYSYN-RXN), RXN0-5515 (reaction.ecocyc.RXN0-5515). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Transferase that catalyzes the synthesis of a CDP-diacylglycerol (CDP-DAG), the activated form of a phosphatidate (PubMed:2995359, PubMed:30936205). It is essential for phospholipid biosynthesis (PubMed:2995359). It is also involved in the biosynthesis of MPIase, a glycolipid essential for membrane protein integration and cell growth (PubMed:30718729, PubMed:30739787). It displays a preference for phosphatidic acids bearing at least one double bond in their fatty acyl moieties (PubMed:2995359). It can use CTP and dCTP, but not ATP, UTP, dATP, dTTP and dGTP (PubMed:2995359). The reaction is reversible in vitro (PubMed:2995359). {ECO:0000269|PubMed:2995359, ECO:0000269|PubMed:30718729, ECO:0000269|PubMed:30739787, ECO:0000269|PubMed:30936205}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CDPDIGLYSYN-RXN|reaction.ecocyc.CDPDIGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5515|reaction.ecocyc.RXN0-5515]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0175|gene.b0175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABG1`
- `KEGG:ecj:JW5810;eco:b0175;ecoc:C3026_00800;`
- `GeneID:93777250;944876;`
- `GO:GO:0004605; GO:0005886; GO:0016024`
- `EC:2.7.7.41`

## Notes

Phosphatidate cytidylyltransferase (EC 2.7.7.41) (CDP-diacylglycerol synthase) (CDP-DAG synthase) (CDP-DG synthase) (CDS) (CDP-diglyceride pyrophosphorylase) (CDP-diglyceride synthase) (CDP-diglyceride synthetase) (CTP:phosphatidate cytidylyltransferase)
