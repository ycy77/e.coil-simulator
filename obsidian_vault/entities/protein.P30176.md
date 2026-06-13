---
entity_id: "protein.P30176"
entity_type: "protein"
name: "ybiA"
source_database: "UniProt"
source_id: "P30176"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybiA b0798 JW0783"
---

# ybiA

`protein.P30176`

## Static

- Type: `protein`
- Source: `UniProt:P30176`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond in the first two intermediates of riboflavin biosynthesis, which are highly reactive metabolites, yielding relatively innocuous products. Thus, can divert a surplus of harmful intermediates into relatively harmless products and pre-empt the damage these intermediates would otherwise do. Helps maintain flavin levels. May act on other substrates in vivo. Has no activity against GTP, nucleoside monophosphates or ADP-ribose (PubMed:25431972). Is Required for swarming motility (PubMed:17122336). {ECO:0000269|PubMed:17122336, ECO:0000269|PubMed:25431972}. YbiA catalyzes the hydrolysis of the N-glycosidic bond in DIAMINO-OH-PHOSPHORIBOSYLAMINO-PYR and CPD-602, highly reactive metabolites which are the first two intermediates in the RIBOSYN2-PWY pathway . Comparative genomics suggests that the YbiA family of proteins may play a role in NAD metabolism . Site-directed mutagenesis of conserved residues resulted in reduced or abolished catalytic activity. A ΔybiA mutant contains reduced amounts of FAD and FMN . A ybiA mutant has a defect in swarming, but not swimming motility .

## Biological Role

Catalyzes RXN-19407 (reaction.ecocyc.RXN-19407).

## Annotation

FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond in the first two intermediates of riboflavin biosynthesis, which are highly reactive metabolites, yielding relatively innocuous products. Thus, can divert a surplus of harmful intermediates into relatively harmless products and pre-empt the damage these intermediates would otherwise do. Helps maintain flavin levels. May act on other substrates in vivo. Has no activity against GTP, nucleoside monophosphates or ADP-ribose (PubMed:25431972). Is Required for swarming motility (PubMed:17122336). {ECO:0000269|PubMed:17122336, ECO:0000269|PubMed:25431972}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-19407|reaction.ecocyc.RXN-19407]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0798|gene.b0798]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30176`
- `KEGG:ecj:JW0783;eco:b0798;`
- `GeneID:945426;`
- `GO:GO:0009231; GO:0016799; GO:0034656; GO:0071978; GO:1901135`
- `EC:3.2.2.-`

## Notes

N-glycosidase YbiA (EC 3.2.2.-) (Riboflavin biosynthesis intermediates N-glycosidase)
