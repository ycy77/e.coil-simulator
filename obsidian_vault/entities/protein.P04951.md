---
entity_id: "protein.P04951"
entity_type: "protein"
name: "kdsB"
source_database: "UniProt"
source_id: "P04951"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00057}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdsB b0918 JW0901"
---

# kdsB

`protein.P04951`

## Static

- Type: `protein`
- Source: `UniProt:P04951`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00057}.

## Enriched Summary

FUNCTION: Activates KDO (a required 8-carbon sugar) for incorporation into bacterial lipopolysaccharide in Gram-negative bacteria. {ECO:0000255|HAMAP-Rule:MF_00057}. CMP-KDO synthetase activates the 8-carbon sugar KDO for incorporation into lipopolysaccharide. The β-pyranose form of KDO is the preferred substrate of CMP-KDO synthetase . A nucleophilic displacement mechanism was proposed for the enzyme . Based on kinetic, modelling and EPR studies and the crystal structure of the ternary complex, a reaction mechanism involving two Mg2+ ions was proposed . A crystal structure of the enzyme has been solved at 2.6 Å resolution ; the structure of the ternary complex of KdsB with CTP and 2β-deoxy KDO was solved at 1.9 Å resolution . Expression of kdsB is growth regulated: it is highest in early log phase and decreases in stationary phase . kdsB is an essential gene .

## Biological Role

Catalyzes CPM-KDOSYNTH-RXN (reaction.ecocyc.CPM-KDOSYNTH-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Activates KDO (a required 8-carbon sugar) for incorporation into bacterial lipopolysaccharide in Gram-negative bacteria. {ECO:0000255|HAMAP-Rule:MF_00057}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CPM-KDOSYNTH-RXN|reaction.ecocyc.CPM-KDOSYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0918|gene.b0918]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04951`
- `KEGG:ecj:JW0901;eco:b0918;ecoc:C3026_05650;`
- `GeneID:945539;`
- `GO:GO:0000287; GO:0005829; GO:0008690; GO:0019294; GO:0033468`
- `EC:2.7.7.38`

## Notes

3-deoxy-manno-octulosonate cytidylyltransferase (EC 2.7.7.38) (CMP-2-keto-3-deoxyoctulosonic acid synthase) (CKS) (CMP-KDO synthase)
