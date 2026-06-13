---
entity_id: "protein.P76217"
entity_type: "protein"
name: "astD"
source_database: "UniProt"
source_id: "P76217"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "astD ydjU b1746 JW5282"
---

# astD

`protein.P76217`

## Static

- Type: `protein`
- Source: `UniProt:P76217`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NAD-dependent reduction of succinylglutamate semialdehyde into succinylglutamate (Probable). Also shows in vitro activity with decanal or succinic semialdehyde as the electron donor and NAD as the electron acceptor. No activity is detected with NADP as the electron acceptor. Therefore, is an aldehyde dehydrogenase with broad substrate specificity (PubMed:15808744). {ECO:0000269|PubMed:15808744, ECO:0000305|PubMed:9696779}. Succinylglutamate semialdehyde dehydrogenase catalyzes the fourth reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The activity has only been assayed in crude cell extracts, and thus there is little direct evidence for the function of the astD gene product . However, a high-throughput screen of purified proteins showed that AstD is an aldehyde dehydrogenase with broad substrate specificity. The enzyme is active with NAD, but not NADP, as the electron acceptor . Expression of the enzymes of the AST pathway is regulated by arginine and nitrogen availability via ArgR and NtrC . astD was identified in a screen for genes that are activated by conditioned medium. Expression was decresed in an rpoS mutant , and the extracellular signal was found to be indole . Expression of astD is also induced by high pH .

## Biological Role

Catalyzes SUCCGLUALDDEHYD-RXN (reaction.ecocyc.SUCCGLUALDDEHYD-RXN).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD-dependent reduction of succinylglutamate semialdehyde into succinylglutamate (Probable). Also shows in vitro activity with decanal or succinic semialdehyde as the electron donor and NAD as the electron acceptor. No activity is detected with NADP as the electron acceptor. Therefore, is an aldehyde dehydrogenase with broad substrate specificity (PubMed:15808744). {ECO:0000269|PubMed:15808744, ECO:0000305|PubMed:9696779}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUCCGLUALDDEHYD-RXN|reaction.ecocyc.SUCCGLUALDDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1746|gene.b1746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76217`
- `KEGG:ecj:JW5282;eco:b1746;ecoc:C3026_09975;`
- `GeneID:946260;`
- `GO:GO:0004029; GO:0004777; GO:0019544; GO:0019545; GO:0043824`
- `EC:1.2.1.71`

## Notes

N-succinylglutamate 5-semialdehyde dehydrogenase (EC 1.2.1.71) (Succinylglutamic semialdehyde dehydrogenase) (SGSD)
