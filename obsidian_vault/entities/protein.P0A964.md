---
entity_id: "protein.P0A964"
entity_type: "protein"
name: "cheW"
source_database: "UniProt"
source_id: "P0A964"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cheW b1887 JW1876"
---

# cheW

`protein.P0A964`

## Static

- Type: `protein`
- Source: `UniProt:P0A964`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. It physically bridges CheA to the MCPs (methyl-accepting chemotaxis proteins) to allow regulated phosphotransfer to CheY and CheB. CheW is the coupling protein in the ternary receptor complexes of two-component signaling pathways (chemotaxis, thermotaxis and energy taxis) which respond to environmental cues (both external and internal) and signal change to the flagellar switch complex to regulate swimming behavior. CheW forms ternary signaling complexes with chemoreceptor proteins (CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap") and the protein histidine kinase CHEA-CPLX "CheA"; ligand binding to the receptor proteins generates a signal that is transmitted across the inner membrane to regulate CheA histidine kinase activity and the subsequent flow of phosphoryl groups to the response regulators CHEY-MONOMER "CheY" - whose phosphorylation status regulates the direction of flagellar motor rotation - and CHEB-MONOMER "CheB" - a protein glutamate methylesterase which modulates the sensory adaption system (see reviews ). CheW also assembles into higher-order complexes with the receptor G7595-MONOMER "Aer" and CheA to mediate the aerotaxis (oxygen-sensing) response . CheW is required for the chemotactic response to PTS sugars (see also )...

## Biological Role

Component of chemotaxis signaling complex core unit - dipeptide sensing (complex.ecocyc.TAP-CPLX), chemotaxis signaling complex core unit - aspartate sensing (complex.ecocyc.TAR-CPLX), chemotaxis signaling complex core unit - ribose/galactose/glucose sensing (complex.ecocyc.TRG-CPLX), chemotaxis signaling complex core unit - serine sensing (complex.ecocyc.TSR-CPLX), Tapgln (protein.ecocyc.TAP-GLN), Tapglu (protein.ecocyc.TAP-GLU), Tapglu-Me (protein.ecocyc.TAP-GLUME), Targln (protein.ecocyc.TAR-GLN), and 8 more.

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. It physically bridges CheA to the MCPs (methyl-accepting chemotaxis proteins) to allow regulated phosphotransfer to CheY and CheB.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (16)

- `is_component_of` --> [[complex.ecocyc.TAP-CPLX|complex.ecocyc.TAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TAR-CPLX|complex.ecocyc.TAR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TRG-CPLX|complex.ecocyc.TRG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TSR-CPLX|complex.ecocyc.TSR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
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

- `encodes` <-- [[gene.b1887|gene.b1887]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A964`
- `KEGG:ecj:JW1876;eco:b1887;ecoc:C3026_10730;`
- `GeneID:93776192;946400;`
- `GO:GO:0005829; GO:0005886; GO:0006935; GO:0007165; GO:0009454; GO:0019904; GO:0035556; GO:0051286; GO:0051649; GO:0098561`

## Notes

Chemotaxis protein CheW
