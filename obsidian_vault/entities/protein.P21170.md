---
entity_id: "protein.P21170"
entity_type: "protein"
name: "speA"
source_database: "UniProt"
source_id: "P21170"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2198270}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speA b2938 JW2905"
---

# speA

`protein.P21170`

## Static

- Type: `protein`
- Source: `UniProt:P21170`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2198270}.

## Enriched Summary

FUNCTION: Catalyzes the biosynthesis of agmatine from arginine. {ECO:0000269|PubMed:19603287, ECO:0000269|PubMed:2198270, ECO:0000269|PubMed:4571773}. Biosynthetic arginine decarboxylase (SpeA) carries out the first step in PWY-40, the decarboxylation of L-arginine to yield agmatine . This enzymatic activity is subject to feedback inhibition by the downstream polyamine products putrescine and spermidine . SpeA is specific to arginine, and can neither decarboxylate nor be inhibited by L-ornithine or L-lysine . The active form of SpeA is a tetramer with one molecule of pyridoxal 5' phosphate bound per subunit . This tetrameric conformation depends on the presence of the Mg2+ cofactor. In its absence, arginine decarboxylase exists in equilibrium between the monomeric and dimeric forms, with the exact distribution of forms depending on pH . A crystal structure of SpeA has been solved at 3.1 Å resolution and shows a dimer-of-dimers arrangement . In experiments with an E. coli W strain, showed that putrescine biosynthesis preferentially utilized exogenously added arginine. Cells grown with exogenous arginine preferentially utilize the PWY-40 (SpeA-SpeB) pathway . A significant portion of SpeA is associated with the cell envelope, suggesting that it is primarily involved in the conversion of exogenous rather than endogenous arginine to putrescine...

## Biological Role

Catalyzes L-arginine carboxy-lyase (agmatine-forming) (reaction.R00566). Component of biosynthetic arginine decarboxylase (complex.ecocyc.ARGDECARBOXBIO-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the biosynthesis of agmatine from arginine. {ECO:0000269|PubMed:19603287, ECO:0000269|PubMed:2198270, ECO:0000269|PubMed:4571773}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00566|reaction.R00566]] `KEGG` `database` - via EC:4.1.1.19
- `is_component_of` --> [[complex.ecocyc.ARGDECARBOXBIO-CPLX|complex.ecocyc.ARGDECARBOXBIO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2938|gene.b2938]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21170`
- `KEGG:ecj:JW2905;eco:b2938;ecoc:C3026_16085;`
- `GeneID:947432;`
- `GO:GO:0000287; GO:0006527; GO:0008295; GO:0008792; GO:0009446; GO:0030170; GO:0033388; GO:0042597; GO:0042802; GO:0051289`
- `EC:4.1.1.19`

## Notes

Biosynthetic arginine decarboxylase (ADC) (EC 4.1.1.19)
