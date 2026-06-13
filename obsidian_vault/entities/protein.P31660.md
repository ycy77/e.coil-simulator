---
entity_id: "protein.P31660"
entity_type: "protein"
name: "prpC"
source_database: "UniProt"
source_id: "P31660"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prpC yahS yzzD b0333 JW0324"
---

# prpC

`protein.P31660`

## Static

- Type: `protein`
- Source: `UniProt:P31660`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the Claisen condensation of propionyl-CoA and oxaloacetate (OAA) to yield 2-methylcitrate (2-MC) and CoA. Also catalyzes the condensation of oxaloacetate with acetyl-CoA to yield citrate but with a lower specificity. {ECO:0000269|PubMed:12473114, ECO:0000269|PubMed:28956599, ECO:0000269|PubMed:8508809, ECO:0000269|PubMed:9325432, ECO:0000269|PubMed:9579066}. 2-Methylcitrate synthase (PrpC) catalyzes the Claisen condensation of propionyl-CoA with oxaloacetate, a reaction in propionate catabolism via the methylcitrate cycle . Production of the enzyme is induced by growth on propionate, but not acetate or glucose . Expression of prpBCDE is regulated by PrpR and catabolite repression and is downregulated in the presence of a variety of sugars . A revertant of a gltA mutant strain produces an enzyme with citrate synthase activity that was later found to be identical to PrpC . The mutation causing the revertant phenotype is unknown. Adaptive laboratory evolution experiments designed to determine whether PrpC can function as a citrate synthase isozyme showed that increased expression and increased copy number of prpC rescued growth of the gltA mutant...

## Biological Role

Catalyzes acetyl-CoA:oxaloacetate C-acetyltransferase (thioester-hydrolysing) (reaction.R00351). Component of 2-methylcitrate synthase (complex.ecocyc.CPLX0-251).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the Claisen condensation of propionyl-CoA and oxaloacetate (OAA) to yield 2-methylcitrate (2-MC) and CoA. Also catalyzes the condensation of oxaloacetate with acetyl-CoA to yield citrate but with a lower specificity. {ECO:0000269|PubMed:12473114, ECO:0000269|PubMed:28956599, ECO:0000269|PubMed:8508809, ECO:0000269|PubMed:9325432, ECO:0000269|PubMed:9579066}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00351|reaction.R00351]] `KEGG` `database` - via EC:2.3.3.5
- `is_component_of` --> [[complex.ecocyc.CPLX0-251|complex.ecocyc.CPLX0-251]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0333|gene.b0333]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31660`
- `KEGG:ecj:JW0324;eco:b0333;ecoc:C3026_01630;ecoc:C3026_24800;`
- `GeneID:947528;`
- `GO:GO:0005737; GO:0005975; GO:0006099; GO:0019679; GO:0036440; GO:0042803; GO:0050440`
- `EC:2.3.3.16; 2.3.3.5`

## Notes

2-methylcitrate synthase (2-MCS) (MCS) (EC 2.3.3.5) ((2S,3S)-2-methylcitrate synthase) (Citrate synthase) (EC 2.3.3.16)
