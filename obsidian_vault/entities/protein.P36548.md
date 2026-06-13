---
entity_id: "protein.P36548"
entity_type: "protein"
name: "amiA"
source_database: "UniProt"
source_id: "P36548"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12787347}. Note=Distributed throughout the periplasm in all cells."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amiA yfeE b2435 JW2428"
---

# amiA

`protein.P36548`

## Static

- Type: `protein`
- Source: `UniProt:P36548`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12787347}. Note=Distributed throughout the periplasm in all cells.

## Enriched Summary

FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}. amiA encodes a protein with N-acetylmuramoyl-L-alanine amidase activity. AmiA cleaves the N-acetylmuramoyl → L-alanine bond present in bacterial peptidoglycan; when incubated with isolated murein sacculi, AmiA action results in the appearance of Ala-Glu-A2pm-Ala tetrapeptide and Ala-Glu-A2pm tripeptide . Murein amidase activity produces stemless or a-denuded-peptidoglycan denuded glycans. AmiA is a zinc dependent enzyme . AmiA requires at least a tetrasaccharide as substrate; AmiA does not cleave the peptide from C6 "lipid II" amiA deletion mutants show increased chaining (5-10% chains, 3-4 cells per chain). AmiA, along with NACMURLALAAMI2-MONOMER "AmiB" and G7458-MONOMER "AmiC" plays a role in septum cleavage during cell division; a triple amiA amiB amiC deletion mutant shows 90-100% chains with up to 24 cells per chain; septa in the triple mutant are formed but not cleaved. AmiA, B, and C are not essential for cell enlargement but they are involved in antibiotic induced cell lysis . The murein amidases are necessary for the continued incorporation of peptidoglycan into the developing septum...

## Biological Role

Catalyzes N-acetylmuramoyl-Ala amidohydrolase (reaction.R04112), RXN-16938 (reaction.ecocyc.RXN-16938).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04112|reaction.R04112]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` --> [[reaction.ecocyc.RXN-16938|reaction.ecocyc.RXN-16938]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2435|gene.b2435]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36548`
- `KEGG:ecj:JW2428;eco:b2435;ecoc:C3026_13525;`
- `GeneID:946916;`
- `GO:GO:0008270; GO:0008745; GO:0009253; GO:0030288; GO:0042597; GO:0043093; GO:0051301; GO:0071236; GO:0071555`
- `EC:3.5.1.28`

## Notes

N-acetylmuramoyl-L-alanine amidase AmiA (EC 3.5.1.28)
