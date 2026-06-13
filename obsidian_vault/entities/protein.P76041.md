---
entity_id: "protein.P76041"
entity_type: "protein"
name: "ycjM"
source_database: "UniProt"
source_id: "P76041"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjM ggaP b1309 JW1302"
---

# ycjM

`protein.P76041`

## Static

- Type: `protein`
- Source: `UniProt:P76041`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible phosphorolysis of glucosylglycerate into alpha-D-glucose 1-phosphate (Glc1P) and D-glycerate (also called (R)-glycerate) (PubMed:28754708, PubMed:29684280). May be a regulator of intracellular levels of glucosylglycerate, a compatible solute that primarily protects organisms facing salt stress and very specific nutritional constraints (PubMed:28754708). Cannot catalyze the phosphorolysis of sucrose (PubMed:28754708). Does not act on other sugars such as alpha-D-galactose 1-phosphate, alpha-D-mannose 1-phosphate or beta-D-glucose 1-phosphate; in vitro D-erythronate can substitute for D-glycerate with a much lower efficiency (PubMed:29684280). {ECO:0000269|PubMed:28754708, ECO:0000269|PubMed:29684280}. YcjM and an enzyme from Meiothermus silvanus both belong to the same subfamily of the GH13_18 family of phosphorylases. The purified M. silvanus enzyme as well as overexpressed, but unpurified YcjM are able to catalyze synthesis of glucosylglycerol from glucose-1-phosphate and glycerol. YcjM showed no activity with sucrose and many other potential acceptor substrates . Glucosylglycerate phosphorylase activity was later shown for purified YcjM; the enzyme is specific for α-(1,2)-D-glucose-D-glycerate .

## Biological Role

Catalyzes 2-O-(alpha-D-glucopyranosyl)-D-glycerate:phosphate alpha-D-glucosyltransferase (configuration-retaining) (reaction.R11959), RXN-18999 (reaction.ecocyc.RXN-18999).

## Annotation

FUNCTION: Catalyzes the reversible phosphorolysis of glucosylglycerate into alpha-D-glucose 1-phosphate (Glc1P) and D-glycerate (also called (R)-glycerate) (PubMed:28754708, PubMed:29684280). May be a regulator of intracellular levels of glucosylglycerate, a compatible solute that primarily protects organisms facing salt stress and very specific nutritional constraints (PubMed:28754708). Cannot catalyze the phosphorolysis of sucrose (PubMed:28754708). Does not act on other sugars such as alpha-D-galactose 1-phosphate, alpha-D-mannose 1-phosphate or beta-D-glucose 1-phosphate; in vitro D-erythronate can substitute for D-glycerate with a much lower efficiency (PubMed:29684280). {ECO:0000269|PubMed:28754708, ECO:0000269|PubMed:29684280}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11959|reaction.R11959]] `KEGG` `database` - via EC:2.4.1.352
- `catalyzes` --> [[reaction.ecocyc.RXN-18999|reaction.ecocyc.RXN-18999]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1309|gene.b1309]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76041`
- `KEGG:ecj:JW1302;eco:b1309;ecoc:C3026_07675;`
- `GeneID:945659;`
- `GO:GO:0005975; GO:0110068`
- `EC:2.4.1.352`

## Notes

Glucosylglycerate phosphorylase (GGa phosphorylase) (GGaP) (EC 2.4.1.352)
