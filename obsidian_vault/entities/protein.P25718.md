---
entity_id: "protein.P25718"
entity_type: "protein"
name: "malS"
source_database: "UniProt"
source_id: "P25718"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malS b3571 JW3543"
---

# malS

`protein.P25718`

## Static

- Type: `protein`
- Source: `UniProt:P25718`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Since only maltooligosaccharides up to a chain length of 6 glucose units are actively transported through the cytoplasmic membrane via the membrane-bound complex of three proteins, MalF, MalG, and MalK, longer maltooligosaccharides must first be degraded by the periplasmic alpha-amylase, the MalS protein. MalS is a periplasmic enzyme that degrades linear Dextrins dextrins of at least three glucose residues. CPD-3781 and CPD-3783 serve as substrates, leading to classification of the enzyme as an α-amylase hydrolyzing internal 1,4-glucosidic linkages . MalS is one of two α-amylases present in E. coli. The second enzyme, ALPHA-AMYL-CYTO-MONOMER "AmyA", is cytoplasmic. MalS is an endo hydrolase that recognizes its substrates from their non-reducing end and preferentially liberates MALTOHEXAOSE , which can then be transported through the cytoplasmic membrane via the ABC-16-CPLX. MalS is thought to provide a growth advantage by degrading periplasmic maltodextrins between 7 and 15 glucose units in length . MalS is a monomer in solution; two intramolecular disulfide bonds have been mapped . A crystal structure was reported at a resolution of 2.7 Å, showing that the enzyme has unique structural features of circularly permutated domains. The N-domain was predicted by AlphaFold2 be a CBM69 (carbohydrate-binding module 69), serving to bind the polysaccharide substrates...

## Biological Role

Catalyzes 1,4-alpha-D-glucan glucanohydrolase (reaction.R02108), 1,4-alpha-D-glucan maltohydrolase (reaction.R02112), RXN0-5181 (reaction.ecocyc.RXN0-5181). Bound by Ca2+ (molecule.ecocyc.CA_2).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Since only maltooligosaccharides up to a chain length of 6 glucose units are actively transported through the cytoplasmic membrane via the membrane-bound complex of three proteins, MalF, MalG, and MalK, longer maltooligosaccharides must first be degraded by the periplasmic alpha-amylase, the MalS protein.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02108|reaction.R02108]] `KEGG` `database` - via EC:3.2.1.1
- `catalyzes` --> [[reaction.R02112|reaction.R02112]] `KEGG` `database` - via EC:3.2.1.1
- `catalyzes` --> [[reaction.ecocyc.RXN0-5181|reaction.ecocyc.RXN0-5181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3571|gene.b3571]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25718`
- `KEGG:ecj:JW3543;eco:b3571;ecoc:C3026_19360;`
- `GeneID:948088;`
- `GO:GO:0004556; GO:0005509; GO:0009313; GO:0030288; GO:0030980; GO:0042597`
- `EC:3.2.1.1`

## Notes

Periplasmic alpha-amylase (EC 3.2.1.1) (1,4-alpha-D-glucan glucanohydrolase)
