---
entity_id: "protein.P0AGC0"
entity_type: "protein"
name: "uhpT"
source_database: "UniProt"
source_id: "P0AGC0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2156798, ECO:0000269|PubMed:8402899}; Multi-pass membrane protein {ECO:0000255, ECO:0000269|PubMed:2156798}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uhpT b3666 JW3641"
---

# uhpT

`protein.P0AGC0`

## Static

- Type: `protein`
- Source: `UniProt:P0AGC0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2156798, ECO:0000269|PubMed:8402899}; Multi-pass membrane protein {ECO:0000255, ECO:0000269|PubMed:2156798}.

## Enriched Summary

FUNCTION: Mediates the exchange of external hexose 6-phosphate and internal inorganic phosphate. Can transport glucose-6-phosphate, fructose-6-phosphate and mannose-6-phosphate. Also catalyzes the neutral exchange of internal and external phosphate. {ECO:0000269|PubMed:2197272, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:3283129, ECO:0000269|PubMed:3522583, ECO:0000269|PubMed:5330662, ECO:0000269|PubMed:8402899}. UhpT is a hexose phosphate transporter that is a member of the Major Facilitator Superfamily (MFS) . UhpT has been purified and reconstituted into liposomes and demonstrated to transport hexose 6-phosphates via an inorganic phosphate antiport mechanism . The transport system was also shown to catalyze a reversible phosphate: phosphate exchange . Using phosphate-loaded proteoliposomes, and in the absence of any imposed cation motive gradient, hexose 6-phosphate accumulated in the proteoliposomes, and the Km for the transport of 2-deoxy-glucose-6-phosphate via UhpT was determined to be approximately 20 μM . Substrate specificity of UhpT has been studied . Size separation chromatography and reconstitution at low lipid/protein ratios suggest that UhpT has a monomeric functional unit . Hydropathy analysis and PhoA fusions suggest that UhpT has a 12 transmembrane segment topology with the amino and carboxy termini facing the cytoplasm...

## Biological Role

Catalyzes glucose-6-phosphate:phosphate antiport (reaction.ecocyc.TRANS-RXN-33), fructose-6-phosphate:phosphate antiport (reaction.ecocyc.TRANS-RXN0-501), mannose-6-phosphate:phosphate antiport (reaction.ecocyc.TRANS-RXN0-502), glyceraldehyde-3-phosphate:phosphate antiport (reaction.ecocyc.TRANS-RXN0-534). Transports D-Fructose 6-phosphate (molecule.C00085), D-Glucose 6-phosphate (molecule.C00092), D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979), L-glyceraldehyde 3-phosphate (molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Mediates the exchange of external hexose 6-phosphate and internal inorganic phosphate. Can transport glucose-6-phosphate, fructose-6-phosphate and mannose-6-phosphate. Also catalyzes the neutral exchange of internal and external phosphate. {ECO:0000269|PubMed:2197272, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:3283129, ECO:0000269|PubMed:3522583, ECO:0000269|PubMed:5330662, ECO:0000269|PubMed:8402899}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-33|reaction.ecocyc.TRANS-RXN-33]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-501|reaction.ecocyc.TRANS-RXN0-501]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-502|reaction.ecocyc.TRANS-RXN0-502]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-534|reaction.ecocyc.TRANS-RXN0-534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00085|molecule.C00085]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3666|gene.b3666]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGC0`
- `KEGG:ecj:JW3641;eco:b3666;ecoc:C3026_19870;`
- `GeneID:93778407;948201;`
- `GO:GO:0005886; GO:0015526; GO:0015712; GO:0015760; GO:0035435; GO:0061513`

## Notes

Hexose-6-phosphate:phosphate antiporter
