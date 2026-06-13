---
entity_id: "protein.P75920"
entity_type: "protein"
name: "mdoC"
source_database: "UniProt"
source_id: "P75920"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdoC opgC ymdD b1047 JW1034"
---

# mdoC

`protein.P75920`

## Static

- Type: `protein`
- Source: `UniProt:P75920`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Necessary for the succinyl substitution of periplasmic glucans. Could catalyze the transfer of succinyl residues from the cytoplasmic side of the membrane to the nascent glucan backbones on the periplasmic side of the membrane. OpgC is required for wild-type succinyl modification of the branched periplasmic oligosaccharides known as CPD-16398 osmoregulated periplasmic glucans (OPG), formerly called membrane-derived oligosaccharides (MDO). The origin of the succinyl group is not known but is suggested to be SUC-COA (see ). OPGs extracted from opgC- cells (strain NFB1864 mdoB214::Tn10 mdoC1::Tn5) are devoid of succinyl residues . Succinylation of OPGs is not osmodependent . OpgC is predicted to be an innner membrane protein with 10 transmembrane domains . In the Transporter Classification Database OpgC is a member of the Acyltransferase-3/Putative Acetyl-CoA Transporter (ATAT) family.

## Annotation

FUNCTION: Necessary for the succinyl substitution of periplasmic glucans. Could catalyze the transfer of succinyl residues from the cytoplasmic side of the membrane to the nascent glucan backbones on the periplasmic side of the membrane.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1047|gene.b1047]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75920`
- `KEGG:ecj:JW1034;eco:b1047;ecoc:C3026_06370;`
- `GeneID:75203635;946944;`
- `GO:GO:0005886; GO:0016741; GO:0016748; GO:1900727`
- `EC:2.1.-.-`

## Notes

Glucans biosynthesis protein C (EC 2.1.-.-)
