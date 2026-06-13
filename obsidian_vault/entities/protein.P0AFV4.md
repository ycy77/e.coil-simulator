---
entity_id: "protein.P0AFV4"
entity_type: "protein"
name: "mepS"
source_database: "UniProt"
source_id: "P0AFV4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mepS spr yeiV b2175 JW2163"
---

# mepS

`protein.P0AFV4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFV4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}.

## Enriched Summary

FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Also has weak LD-carboxypeptidase activity on L-mDAP-D-Ala peptide bonds. Partially suppresses a prc disruption mutant. {ECO:0000269|PubMed:23062283, ECO:0000269|PubMed:9158724}. Purified MepS (formerly Spr) is a murein DD-endopeptidase with specificity for D-ala-m-DAP (4→3) cross links; the endopeptidase activity of MepS is associated with murein incorporation during cell growth; purified MepS also has weak LD-carboxypeptidase activity; purifed MepS has murein hydrolase activity on intact peptidoglycan (PG) sacculi . Purified MepS hydrolyses both 4→3 and 3→3 (m-DAP-mDAP) cross-links with similar efficacy . In addition to promoting cell elongation, MepS influences the cell division process; elevated MepS activity interferes with the activation of septal PG biogenesis by the divisome . mepS deletion mutants are unable to grow on nutrient agar at high temperatures - over-expression of mepH or mepM from a plasmid suppresses this phenotype . A strain lacking all three murein endopeptidases MepS, EG10013-MONOMER "MepM", and G6892-MONOMER "MepH" exhibits extensive cell lysis and a terminal phenotype...

## Biological Role

Catalyzes RXN-16664 (reaction.ecocyc.RXN-16664), RXN0-3461 (reaction.ecocyc.RXN0-3461), RXN0-5407 (reaction.ecocyc.RXN0-5407).

## Annotation

FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Also has weak LD-carboxypeptidase activity on L-mDAP-D-Ala peptide bonds. Partially suppresses a prc disruption mutant. {ECO:0000269|PubMed:23062283, ECO:0000269|PubMed:9158724}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16664|reaction.ecocyc.RXN-16664]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5407|reaction.ecocyc.RXN0-5407]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2175|gene.b2175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFV4`
- `KEGG:ecj:JW2163;eco:b2175;ecoc:C3026_12170;`
- `GeneID:86860350;93775006;946686;`
- `GO:GO:0000270; GO:0004175; GO:0006508; GO:0008234; GO:0009254; GO:0009279; GO:0045227; GO:0071555; GO:0106415`
- `EC:3.4.-.-; 3.4.17.13`

## Notes

Murein DD-endopeptidase MepS/Murein LD-carboxypeptidase (EC 3.4.-.-) (EC 3.4.17.13) (Lipoprotein Spr) (Murein hydrolase MepS)
