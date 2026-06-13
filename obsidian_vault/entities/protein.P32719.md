---
entity_id: "protein.P32719"
entity_type: "protein"
name: "alsE"
source_database: "UniProt"
source_id: "P32719"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alsE yjcU b4085 JW4046"
---

# alsE

`protein.P32719`

## Static

- Type: `protein`
- Source: `UniProt:P32719`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible epimerization of D-allulose 6-phosphate to D-fructose 6-phosphate. Can also catalyze with lower efficiency the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_02226, ECO:0000269|PubMed:18700786, ECO:0000269|PubMed:9401019}. Allulose-6-phosphate 3-epimerase catalyzes the final step in the degradation of D-allose, the conversion of D-allulose-6-phosphate to D-fructose-6-phosphate, which feeds into the glycolysis pathway . Crystal structures of AlsE have been solved. The enzyme has a (β/α)8 barrel structure; the active site is located at the C-terminal end of the β strands. Site-directed mutants that were predicted to alter substrate specificity have been purified and analyzed . Expression of alsE is induced by allose, and an alsE mutant is unable to catabolize allose . AlsE: "allulose 6-phosphate epimerase"

## Biological Role

Catalyzes RXN0-304 (reaction.ecocyc.RXN0-304). Bound by Cobalt ion (molecule.C00175).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible epimerization of D-allulose 6-phosphate to D-fructose 6-phosphate. Can also catalyze with lower efficiency the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_02226, ECO:0000269|PubMed:18700786, ECO:0000269|PubMed:9401019}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-304|reaction.ecocyc.RXN0-304]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4085|gene.b4085]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32719`
- `KEGG:ecj:JW4046;eco:b4085;ecoc:C3026_22085;`
- `GeneID:948595;`
- `GO:GO:0004750; GO:0005829; GO:0005975; GO:0009052; GO:0019316; GO:0034700; GO:0046872`
- `EC:5.1.3.-`

## Notes

D-allulose-6-phosphate 3-epimerase (EC 5.1.3.-)
