---
entity_id: "protein.P0AFS9"
entity_type: "protein"
name: "mepM"
source_database: "UniProt"
source_id: "P0AFS9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=Uniform peripheral location, with partial enrichment at cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mepM yebA b1856 JW5304"
---

# mepM

`protein.P0AFS9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFS9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=Uniform peripheral location, with partial enrichment at cell poles.

## Enriched Summary

FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Partially suppresses an mepS disruption mutant. {ECO:0000269|PubMed:23062283}. Purified MepM is a dual specificity murein endopeptidase which cleaves both D-ala-m-DAP (4 → 3) and m-DAP-mDAP (3 → 3) cross-links with similar efficacy; the endopeptidase activity of MepM is associated with murein incorporation during cell growth. MepM is a metalloendopeptidase - activity is dependent on the presence of a divalent metal ion . In addition to promoting cell elongation, MepM influences the cell division process; elevated activity of the endopeptidases which promote cell elongation interferes with the activation of septal PG biogenesis by the divisome . An E. coli K-12 strain lacking all three murein endopeptidases MepM, G7147-MONOMER "MepS" and G6892-MONOMER "MepH" exhibits extensive cell lysis and a terminal phenotype. Incorporation of labelled mDAP into the peptidoglycan sacculi is decreased by up to 80% in the triple deletion strain. Over-expression of any of the three genes from a plasmid allows the triple deletion mutant to grow normally...

## Biological Role

Catalyzes RXN0-3461 (reaction.ecocyc.RXN0-3461), RXN0-5407 (reaction.ecocyc.RXN0-5407).

## Annotation

FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Partially suppresses an mepS disruption mutant. {ECO:0000269|PubMed:23062283}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5407|reaction.ecocyc.RXN0-5407]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1856|gene.b1856]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFS9`
- `KEGG:ecj:JW5304;eco:b1856;ecoc:C3026_10575;`
- `GeneID:75171927;75202739;946376;`
- `GO:GO:0000270; GO:0004175; GO:0004222; GO:0005886; GO:0006508; GO:0009254; GO:0045227; GO:0046872; GO:0071555`
- `EC:3.4.24.-`

## Notes

Murein DD-endopeptidase MepM (EC 3.4.24.-) (Murein hydrolase MepM) (ORFU)
