---
entity_id: "protein.P0AFK2"
entity_type: "protein"
name: "pnuC"
source_database: "UniProt"
source_id: "P0AFK2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15561822}; Multi-pass membrane protein {ECO:0000305|PubMed:15561822, ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pnuC b0751 JW0734"
---

# pnuC

`protein.P0AFK2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFK2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15561822}; Multi-pass membrane protein {ECO:0000305|PubMed:15561822, ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Required for nicotinamide riboside transport across the inner membrane. {ECO:0000269|PubMed:15561822}. PnuC is a nicotinamide riboside (NR) transporter and member of the nicotinamide ribonucleoside uptake permease family. E. coli pnuC expressed in an Haemophilus influenzae pnuC mutant is able to take up NR but is not able to import nicotinamide mononucleotide (NMN) . PnuC was initially annotated as a nicotinamide mononucleotide (NMN) transporter based on its homology to the PnuC protein from Salmonella enterica . However more recent work in Salmonella has indicated that PnuC in this organism is also an NR transporter which is consistent with its characterisation in E. coli. In Salmonella the conversion of NMN to NR prior to transport is catalysed by the periplasmic acid phosphatase APHA-CPLX AphA . PnuC is monomeric in detergent solution . PnuC variants which are able to transport thiamine have been developed PnuC functions to salvage exogenous NR which is converted to NAD in a two-step reaction catalysed by NadR (see PWY3O-4106) and .

## Biological Role

Catalyzes TRANS-RXN0-481 (reaction.ecocyc.TRANS-RXN0-481).

## Annotation

FUNCTION: Required for nicotinamide riboside transport across the inner membrane. {ECO:0000269|PubMed:15561822}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-481|reaction.ecocyc.TRANS-RXN0-481]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0751|gene.b0751]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFK2`
- `KEGG:ecj:JW0734;eco:b0751;ecoc:C3026_03795;`
- `GeneID:93776730;945350;`
- `GO:GO:0005886; GO:0034257; GO:0034258`

## Notes

Nicotinamide riboside transporter PnuC
