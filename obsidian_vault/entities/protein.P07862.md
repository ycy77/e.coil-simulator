---
entity_id: "protein.P07862"
entity_type: "protein"
name: "ddlB"
source_database: "UniProt"
source_id: "P07862"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ddlB ddl b0092 JW0090"
---

# ddlB

`protein.P07862`

## Static

- Type: `protein`
- Source: `UniProt:P07862`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Cell wall formation. DdlB is one of two D-alanine—D-alanine ligases in E. coli . D-alanine—D-alanine ligase, along with alanine racemase, makes up the D-alanine branch of peptidoglycan biosynthesis. The enzyme combines two molecules of D-alanine to form D-alanyl-D-alanine, which is then added to the growing cell wall precursor. DdlB belongs to the ATP grasp superfamily. The enzyme is similar to VanA, a DD-ligase with modified substrate specificity that occurs in vancomycin-resistant enterococci . D-alanine—D-alanine ligase is an antibacterial drug target; it has long known to be the target of D-cycloserine . Structural and functional studues revealed that it is the phosphorylated form of D-cycloserine that inhibits DdlB . Crystal structures of DdlB have been solved, and a reaction mechanism was proposed . Kinetic analysis of mutants in predicted active site residues has allowed confirmation and refinement of the proposed reaction mechanism . The reaction involves rapid formation of an enzyme-bound D-alanyl phosphate intermediate . Several active site mutants have gained ligase functions similar to the VanA enzyme involved in vancomycin resistance of enterococci . Crystal structures of wild type and mutant DdlB in a complex with an inhibitor allowed insights into substrate specificity and reasons for the weaker inhibition of VanA...

## Biological Role

Catalyzes D-alanine:D-alanine ligase (ADP-forming) (reaction.R01150). Component of D-alanine—D-alanine ligase B (complex.ecocyc.DALADALALIGB-CPLX).

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
- `is_component_of` --> [[complex.ecocyc.DALADALALIGB-CPLX|complex.ecocyc.DALADALALIGB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0092|gene.b0092]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07862`
- `KEGG:ecj:JW0090;eco:b0092;ecoc:C3026_00365;`
- `GeneID:93777342;946324;`
- `GO:GO:0005524; GO:0005829; GO:0008360; GO:0008716; GO:0009252; GO:0042803; GO:0046872; GO:0071555`
- `EC:6.3.2.4`

## Notes

D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B)
