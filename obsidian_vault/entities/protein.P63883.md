---
entity_id: "protein.P63883"
entity_type: "protein"
name: "amiC"
source_database: "UniProt"
source_id: "P63883"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12787347}. Note=Present throughout the periplasm in non-dividing cells, but localizes almost exclusively to a ring at the site of constriction in dividing cells."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amiC ygdN b2817 JW5449"
---

# amiC

`protein.P63883`

## Static

- Type: `protein`
- Source: `UniProt:P63883`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12787347}. Note=Present throughout the periplasm in non-dividing cells, but localizes almost exclusively to a ring at the site of constriction in dividing cells.

## Enriched Summary

FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}. AmiC is an N-acetylmuramyl-L-alanine amidase, which cleaves the peptide moiety from N-acetylmuramic acid, removing murein crosslinks. AmiC is active toward the murein located at the septum and is therefore important for cell separation upon cell division . NACMURLALAAMI1-MONOMER "AmiA", NACMURLALAAMI2-MONOMER "AmiB" and AmiC appear to have overlapping functions . Murein amidase activity produces stemless or a-denuded-peptidoglycan denuded glycans. AmiC is translocated from the cytoplasm to the periplasm by the twin-arginine transport (Tat) system . During cell division, AmiC specifically localizes to the septal ring; localization is mediated by an N-terminal targeting domain and is dependent on FtsN. In small cells that have not begun dividing, AmiC is located throughout the periplasm . AmiC contains an N-terminal peptidoglycan binding domain and a C-terminal, zinc dependent, catalytic domain. The two domains are linked by a flexible segment . An AmiC mutant which lacks helix α5 in the catalytic domain is constitutively active; an inhibited form of the enzyme is restored by addition of a synthetic peptide mimic...

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

- `encodes` <-- [[gene.b2817|gene.b2817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63883`
- `KEGG:ecj:JW5449;eco:b2817;ecoc:C3026_15470;`
- `GeneID:93779181;947293;`
- `GO:GO:0008745; GO:0009253; GO:0030288; GO:0042597; GO:0043093; GO:0051301; GO:0071555`
- `EC:3.5.1.28`

## Notes

N-acetylmuramoyl-L-alanine amidase AmiC (EC 3.5.1.28)
