---
entity_id: "protein.P76558"
entity_type: "protein"
name: "maeB"
source_database: "UniProt"
source_id: "P76558"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "maeB ypfF b2463 JW2447"
---

# maeB

`protein.P76558`

## Static

- Type: `protein`
- Source: `UniProt:P76558`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of malate to pyruvate (PubMed:17557829). In vitro, shows malolactic enzyme activity in the presence of NADPH. However, it is unlikely that this activity is of relevance in E.coli, which produces little NADPH (PubMed:33824210). {ECO:0000269|PubMed:17557829, ECO:0000269|PubMed:33824210}. E. coli encodes two "malic enzymes" that catalyze the decarboxylation of malate to form pyruvate with concomitant reduction of NAD(P)+. One enzyme, MaeB (described here) reduces NADP+, while the other, MALIC-NAD-MONOMER MaeA, reduces NAD+ . MaeB activity is highly regulated by key metabolites . Inhibition by acetyl-CoA may direct carbon distribution at the PEP-pyruvate-oxaloacetate metabolic node . MaeB appears to be important for supplying NADPH during growth on two-carbon compounds ; flux-balance analysis predicts flux to pyruvate through MaeB during growth on acetate . Metabolic flux through the malic enzymes during growth on glycerol as the sole source of carbon appears to be essentially zero . A malolactic enzyme activity - decarboxylation of malate to lactate without concomitant reduction of NAD(P)+ - was recently discovered for MaeB; this activity may contribute to maintaining the NADPH/NADH balance of the cell . Purification of the enzyme from E. coli K10 and K-12 indicated that it was composed of 8 subunits...

## Biological Role

Catalyzes (S)-malate:NADP+ oxidoreductase(oxaloacetate-decarboxylating) (reaction.R00216), oxaloacetate carboxy-lyase (pyruvate-forming) (reaction.R00217). Component of malate dehydrogenase (oxaloacetate-decarboxylating) (NADP+) (complex.ecocyc.MALIC-NADP-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of malate to pyruvate (PubMed:17557829). In vitro, shows malolactic enzyme activity in the presence of NADPH. However, it is unlikely that this activity is of relevance in E.coli, which produces little NADPH (PubMed:33824210). {ECO:0000269|PubMed:17557829, ECO:0000269|PubMed:33824210}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00216|reaction.R00216]] `KEGG` `database` - via EC:1.1.1.40
- `catalyzes` --> [[reaction.R00217|reaction.R00217]] `KEGG` `database` - via EC:1.1.1.40
- `is_component_of` --> [[complex.ecocyc.MALIC-NADP-CPLX|complex.ecocyc.MALIC-NADP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b2463|gene.b2463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76558`
- `KEGG:ecj:JW2447;eco:b2463;ecoc:C3026_13665;`
- `GeneID:946947;`
- `GO:GO:0004473; GO:0005829; GO:0006108; GO:0008948; GO:0016746; GO:0030145; GO:0042802; GO:0043883; GO:0051287`
- `EC:1.1.1.40`

## Notes

NADP-dependent malic enzyme (NADP-ME) (EC 1.1.1.40)
