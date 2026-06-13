---
entity_id: "protein.P54746"
entity_type: "protein"
name: "mngB"
source_database: "UniProt"
source_id: "P54746"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mngB ybgG b0732 JW0721"
---

# mngB

`protein.P54746`

## Static

- Type: `protein`
- Source: `UniProt:P54746`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May hydrolyze 6-phospho-mannosyl-D-glycerate to mannose-6-phosphate and glycerate. {ECO:0000269|PubMed:14645248}. MngB is an α-mannosidase that appears to be responsible for the conversion of 2-O-(6-phospho-α-mannosyl)-D-glycerate (MG-P) to mannose-6-phosphate and glycerate in the PWY0-1300 pathway . The enzyme has not yet been purified and assayed in vitro. Expression of mngAB is repressed by MngR and induced when cells are grown in 2-O-α-mannosyl-D-glycerate (MG). mngB mutants are unable to grow in medium containing high levels of MG (without secondary mutations in mngA), likely due to the toxicity of accumulating MG-P within the cells . MngB: "mannosylglycerate catabolism B"

## Biological Role

Catalyzes RXN0-5216 (reaction.ecocyc.RXN0-5216).

## Annotation

FUNCTION: May hydrolyze 6-phospho-mannosyl-D-glycerate to mannose-6-phosphate and glycerate. {ECO:0000269|PubMed:14645248}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5216|reaction.ecocyc.RXN0-5216]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0732|gene.b0732]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P54746`
- `KEGG:ecj:JW0721;eco:b0732;ecoc:C3026_03665;`
- `GeneID:945359;`
- `GO:GO:0004559; GO:0006013; GO:0009313; GO:0030246; GO:0046872`
- `EC:3.2.1.-`

## Notes

Mannosylglycerate hydrolase (EC 3.2.1.-) (2-O-(6-phospho-mannosyl)-D-glycerate hydrolase) (Alpha-mannosidase mngB)
