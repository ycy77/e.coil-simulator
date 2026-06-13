---
entity_id: "protein.P76352"
entity_type: "protein"
name: "yeeO"
source_database: "UniProt"
source_id: "P76352"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeeO b1985 JW1965"
---

# yeeO

`protein.P76352`

## Static

- Type: `protein`
- Source: `UniProt:P76352`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: A transporter able to export peptides and flavins. When overexpressed allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide, overproduction of this protein increases its export (PubMed:20067529). When overexpressed increases secretion of FMN and FAD but not riboflavin; intracellular concentrations of FMN and riboflavin rise, possibly to compensate for increased secretion (PubMed:25482085). Increased overexpression causes slight cell elongation (PubMed:25482085). {ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:25482085}. YeeO belongs to the MATE (multi antimicrobial extrusion family or multidrug and toxic compound extrusion) family of transporters . E. coli K-12 (strain BW25113) naturally secretes flavins including riboflavin, flavin mononucleotide (FMN) and flavin adenine dinucleotide (FAD); overexpression of yeeO from a plasmid shifts the flavin secretion profile towards FMN and FAD. Paradoxically, it also increases the intracellular concentration of FMN and riboflavin and is associated with abnormal cell elongation...

## Biological Role

Catalyzes TRANS-RXN-272 (reaction.ecocyc.TRANS-RXN-272), TRANS-RXN0-595 (reaction.ecocyc.TRANS-RXN0-595).

## Annotation

FUNCTION: A transporter able to export peptides and flavins. When overexpressed allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide, overproduction of this protein increases its export (PubMed:20067529). When overexpressed increases secretion of FMN and FAD but not riboflavin; intracellular concentrations of FMN and riboflavin rise, possibly to compensate for increased secretion (PubMed:25482085). Increased overexpression causes slight cell elongation (PubMed:25482085). {ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:25482085}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-272|reaction.ecocyc.TRANS-RXN-272]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-595|reaction.ecocyc.TRANS-RXN0-595]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1985|gene.b1985]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76352`
- `KEGG:ecj:JW1965;eco:b1985;`
- `GeneID:946506;`
- `GO:GO:0005886; GO:0015031; GO:0015230; GO:0015297; GO:0016020; GO:0035350; GO:0035442; GO:0042910; GO:0044610; GO:0071916`

## Notes

Probable FMN/FAD exporter YeeO
