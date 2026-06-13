---
entity_id: "protein.P69425"
entity_type: "protein"
name: "tatB"
source_database: "UniProt"
source_id: "P69425"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}. Note=Localizes at the cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tatB mttA2 ysgB b3838 JW5580"
---

# tatB

`protein.P69425`

## Static

- Type: `protein`
- Source: `UniProt:P69425`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}. Note=Localizes at the cell poles.

## Enriched Summary

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. Together with TatC, TatB is part of a receptor directly interacting with Tat signal peptides. TatB may form an oligomeric binding site that transiently accommodates folded Tat precursor proteins before their translocation. {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:10593889, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:14580344, ECO:0000269|PubMed:19666509, ECO:0000269|PubMed:20926683}. TatB is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins; TatB and TatC form a functional unit that is thought to act as the substrate receptor for the Tat complex. TatB is predicted to contain an N-terminal transmembrane domain followed by a cytoplasmic domain . TatB is an integral inner membrane protein; overexpressed TatB lacking the transmembrane domain remains peripherally associated with the inner membrane; TatB forms homooligomers; higher order Tat complexes may be assembled from homooligomeric TatB (and TatA) units . Purified TatB (residues 1-101) consists of 4 α helices (one transmembrane helix, one amphipathic helix and two solvent exposed helices) and adopts an extended 'L-shaped' structure...

## Biological Role

Component of twin arginine protein translocation system (complex.ecocyc.TATABCE-CPLX).

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. Together with TatC, TatB is part of a receptor directly interacting with Tat signal peptides. TatB may form an oligomeric binding site that transiently accommodates folded Tat precursor proteins before their translocation. {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:10593889, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:14580344, ECO:0000269|PubMed:19666509, ECO:0000269|PubMed:20926683}.

## Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TATABCE-CPLX|complex.ecocyc.TATABCE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3838|gene.b3838]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69425`
- `KEGG:ecj:JW5580;eco:b3838;ecoc:C3026_20760;`
- `GeneID:93778098;948319;`
- `GO:GO:0005886; GO:0009977; GO:0033281; GO:0042802; GO:0042803; GO:0043953; GO:0065002`

## Notes

Sec-independent protein translocase protein TatB
