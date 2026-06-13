---
entity_id: "protein.P69428"
entity_type: "protein"
name: "tatA"
source_database: "UniProt"
source_id: "P69428"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Cytoplasmic side {ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}. Note=Abundant all over the membrane, but is more concentrated at the cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tatA mttA1 yigT b3836 JW3813"
---

# tatA

`protein.P69428`

## Static

- Type: `protein`
- Source: `UniProt:P69428`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Cytoplasmic side {ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}. Note=Abundant all over the membrane, but is more concentrated at the cell poles.

## Enriched Summary

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. TatA could form the protein-conducting channel of the Tat system. {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:9649434}. TatA is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins. Homo-oligomeric TatA may form the translocation pore of the complex although other models have been also suggested . TatA is predicted to consist of an N-terminal transmembrane domain followed by an amphipathic helix and a cytoplasmic domain . The topology of TatA has been debated with studies variously suggesting that TatA is exposed at the cytoplasmic face of the membrane , that the N-terminus is located in the periplasm while the C-terminal region adopts a dual topology , that the N-terminus is located in the cytoplasm and the C-terminus adopts a dual topology or that it has a fixed Nout:Cin topology . TatA is an integral inner membrane protein; overexpressed TatA lacking the transmembrane domain does not associate with the inner membrane; TatA forms homo-oligomers; higher order Tat complexes may be assembled from homo-oligomeric TatA (and TatB) units...

## Biological Role

Component of twin arginine protein translocation system (complex.ecocyc.TATABCE-CPLX).

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. TatA could form the protein-conducting channel of the Tat system. {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:9649434}.

## Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TATABCE-CPLX|complex.ecocyc.TATABCE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3836|gene.b3836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69428`
- `KEGG:ecj:JW3813;eco:b3836;ecoc:C3026_20755;`
- `GeneID:86861941;93778099;948321;`
- `GO:GO:0005829; GO:0005886; GO:0008289; GO:0008320; GO:0009977; GO:0033281; GO:0042802; GO:0043953; GO:0065002`

## Notes

Sec-independent protein translocase protein TatA
