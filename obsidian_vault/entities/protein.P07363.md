---
entity_id: "protein.P07363"
entity_type: "protein"
name: "cheA"
source_database: "UniProt"
source_id: "P07363"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cheA b1888 JW1877"
---

# cheA

`protein.P07363`

## Static

- Type: `protein`
- Source: `UniProt:P07363`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. CheA is autophosphorylated; it can transfer its phosphate group to either CheB or CheY. CheA is the histidine protein kinase of two-component signaling pathways (chemotaxis, thermotaxis and energy taxis) which respond to environmental cues and signal change to the flagellar switch complex to regulate swimming behavior. CheA forms ternary signaling complexes with chemoreceptor proteins (CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap") and the coupling protein CHEW-MONOMER "CheW"; ligand binding to the receptor proteins generates a signal that is transmitted across the inner membrane to regulate CheA histidine kinase activity and the subsequent flow of phosphoryl groups to the response regulators CHEY-MONOMER "CheY" - whose phosphorylation status regulates the direction of flagellar motor rotation - and CHEB-MONOMER "CheB" - a protein glutamate methylesterase which modulates the sensory adaption system (see reviews ). CheA also assembles into higher-order complexes with the receptor G7595-MONOMER "Aer" and CheW; Aer reversibly regulates CheA activity based on FAD redox state...

## Biological Role

Component of chemotaxis protein CheA(L) (complex.ecocyc.CHEA-CPLX), CheA(L) - phosphorylated (complex.ecocyc.CPLX0-8274), chemotaxis signaling complex core unit - dipeptide sensing (complex.ecocyc.TAP-CPLX), chemotaxis signaling complex core unit - aspartate sensing (complex.ecocyc.TAR-CPLX), chemotaxis signaling complex core unit - ribose/galactose/glucose sensing (complex.ecocyc.TRG-CPLX), chemotaxis signaling complex core unit - serine sensing (complex.ecocyc.TSR-CPLX), Tapgln (protein.ecocyc.TAP-GLN), Tapglu (protein.ecocyc.TAP-GLU), and 10 more.

## Annotation

FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. CheA is autophosphorylated; it can transfer its phosphate group to either CheB or CheY.

## Outgoing Edges (18)

- `is_component_of` --> [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8274|complex.ecocyc.CPLX0-8274]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TAP-CPLX|complex.ecocyc.TAP-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TAR-CPLX|complex.ecocyc.TAR-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TRG-CPLX|complex.ecocyc.TRG-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TSR-CPLX|complex.ecocyc.TSR-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TAP-GLN|protein.ecocyc.TAP-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TAP-GLU|protein.ecocyc.TAP-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TAP-GLUME|protein.ecocyc.TAP-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TAR-GLN|protein.ecocyc.TAR-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TAR-GLU|protein.ecocyc.TAR-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TAR-GLUME|protein.ecocyc.TAR-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TRG-GLN|protein.ecocyc.TRG-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TRG-GLU|protein.ecocyc.TRG-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TRG-GLUME|protein.ecocyc.TRG-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TSR-GLN|protein.ecocyc.TSR-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TSR-GLU|protein.ecocyc.TSR-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.TSR-GLUME|protein.ecocyc.TSR-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1888|gene.b1888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07363`
- `KEGG:ecj:JW1877;`
- `GeneID:946401;`
- `GO:GO:0000155; GO:0000160; GO:0004673; GO:0005524; GO:0005737; GO:0005829; GO:0005886; GO:0006935; GO:0007165; GO:0009454; GO:0031400; GO:0035556; GO:0043052; GO:0050920; GO:0051649; GO:0071977; GO:0098561; GO:1902021`
- `EC:2.7.13.3`

## Notes

Chemotaxis protein CheA (EC 2.7.13.3)
