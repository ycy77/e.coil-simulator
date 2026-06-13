---
entity_id: "protein.P75757"
entity_type: "protein"
name: "zitB"
source_database: "UniProt"
source_id: "P75757"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zitB ybgR b0752 JW0735"
---

# zitB

`protein.P75757`

## Static

- Type: `protein`
- Source: `UniProt:P75757`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in zinc efflux across the cytoplasmic membrane, thus reducing zinc accumulation in the cytoplasm and rendering bacteria more resistant to zinc. It may contribute to zinc homeostasis at low concentrations of zinc, whereas ZntA is required for growth at more toxic concentrations. ZitB (formerly known as YbgR) is a probable Zn2+ transporter. It is a member of the cation diffusion facilitator family of metal ion efflux proteins . Metal ion uptake and solid state NMR studies indicate that ZitB maybe able to transport not only zinc but also cadmium, nickel and copper . Studies have shown that disruption of zntA and zitB results in a greater degree of Zn2+ sensitivity than disruption of zntA alone . Furthermore, overexpression of zitB results in a significant increase in Zn2+ resistance and a decrease in Zn2+ accumulation. Thus, ZitB probably functions as a Zn2+ efflux system possibly playing a role in zinc homeostasis at low Zn2+ levels. Transcription is Zn2+ inducible, based on zitB-lacZ gene fusion studies . zitB is constitutively expressed and plays a role as a first-line defense against excess zinc . Membrane topology predictions using experimentally determined C terminus locations indicate that ZitB has 6 transmembrane helices and the C-terminus is located in the cytoplasm .

## Biological Role

Catalyzes Zn2+:proton antiport (reaction.ecocyc.TRANS-RXN0-200).

## Annotation

FUNCTION: Involved in zinc efflux across the cytoplasmic membrane, thus reducing zinc accumulation in the cytoplasm and rendering bacteria more resistant to zinc. It may contribute to zinc homeostasis at low concentrations of zinc, whereas ZntA is required for growth at more toxic concentrations.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-200|reaction.ecocyc.TRANS-RXN0-200]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0752|gene.b0752]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75757`
- `KEGG:ecj:JW0735;eco:b0752;ecoc:C3026_03800;`
- `GeneID:75204867;945348;`
- `GO:GO:0005385; GO:0005886; GO:0006829; GO:0071577`

## Notes

Zinc transporter ZitB
