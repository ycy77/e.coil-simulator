---
entity_id: "protein.P11868"
entity_type: "protein"
name: "tdcD"
source_database: "UniProt"
source_id: "P11868"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcD yhaA b3115 JW5806"
---

# tdcD

`protein.P11868`

## Static

- Type: `protein`
- Source: `UniProt:P11868`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of propionyl phosphate and ADP to propionate and ATP. It can also use acetyl phosphate as phosphate group acceptor. {ECO:0000255|HAMAP-Rule:MF_01881, ECO:0000269|PubMed:9484901}. The tdcD gene encodes a protein with propionate and acetate kinase activity. Propionate kinase functions in the anaerobic degradation of threonine . Evidence suggests that TdcD also catalyzes the reverse reaction converting propionyl-phosphate and ADP to propionate and ATP, which is the last step in pathway PWY-5437. E. coli double null mutants deficient in TdcD and AckA activity, or Pta and AckA activity were unable to metabolize threonine to propionate. This suggested the occurrence of both this reaction and the preceding reaction that converts propanoyl-CoA and phosphate to propionyl-phosphate and coenzyme A in this pathway . Based on sequence similarity, TdcD was predicted to be an acetate kinase . Overexpression of tdcD partially rescues the anaerobic growth defect of an ackA mutant. A tdcD deletion mutant has no obvious phenotype . E. coli TdcD shows 42% identity and 62% overall similarity with TdcD from Salmonella enterica subsp. enterica serovar Typhimurium. The crystal structure of TdcD from Salmonella enterica subsp...

## Biological Role

Catalyzes ATP:acetate phosphotransferase (reaction.R00315), PROPKIN-RXN (reaction.ecocyc.PROPKIN-RXN).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of propionyl phosphate and ADP to propionate and ATP. It can also use acetyl phosphate as phosphate group acceptor. {ECO:0000255|HAMAP-Rule:MF_01881, ECO:0000269|PubMed:9484901}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00315|reaction.R00315]] `KEGG` `database` - via EC:2.7.2.15
- `catalyzes` --> [[reaction.ecocyc.PROPKIN-RXN|reaction.ecocyc.PROPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3115|gene.b3115]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11868`
- `KEGG:ecj:JW5806;eco:b3115;ecoc:C3026_16990;`
- `GeneID:947635;`
- `GO:GO:0005524; GO:0005829; GO:0006083; GO:0006567; GO:0008776; GO:0008980; GO:0019665; GO:0046872; GO:0070689`
- `EC:2.7.2.15`

## Notes

Propionate kinase (EC 2.7.2.15)
