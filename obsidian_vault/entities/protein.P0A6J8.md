---
entity_id: "protein.P0A6J8"
entity_type: "protein"
name: "ddlA"
source_database: "UniProt"
source_id: "P0A6J8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ddlA b0381 JW0372"
---

# ddlA

`protein.P0A6J8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6J8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Cell wall formation. DdlA is one of two D-alanine—D-alanine ligases in E. coli . D-alanine—D-alanine ligase, along with alanine racemase, makes up the D-alanine branch of peptidoglycan biosynthesis. The enzyme combines two molecules of D-alanine to form D-alanyl-D-alanine, which is then added to the growing cell wall precursor. D-alanine—D-alanine ligase is an antibacterial drug target; it was long known to be the target of D-cycloserine . The Keio collection ddlA mutant is 8-fold more sensitive to X-ray radiation than wild type .

## Biological Role

Catalyzes D-alanine:D-alanine ligase (ADP-forming) (reaction.R01150), DALADALALIG-RXN (reaction.ecocyc.DALADALALIG-RXN).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

FUNCTION: Cell wall formation.

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01150|reaction.R01150]] `KEGG` `database` - via EC:6.3.2.4
- `catalyzes` --> [[reaction.ecocyc.DALADALALIG-RXN|reaction.ecocyc.DALADALALIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0381|gene.b0381]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6J8`
- `KEGG:ecj:JW0372;eco:b0381;ecoc:C3026_01840;`
- `GeneID:93777081;945313;`
- `GO:GO:0005524; GO:0005829; GO:0008360; GO:0008716; GO:0009252; GO:0010165; GO:0046872; GO:0071555`
- `EC:6.3.2.4`

## Notes

D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A)
