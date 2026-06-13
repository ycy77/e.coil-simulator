---
entity_id: "protein.P0ACA7"
entity_type: "protein"
name: "gstB"
source_database: "UniProt"
source_id: "P0ACA7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gstB yliJ b0838 JW0822"
---

# gstB

`protein.P0ACA7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACA7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles. Catalyzes the glutathione-dependent dehalogenation of bromoacetate. {ECO:0000269|PubMed:20921376}. The GstB protein is a glutathione S-transferase that is able to dehalogenate the non-natural toxic chemicals bromoacetate and iodoacetate. GstB does not catalyze the dehalogenation of chloroacetate, bromoacetamide, 2-bromopropionate or 3-bromopropionate. Its physiological substrate may be a small molecule containing a carboxylate moiety . Arsenate resistance conferred by GstB is not dependent on glutaredoxins or on the C134/C137 residues within GstB, but requires two arginine residues, R111 and R119 within its substrate binding domain. The proposed mechanism for the glutathione-dependent reduction of arsenate by GstB includes enzymatic formation of an arsenate-glutathione intermediate, which is subsequently reduced by a second glutathione molecule in solution . A gstB mutant is hypersensitive to bromoacetate. Overexpression of gstB does not result in resistance to bromoacetate; instead, it decreases its minimum inhibitory concentration . Overexpression of gstB complements the arsenate sensitivity of a ΔarsC mutant . An R111Q/R119Q mutant has lost the ability to confer arsenate resistance and lost bromoacetate dehalogenase activity...

## Biological Role

Catalyzes RXN0-6549 (reaction.ecocyc.RXN0-6549).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles. Catalyzes the glutathione-dependent dehalogenation of bromoacetate. {ECO:0000269|PubMed:20921376}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6549|reaction.ecocyc.RXN0-6549]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0838|gene.b0838]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACA7`
- `KEGG:ecj:JW0822;eco:b0838;ecoc:C3026_05245;`
- `GeneID:75170907;75204697;945469;`
- `GO:GO:0004364; GO:0005737; GO:0005829; GO:0030611; GO:0042802; GO:0043295`
- `EC:2.5.1.18`

## Notes

Glutathione S-transferase GstB (EC 2.5.1.18)
