---
entity_id: "protein.P77243"
entity_type: "protein"
name: "prpD"
source_database: "UniProt"
source_id: "P77243"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prpD yahT b0334 JW0325"
---

# prpD

`protein.P77243`

## Static

- Type: `protein`
- Source: `UniProt:P77243`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the dehydration of 2-methylcitrate (2-MC) to yield the cis isomer of 2-methyl-aconitate. It is also able to catalyze the dehydration of citrate and the hydration of cis-aconitate at a lower rate. Due to its broad substrate specificity, it seems to be responsible for the residual aconitase activity of the acnAB-null mutant. {ECO:0000269|PubMed:11782506, ECO:0000269|PubMed:12473114}. 2-Methylcitrate dehydratase (PrpD) catalyzes the stereospecific dehydration of 2-methylcitrate, a reaction in propionate catabolism via the methylcitrate cycle . PrpD is monomeric in solution . Reports disagree on whether or not PrpD contains an iron-sulfur cluster, and on the substrate specificity of the enzyme . prpD also encodes the residual aconitase-like activity, aconitase C , which constitutes 5% or less of cellular aconitase activity and is observed in an acnA acnB double mutant . Aconitase C activity does not substitute for aconitase A and B activities in vivo and appears not to be reversible, in contrast to true aconitase activity, and is therefore better described as a dehydratase activity...

## Biological Role

Catalyzes (2S,3S)-2-hydroxybutane-1,2,3-tricarboxylate hydro-lyase [(Z)-but-2-ene-1,2,3-tricarboxylate-forming] (reaction.R04424), 2-METHYLCITRATE-DEHYDRATASE-RXN (reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the dehydration of 2-methylcitrate (2-MC) to yield the cis isomer of 2-methyl-aconitate. It is also able to catalyze the dehydration of citrate and the hydration of cis-aconitate at a lower rate. Due to its broad substrate specificity, it seems to be responsible for the residual aconitase activity of the acnAB-null mutant. {ECO:0000269|PubMed:11782506, ECO:0000269|PubMed:12473114}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04424|reaction.R04424]] `KEGG` `database` - via EC:4.2.1.79
- `catalyzes` --> [[reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN|reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0334|gene.b0334]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77243`
- `KEGG:ecj:JW0325;eco:b0334;ecoc:C3026_01635;ecoc:C3026_24805;`
- `GeneID:945931;`
- `GO:GO:0003994; GO:0006099; GO:0019541; GO:0019679; GO:0047547; GO:0051537`
- `EC:4.2.1.3; 4.2.1.79`

## Notes

2-methylcitrate dehydratase (2-MC dehydratase) (EC 4.2.1.79) ((2S,3S)-2-methylcitrate dehydratase) (Aconitate hydratase) (ACN) (Aconitase) (EC 4.2.1.3)
