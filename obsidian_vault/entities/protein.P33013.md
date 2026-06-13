---
entity_id: "protein.P33013"
entity_type: "protein"
name: "dacD"
source_database: "UniProt"
source_id: "P33013"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}. Note=N-terminal lies in the periplasmic space. {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dacD phsE yeeC b2010 JW5329"
---

# dacD

`protein.P33013`

## Static

- Type: `protein`
- Source: `UniProt:P33013`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}. Note=N-terminal lies in the periplasmic space. {ECO:0000305}.

## Enriched Summary

FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors. Penicillin-binding protein 6b (PBP6b), the product of the dacD gene, is a penicillin-sensitive, membrane-bound D-alanyl D-alanine carboxypeptidase (DD-carboxypeptidase) which cleaves the carboxy-terminal D-alanine from peptidoglycan pentapeptides . PBP6b DD-carboxypeptidase activity contributes to the maintenance of cell shape at low pH . The predicted amino acid sequence of PBP6b is 47.4% identical to CPLX0-8252 "PBP5" and 47.7% identical to CPLX0-8254 "PBP6" . Increased expression of dacD in a strain that contains dacA and dacC null alleles reduces the amount of pentapeptide muropeptides in peptidoglycan . DacD contains the conserved motif sequences, SxxK (SLTK), [S/Y]xN (SGN) and [K/H][T/S]G (KTG), of the serine acyltransferase superfamily ; DacD binds benzylpenicillin . DacD does not contribute to intrinsic β-lactam resistance in E. coli K-12, however overexpression of dacD partially complements the β-lactam sensitivity of a ΔdacA mutant . Purified, soluble DacD binds Bocillin FL penicillin and has moderate deacylation activity; it also exhibits DD-carboxpeptidase activity with the model substrate diacetyl-Lys-D-Ala-D-Ala and with the the peptidoglycan mimetic pentapeptide substrate, L-Ala-γ-D-Glu-L-Lys-D-Ala-D-Ala...

## Biological Role

Catalyzes BETA-LACTAMASE-RXN (reaction.ecocyc.BETA-LACTAMASE-RXN), RXN-16649 (reaction.ecocyc.RXN-16649), RXN-19249 (reaction.ecocyc.RXN-19249), RXN-19253 (reaction.ecocyc.RXN-19253).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.BETA-LACTAMASE-RXN|reaction.ecocyc.BETA-LACTAMASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19249|reaction.ecocyc.RXN-19249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19253|reaction.ecocyc.RXN-19253]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2010|gene.b2010]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33013`
- `KEGG:ecj:JW5329;eco:b2010;ecoc:C3026_11340;`
- `GeneID:946518;`
- `GO:GO:0000270; GO:0004180; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0008800; GO:0009002; GO:0009252; GO:0071555`
- `EC:3.4.16.4`

## Notes

D-alanyl-D-alanine carboxypeptidase DacD (DD-carboxypeptidase) (DD-peptidase) (EC 3.4.16.4) (Penicillin-binding protein 6b) (PBP-6b)
