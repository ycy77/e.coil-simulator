---
entity_id: "protein.P0AEA2"
entity_type: "protein"
name: "csgG"
source_database: "UniProt"
source_id: "P0AEA2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|PROSITE-ProRule:PRU00303}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csgG b1037 JW1020"
---

# csgG

`protein.P0AEA2`

## Static

- Type: `protein`
- Source: `UniProt:P0AEA2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|PROSITE-ProRule:PRU00303}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}.

## Enriched Summary

FUNCTION: May be involved in the biogenesis of curli organelles. CsgG is an outer membrane lipoprotein which forms the secretion channel for curli subunits. A transposon insertion in csgG abolishes curli production without affecting production of the EG11489-MONOMER "CsgA" curlin subunit . CsgG is a periplasmic facing outer membrane lipoprotein which folds into a protease-resistant conformation . Purified CsgG forms pore containing oligomers; CsgG interacts with G6545-MONOMER "CsgE" and G6544-MONOMER "CsgF" at the outer membrane | (see further ). CsgG clusters into foci in curli-producing cells . CsgG forms a nonameric transmembrane channel in the outer membrane with a large solvent accessible periplasmic cavity; the cavity is open to the periplasm but is constricted to form a pore at the membrane interface; the size of the pore eyelet suggests that curli subunits are secreted in unfolded form; three aromatic residues (Phe63, Tyr66 and Phe71) located at the pore eyelet may have a role in recognising curli subunits (see further ). Overexpression of CsgG increases sensitivity to the hydrophobic antibiotic, erythromycin . Integration and assembly of CsgG into the outer membrane does not require the CPLX0-3933 "Bam" or the CPLX0-7976 "Tam" complex; functional CsgG multimers are present in the outer membrane of a BamA depletion strain

## Biological Role

Component of curli secretion and assembly complex (complex.ecocyc.CPLX-3945).

## Annotation

FUNCTION: May be involved in the biogenesis of curli organelles.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-3945|complex.ecocyc.CPLX-3945]] `EcoCyc` `database` - EcoCyc component coefficient=9 | EcoCyc protcplxs.col coefficient=9 | EcoCyc transporter component coefficient=9

## Incoming Edges (1)

- `encodes` <-- [[gene.b1037|gene.b1037]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEA2`
- `KEGG:ecj:JW1020;eco:b1037;ecoc:C3026_06315;`
- `GeneID:75171163;75203625;945619;`
- `GO:GO:0005886; GO:0009279; GO:0030288; GO:0042802; GO:0044010; GO:0062155; GO:0071806; GO:0098775; GO:0098777`

## Notes

Curli production assembly/transport component CsgG
