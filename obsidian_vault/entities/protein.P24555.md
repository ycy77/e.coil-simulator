---
entity_id: "protein.P24555"
entity_type: "protein"
name: "ptrB"
source_database: "UniProt"
source_id: "P24555"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptrB tlp b1845 JW1834"
---

# ptrB

`protein.P24555`

## Static

- Type: `protein`
- Source: `UniProt:P24555`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Cleaves peptide bonds on the C-terminal side of lysyl and argininyl residues. Oligopeptidase B, originally called protease II, is a serine protease that hydrolyzes peptide bonds following arginines and lysines . The enzyme is very efficient at cleaving after paired basic amino acid residues such as Arg-Arg . Its specificity for artificial peptide substrates has been compared with EG11441-MONOMER and oligopeptidases from other organisms . PtrB is able to degrade and thereby inactivate several short antimicrobial peptides (AMPs) . The enzyme belongs to the prolyl oligopeptidase family of serine peptidases . A noncanonical translation initiation mechanism was discovered for PtrB. The ptrB mRNA begins with an AUG codon at its very 5' end (5'-uAUG). Although translation of the potential 5' ORF is poor, the 5'-uAUG is required for efficent translation of PtrB . The 5'-uAUG functions as a ribosome recognition signal that compensates for the poor Shine-Dalgarno sequence upstream of the ptrB ORF . Overexpression of ptrB from a plasmid confers increased resistance to the proline-rich antimicrobial peptide Bac7(1-16) and certain other AMPs . OpdB: "oligopeptidase B" Reviews:

## Biological Role

Catalyzes 3.4.21.83-RXN (reaction.ecocyc.3.4.21.83-RXN).

## Annotation

FUNCTION: Cleaves peptide bonds on the C-terminal side of lysyl and argininyl residues.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.83-RXN|reaction.ecocyc.3.4.21.83-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1845|gene.b1845]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24555`
- `KEGG:ecj:JW1834;eco:b1845;ecoc:C3026_10510;`
- `GeneID:946358;`
- `GO:GO:0004252; GO:0005737; GO:0006508; GO:0070012`
- `EC:3.4.21.83`

## Notes

Protease 2 (EC 3.4.21.83) (Oligopeptidase B) (Protease II)
