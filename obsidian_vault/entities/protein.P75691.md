---
entity_id: "protein.P75691"
entity_type: "protein"
name: "yahK"
source_database: "UniProt"
source_id: "P75691"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yahK b0325 JW0317"
---

# yahK

`protein.P75691`

## Static

- Type: `protein`
- Source: `UniProt:P75691`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of a wide range of aldehydes into their corresponding alcohols. Has a strong preference for NADPH over NADH as the electron donor. Cannot use a ketone as substrate. Is a major source of NADPH-dependent aldehyde reductase activity in E.coli. The in vivo functions of YahK has yet to be determined. {ECO:0000269|PubMed:23093176}. YahK is a member of the zinc-containing medium-chain dehydrogenase/reductase family. The enzyme is a major source of NADPH-dependent aldehyde reductase activity in the cell. Catalytic activity of the purified enzyme was measured with a variety of aldehyde substrates . In a metabolically engineered strain, phenylacetaldehyde and 4-hydroxyphenylacetaldehyde are reduced to 2-phenylethanol and 2-(4-hydroxyphenyl)ethanol by the endogenous aldehyde reductases YqhD, YjgB, and YahK . In a different engineered strain LACTALD and CPD-358 were reduced to the corresponding forms of DL-12-Propanediol "propane-1,2-diol" . Conversely, a broad survey of aldehyde reductases showed that YahK was one of several endogenous aldehyde reductases that contribute to the degradation of desired aldehyde end products of metabolic engineering . Mutants that change the preference of the enzyme for the NADPH cosubstrate towards NADH have been constructed . An acetate-tolerant mutant of E...

## Biological Role

Catalyzes primary_alcohol:NADP+ oxidoreductase (reaction.R00625), ethanol:NADP+ oxidoreductase (reaction.R00746), 6-hydroxyhexanoate:NADP+ oxidoreductase (reaction.R05231), ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN (reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN), RXN-15743 (reaction.ecocyc.RXN-15743), RXN-15744 (reaction.ecocyc.RXN-15744), RXN-23340 (reaction.ecocyc.RXN-23340), RXN0-7119 (reaction.ecocyc.RXN0-7119).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of a wide range of aldehydes into their corresponding alcohols. Has a strong preference for NADPH over NADH as the electron donor. Cannot use a ketone as substrate. Is a major source of NADPH-dependent aldehyde reductase activity in E.coli. The in vivo functions of YahK has yet to be determined. {ECO:0000269|PubMed:23093176}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.R00625|reaction.R00625]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` --> [[reaction.R00746|reaction.R00746]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` --> [[reaction.R05231|reaction.R05231]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN|reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15743|reaction.ecocyc.RXN-15743]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15744|reaction.ecocyc.RXN-15744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23340|reaction.ecocyc.RXN-23340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7119|reaction.ecocyc.RXN0-7119]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0325|gene.b0325]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75691`
- `KEGG:ecj:JW0317;eco:b0325;ecoc:C3026_01595;ecoc:C3026_24765;`
- `GeneID:944975;`
- `GO:GO:0008106; GO:0008270; GO:0016616`
- `EC:1.1.1.2`

## Notes

Aldehyde reductase YahK (EC 1.1.1.2) (Zinc-dependent alcohol dehydrogenase YahK)
