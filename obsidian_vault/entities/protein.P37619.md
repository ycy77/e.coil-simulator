---
entity_id: "protein.P37619"
entity_type: "protein"
name: "yhhQ"
source_database: "UniProt"
source_id: "P37619"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02088, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02088}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhhQ b3471 JW3436"
---

# yhhQ

`protein.P37619`

## Static

- Type: `protein`
- Source: `UniProt:P37619`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02088, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02088}.

## Enriched Summary

FUNCTION: Involved in the import of queuosine (Q) precursors, required for Q precursor salvage. Transports 7-cyano-7-deazaguanine (preQ(0)) and 7-aminomethyl-7-deazaguanine (preQ(1)), with a preference for preQ(0). {ECO:0000269|PubMed:28208705}. YhhQ is an inner membrane protein implicated in the uptake of queuosine (Q) precursors - 7-cyano-7-deazaguanine (7-CYANO-7-DEAZAGUANINE "preQ0") and 7-aminomethyl-7-deazaguanine (7-AMINOMETHYL-7-DEAZAGUANINE "preQ1") - for Q salvage. Q-modified tRNA is absent in ΔG7431 "queD" and ΔqueD ΔyhhQ strains grown in minimal media with glycerol; Q-modified tRNA is detected when a ΔqueD strain is grown in minimal media plus 10 nM preQ0 or preQ1 but is absent when a ΔqueD ΔyhhQ strain is grown under these conditions . yhhQ expressed from a plasmid restores the presence of Q-modified tRNA in a ΔqueD ΔyhhQ strain . Cleavage of yhhQ mRNA by CPLX0-3281 appears to accelerate its degradation ; a 5' UTR antisense RNA might be required to show cleavage in vitro . A class I type III pre-Q1 (preQ1-IIII)-sensing riboswitch in the 5' leader region of yhhQ mRNA is implicated in translation control . YhhQ is prediced to be an inner membrane protein with six transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . yhhQ is predicted to be a member of the purine (PurR) regulon...

## Biological Role

Catalyzes TRANS-RXN-412 (reaction.ecocyc.TRANS-RXN-412).

## Annotation

FUNCTION: Involved in the import of queuosine (Q) precursors, required for Q precursor salvage. Transports 7-cyano-7-deazaguanine (preQ(0)) and 7-aminomethyl-7-deazaguanine (preQ(1)), with a preference for preQ(0). {ECO:0000269|PubMed:28208705}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-412|reaction.ecocyc.TRANS-RXN-412]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3471|gene.b3471]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37619`
- `KEGG:ecj:JW3436;eco:b3471;ecoc:C3026_18800;`
- `GeneID:947984;`
- `GO:GO:0005886; GO:0022857; GO:0072531`

## Notes

Queuosine precursor transporter (Q precursor transporter)
