---
entity_id: "protein.P69423"
entity_type: "protein"
name: "tatC"
source_database: "UniProt"
source_id: "P69423"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}. Note=Localizes at the cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tatC mttB yigU yigV b3839 JW3815"
---

# tatC

`protein.P69423`

## Static

- Type: `protein`
- Source: `UniProt:P69423`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11591389, ECO:0000269|PubMed:15225613, ECO:0000269|PubMed:20169075}. Note=Localizes at the cell poles.

## Enriched Summary

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. Together with TatB, TatC is part of a receptor directly interacting with Tat signal peptides. {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:14580344, ECO:0000269|PubMed:19666509, ECO:0000269|PubMed:20926683, ECO:0000269|PubMed:9660752}. TatC is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins. TatC and TatB form a functional unit that is thought to act as the substrate receptor for the Tat complex. TatC is an integral inner membrane protein . Deletion of tatC blocks the export of precursor proteins that contain twin-arginine signal sequences and are predicted to bind redox cofactors Membrane topology predictions using experimentally determined C terminus locations indicate that TatC has 6 transmembrane helices and the C-terminus is located in the periplasm . TatC may form functional dimers . TatC functions as an obligate oligomer TatC interacts with the twin arginine region of a Tat substrate signal peptide; this interaction does not require TatB . The signal peptide recognition site resides in the N-terminal region and first cytosolic domain of TatC...

## Biological Role

Component of twin arginine protein translocation system (complex.ecocyc.TATABCE-CPLX).

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. Together with TatB, TatC is part of a receptor directly interacting with Tat signal peptides. {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:14580344, ECO:0000269|PubMed:19666509, ECO:0000269|PubMed:20926683, ECO:0000269|PubMed:9660752}.

## Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TATABCE-CPLX|complex.ecocyc.TATABCE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3839|gene.b3839]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69423`
- `KEGG:ecj:JW3815;eco:b3839;ecoc:C3026_20765;`
- `GeneID:86948510;93778097;948328;`
- `GO:GO:0005886; GO:0008320; GO:0009314; GO:0009977; GO:0016020; GO:0033281; GO:0042802; GO:0043953; GO:0065002`

## Notes

Sec-independent protein translocase protein TatC
