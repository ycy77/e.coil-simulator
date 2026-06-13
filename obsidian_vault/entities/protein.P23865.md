---
entity_id: "protein.P23865"
entity_type: "protein"
name: "prc"
source_database: "UniProt"
source_id: "P23865"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Periplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prc tsp b1830 JW1819"
---

# prc

`protein.P23865`

## Static

- Type: `protein`
- Source: `UniProt:P23865`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Periplasmic side.

## Enriched Summary

FUNCTION: Involved in the cleavage of a C-terminal peptide of 11 residues from the precursor form of penicillin-binding protein 3 (PBP3). May be involved in protection of the bacterium from thermal and osmotic stresses. Early studies in E. coli K-12 identified various soluble serine proteases, including protease Re , later suggested to be identical with the periplasmic protease known as tail-specific protease (Tsp) encoded by prc (see ). Prc cleaves the C-terminal 11 residue peptide of EG10341-MONOMER "penicillin binding protein 3" to generate the mature protein . Prc binds to and degrades proteins that have been tagged with the quality control peptide sequence coded for by EG30100 "ssrA", indicative of a role in removing improperly translated proteins . Prc together with its adaptor protein CPLX0-8198 "NlpI", forms a proteolytic system that regulates peptidoglycan synthesis by degrading G7147-MONOMER "MepS", a murein endopeptidase that participates in expansion of the peptidoglycan sacculus during bacterial growth and morphogenesis (and further ). NlpI-Prc degrades EG10246-MONOMER . Prc binds NlpI with high affinity . Prc does not cleave soluble, recombinant FtsI in the presence of NlpI . NlpI-Prc mediated proteolysis of peptidoglycan-cleaving enzymes is negatively regulated by the periplasmic protein EG12254-MONOMER BipP in response to reduced DD-endopeptidase activity...

## Biological Role

Catalyzes 3.4.21.102-RXN (reaction.ecocyc.3.4.21.102-RXN).

## Annotation

FUNCTION: Involved in the cleavage of a C-terminal peptide of 11 residues from the precursor form of penicillin-binding protein 3 (PBP3). May be involved in protection of the bacterium from thermal and osmotic stresses.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.102-RXN|reaction.ecocyc.3.4.21.102-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1830|gene.b1830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23865`
- `KEGG:ecj:JW1819;eco:b1830;ecoc:C3026_10430;`
- `GeneID:946096;`
- `GO:GO:0004175; GO:0004252; GO:0005886; GO:0006508; GO:0007165; GO:0030163; GO:0030288; GO:0046677; GO:0141178`
- `EC:3.4.21.102`

## Notes

Tail-specific protease (EC 3.4.21.102) (C-terminal-processing peptidase) (PRC protein) (Protease Re)
