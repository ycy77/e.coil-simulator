---
entity_id: "protein.P0AGK1"
entity_type: "protein"
name: "ubiA"
source_database: "UniProt"
source_id: "P0AGK1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01635, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:4552989, ECO:0000269|PubMed:8155731}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01635}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiA cyr b4040 JW4000"
---

# ubiA

`protein.P0AGK1`

## Static

- Type: `protein`
- Source: `UniProt:P0AGK1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01635, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:4552989, ECO:0000269|PubMed:8155731}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01635}.

## Enriched Summary

FUNCTION: Catalyzes the prenylation of para-hydroxybenzoate (PHB) with an all-trans polyprenyl group. Mediates the second step in the final reaction sequence of ubiquinone-8 (UQ-8) biosynthesis, which is the condensation of the polyisoprenoid side chain with PHB, generating the first membrane-bound Q intermediate 3-octaprenyl-4-hydroxybenzoate (PubMed:4552989). Geranyldiphosphate (GPP), all-trans-farnesyldiphosphate (FPP) and all-trans-solanesyldiphosphate (SPP) are also accepted as side chain precursors (PubMed:8155731). {ECO:0000269|PubMed:4552989, ECO:0000269|PubMed:8155731}. 4-Hydroxybenzoate octaprenyltransferase is the second enzyme in the pathway of ubiquinone biosynthesis. It is responsible for the prenylation of 4-hydroxybenzoate using a polyprenyldiphosphate as a side chain precursor. While E. coli produces an octapreny diphosphatel natively, UbiA is not specific to that compound and can accept polyprenyl diphosphates of different lengths . UbiA is an inner membrane protein with seven predicted transmembrane domains. The C terminus is located in the periplasm . Earlier work experimentally localized UbiA to the membrane fraction . The structure of the enzyme and its active site have been modelled . In subsequent work a 3D structural model was developed that places UbiA in SCOP family 48 583. The model was experimentally supported by site-directed mutagenesis studies...

## Biological Role

Catalyzes solanesyl-diphosphate:4-hydroxybenzoate nonaprenyltransferase (reaction.R07273), 4OHBENZOATE-OCTAPRENYLTRANSFER-RXN (reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the prenylation of para-hydroxybenzoate (PHB) with an all-trans polyprenyl group. Mediates the second step in the final reaction sequence of ubiquinone-8 (UQ-8) biosynthesis, which is the condensation of the polyisoprenoid side chain with PHB, generating the first membrane-bound Q intermediate 3-octaprenyl-4-hydroxybenzoate (PubMed:4552989). Geranyldiphosphate (GPP), all-trans-farnesyldiphosphate (FPP) and all-trans-solanesyldiphosphate (SPP) are also accepted as side chain precursors (PubMed:8155731). {ECO:0000269|PubMed:4552989, ECO:0000269|PubMed:8155731}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07273|reaction.R07273]] `KEGG` `database` - via EC:2.5.1.39
- `catalyzes` --> [[reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN|reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4040|gene.b4040]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGK1`
- `KEGG:ecj:JW4000;eco:b4040;ecoc:C3026_21835;`
- `GeneID:93777791;948540;`
- `GO:GO:0005886; GO:0006744; GO:0008412; GO:0016765`
- `EC:2.5.1.39`

## Notes

4-hydroxybenzoate octaprenyltransferase (EC 2.5.1.39) (4-HB polyprenyltransferase) (PHB octaprenyl transferase)
