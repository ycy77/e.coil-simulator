---
entity_id: "protein.Q6BF16"
entity_type: "protein"
name: "dgoA"
source_database: "UniProt"
source_id: "Q6BF16"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgoA yidU b4477 JW5628"
---

# dgoA

`protein.Q6BF16`

## Static

- Type: `protein`
- Source: `UniProt:Q6BF16`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the degradation of galactose via the DeLey-Doudoroff pathway. Catalyzes the reversible, stereospecific retro-aldol cleavage of 2-keto-3-deoxy-6-phosphogalactonate (KDPGal) to pyruvate and D-glyceraldehyde-3-phosphate. In the synthetic direction, it catalyzes the addition of pyruvate to electrophilic aldehydes with re-facial selectivity. It can use a limited number of aldehyde substrates, including D-glyceraldehyde-3-phosphate (natural substrate), D-glyceraldehyde, glycolaldehyde, 2-pyridinecarboxaldehyde, D-ribose, D-erythrose and D-threose. It efficiently catalyzes aldol addition only using pyruvate as the nucleophilic component and accepts both stereochemical configurations at C2 of the electrophile. {ECO:0000269|PubMed:17981470, ECO:0000269|PubMed:324806}. 2-oxo-3-deoxygalactonate 6-phosphate aldolase (KDPGal aldolase) catalyzes the final reaction in the degradation of D-galactonate, an aldol cleavage resulting in GA3P and pyruvate which enter central metabolism . Crystal structures of KDPGal aldolase have been determined. Comparison to the crystal structure of KDPG aldolase led to the hypothesis that the V154 residue was involved in stereoselectivity of the enzyme. A V154T mutant shows reduced stereoselectivity, but also reduced catalytic efficiency...

## Biological Role

Catalyzes DEHYDDEOXPHOSGALACT-ALDOL-RXN (reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the degradation of galactose via the DeLey-Doudoroff pathway. Catalyzes the reversible, stereospecific retro-aldol cleavage of 2-keto-3-deoxy-6-phosphogalactonate (KDPGal) to pyruvate and D-glyceraldehyde-3-phosphate. In the synthetic direction, it catalyzes the addition of pyruvate to electrophilic aldehydes with re-facial selectivity. It can use a limited number of aldehyde substrates, including D-glyceraldehyde-3-phosphate (natural substrate), D-glyceraldehyde, glycolaldehyde, 2-pyridinecarboxaldehyde, D-ribose, D-erythrose and D-threose. It efficiently catalyzes aldol addition only using pyruvate as the nucleophilic component and accepts both stereochemical configurations at C2 of the electrophile. {ECO:0000269|PubMed:17981470, ECO:0000269|PubMed:324806}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN|reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4477|gene.b4477]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q6BF16`
- `KEGG:ecj:JW5628;eco:b4477;ecoc:C3026_20020;`
- `GeneID:2847766;`
- `GO:GO:0008674; GO:0034194`
- `EC:4.1.2.21`

## Notes

2-dehydro-3-deoxy-6-phosphogalactonate aldolase (EC 4.1.2.21) (2-oxo-3-deoxygalactonate 6-phosphate aldolase) (6-phospho-2-dehydro-3-deoxygalactonate aldolase) (6-phospho-2-keto-3-deoxygalactonate aldolase) (KDPGal aldolase)
