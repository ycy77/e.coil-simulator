---
entity_id: "protein.P76190"
entity_type: "protein"
name: "mepH"
source_database: "UniProt"
source_id: "P76190"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mepH ydhO b1655 JW5270"
---

# mepH

`protein.P76190`

## Static

- Type: `protein`
- Source: `UniProt:P76190`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Partially suppresses an mepS disruption mutant. {ECO:0000269|PubMed:23062283}. Purified MepH is a murein DD-endopeptidase with specificity for D-ala-m-DAP (4→3) cross-links; the endopeptidase activity of MepH is associated with murein incorporation during cell growth; purified MepH has no LD carboxypeptidase activity . Purified MepH has weak hydrolytic activity on m-DAP-m-DAP (3→3) cross-links and, in contradiction of earlier results, also displays L,D-carboxypeptidase activity . An E. coli K-12 strain lacking all three murein endopeptidases MepH, G7147-MONOMER "MepS" and EG10013-MONOMER "MepM" exhibits extensive cell lysis and a terminal phenotype. Incorporation of labelled mDAP into the peptidoglycan sacculi is decreased by up to 80% in the triple deletion strain. Over-expression of any of the three genes from a plasmid allows the triple deletion mutant to grow normally. This suggests that MepH, MepS and MepM perform essential and redundant functions in vivo . MepH is a substrate of the EG10760-MONOMER Prc-EG12371-MONOMER Nlp proteolytic system .

## Biological Role

Catalyzes RXN-16664 (reaction.ecocyc.RXN-16664), RXN0-3461 (reaction.ecocyc.RXN0-3461), RXN0-5407 (reaction.ecocyc.RXN0-5407).

## Annotation

FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Partially suppresses an mepS disruption mutant. {ECO:0000269|PubMed:23062283}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16664|reaction.ecocyc.RXN-16664]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5407|reaction.ecocyc.RXN0-5407]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1655|gene.b1655]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76190`
- `KEGG:ecj:JW5270;eco:b1655;ecoc:C3026_09495;`
- `GeneID:93775809;945210;`
- `GO:GO:0000270; GO:0004175; GO:0006508; GO:0008234; GO:0045227; GO:0071555`
- `EC:3.4.-.-`

## Notes

Murein DD-endopeptidase MepH (EC 3.4.-.-) (Murein hydrolase MepH)
