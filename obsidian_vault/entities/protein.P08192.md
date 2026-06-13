---
entity_id: "protein.P08192"
entity_type: "protein"
name: "folC"
source_database: "UniProt"
source_id: "P08192"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folC dedC b2315 JW2312"
---

# folC

`protein.P08192`

## Static

- Type: `protein`
- Source: `UniProt:P08192`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Functions in two distinct reactions of the de novo folate biosynthetic pathway. Catalyzes the addition of a glutamate residue to dihydropteroate (7,8-dihydropteroate or H2Pte) to form dihydrofolate (7,8-dihydrofolate monoglutamate or H2Pte-Glu). Also catalyzes successive additions of L-glutamate to tetrahydrofolate or 10-formyltetrahydrofolate or 5,10-methylenetetrahydrofolate, leading to folylpolyglutamate derivatives. {ECO:0000269|PubMed:18232714, ECO:0000269|PubMed:1989505, ECO:0000269|PubMed:2985605}. During de novo tetrahydrofolate biosynthesis, dihydrofolate synthetase encoded by folC catalyzes the addition of the glutamyl residue to dihydropteroate (7,8-dihydropteroate) to form dihydrofolate (7,8-dihydrofolate monoglutamate) in an ATP-dependent reaction (see pathway PWY-6614). In E. coli FolC is a bifunctional enzyme that also catalyzes the subsequent additions of L-glutamate to tetrahydrofolate (folylpoly-γ-glutamate synthetase activity). This latter activity can also utilize the 10-formyl and methylene derivatives of tetrahydrofolate as substrate (see pathway PWY-2161). The folC gene has been shown to be essential in E. coli because this organism lacks specific folate transporters . Recombinant FolC has been overexpressed as a soluble protein, purified and characterized . The enzyme is a member of the Mur synthetase superfamily...

## Biological Role

Catalyzes DIHYDROFOLATESYNTH-RXN (reaction.ecocyc.DIHYDROFOLATESYNTH-RXN), FOLYLPOLYGLUTAMATESYNTH-RXN (reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN), FORMYLTHFGLUSYNTH-RXN (reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN), RXN0-2921 (reaction.ecocyc.RXN0-2921). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Functions in two distinct reactions of the de novo folate biosynthetic pathway. Catalyzes the addition of a glutamate residue to dihydropteroate (7,8-dihydropteroate or H2Pte) to form dihydrofolate (7,8-dihydrofolate monoglutamate or H2Pte-Glu). Also catalyzes successive additions of L-glutamate to tetrahydrofolate or 10-formyltetrahydrofolate or 5,10-methylenetetrahydrofolate, leading to folylpolyglutamate derivatives. {ECO:0000269|PubMed:18232714, ECO:0000269|PubMed:1989505, ECO:0000269|PubMed:2985605}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROFOLATESYNTH-RXN|reaction.ecocyc.DIHYDROFOLATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN|reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN|reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2921|reaction.ecocyc.RXN0-2921]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2315|gene.b2315]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08192`
- `KEGG:ecj:JW2312;eco:b2315;ecoc:C3026_12905;`
- `GeneID:945451;`
- `GO:GO:0004326; GO:0005524; GO:0005737; GO:0006730; GO:0006761; GO:0008841; GO:0009257; GO:0009396; GO:0046656; GO:0046872; GO:0046901; GO:0097216`
- `EC:6.3.2.12; 6.3.2.17`

## Notes

Dihydrofolate synthase/folylpolyglutamate synthase (DHFS / FPGS) (EC 6.3.2.12) (EC 6.3.2.17) (Folylpoly-gamma-glutamate synthetase-dihydrofolate synthetase) (Folylpolyglutamate synthetase) (Tetrahydrofolylpolyglutamate synthase)
