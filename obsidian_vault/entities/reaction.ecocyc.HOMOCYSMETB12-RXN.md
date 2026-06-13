---
entity_id: "reaction.ecocyc.HOMOCYSMETB12-RXN"
entity_type: "reaction"
name: "HOMOCYSMETB12-RXN"
source_database: "EcoCyc"
source_id: "HOMOCYSMETB12-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOMOCYSMETB12-RXN

`reaction.ecocyc.HOMOCYSMETB12-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOMOCYSMETB12-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

.During catalysis, an enzyme-bound cobalamine prosthetic group is used as an intermediate methyl donor and acceptor. At different points during the reaction cycle, the coordination to the cobalt of the cobalamine changes. Corodination of the His-759 residue to the cobalt center is necessary for the interconversion betwee the reactivation and catalytic conformations. Zinc is required for catalysis of methyl transfer from methylcobalamin to homocysteine. Mutations of Cys310 or Cys311 to either alanine or serine result in loss of catalytic activity. The equilibria between various conformations of MetH are sensitive to temparature, the presence or absence of ligands including methyl-tetrahydrofolate, and the beta-ligand of the cobalamine prosthetic group . EcoCyc reaction equation: HOMO-CYS + 5-METHYL-THF-GLU-N -> MET + THF-GLU-N; direction=PHYSIOL-LEFT-TO-RIGHT. .During catalysis, an enzyme-bound cobalamine prosthetic group is used as an intermediate methyl donor and acceptor. At different points during the reaction cycle, the coordination to the cobalt of the cobalamine changes. Corodination of the His-759 residue to the cobalt center is necessary for the interconversion betwee the reactivation and catalytic conformations. Zinc is required for catalysis of methyl transfer from methylcobalamin to homocysteine...

## Biological Role

Catalyzed by metH (protein.P13009). Substrates: L-Homocysteine (molecule.C00155), a 5-methyltetrahydrofolate (molecule.ecocyc.5-METHYL-THF-GLU-N). Products: L-Methionine (molecule.C00073), THF-polyglutamate (molecule.C03541).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Annotation

.During catalysis, an enzyme-bound cobalamine prosthetic group is used as an intermediate methyl donor and acceptor. At different points during the reaction cycle, the coordination to the cobalt of the cobalamine changes. Corodination of the His-759 residue to the cobalt center is necessary for the interconversion betwee the reactivation and catalytic conformations. Zinc is required for catalysis of methyl transfer from methylcobalamin to homocysteine. Mutations of Cys310 or Cys311 to either alanine or serine result in loss of catalytic activity. The equilibria between various conformations of MetH are sensitive to temparature, the presence or absence of ligands including methyl-tetrahydrofolate, and the beta-ligand of the cobalamine prosthetic group .

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P13009|protein.P13009]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-METHYL-THF-GLU-N|molecule.ecocyc.5-METHYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00887|molecule.C00887]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HOMOCYSMETB12-RXN`

## Notes

HOMO-CYS + 5-METHYL-THF-GLU-N -> MET + THF-GLU-N; direction=PHYSIOL-LEFT-TO-RIGHT
