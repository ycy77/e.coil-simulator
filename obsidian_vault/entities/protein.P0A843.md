---
entity_id: "protein.P0A843"
entity_type: "protein"
name: "tatE"
source_database: "UniProt"
source_id: "P0A843"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00903}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00903}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tatE ybeC b0627 JW0622"
---

# tatE

`protein.P0A843`

## Static

- Type: `protein`
- Source: `UniProt:P0A843`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00903}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00903}.

## Enriched Summary

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. TatE shares overlapping functions with TatA. {ECO:0000255|HAMAP-Rule:MF_00903, ECO:0000269|PubMed:9649434}. TatE is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins. TatE is predicted to contain an N-terminal transmembrane domain followed by an amphipathic helix and a cytoplasmic domain; TatE has 53% amino acid identity to TatA . ΔtatA ΔtatE knockout mutants are unable to export a number of redox cofactor containing proteins; a ΔtatA strain is significantly more compromised for export than a ΔtatE strain . tatE forms a monocistronic unit which is transcribed consititutively; TatE is synthesized at a much lower level than TatA . TatE supports a lower level of Tat mediated transport than TatA . TatE: twin arginine translocation

## Biological Role

Component of twin arginine protein translocation system (complex.ecocyc.TATABCE-CPLX).

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. TatE shares overlapping functions with TatA. {ECO:0000255|HAMAP-Rule:MF_00903, ECO:0000269|PubMed:9649434}.

## Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TATABCE-CPLX|complex.ecocyc.TATABCE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0627|gene.b0627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A843`
- `KEGG:ecj:JW0622;eco:b0627;ecoc:C3026_03130;`
- `GeneID:86863146;93776856;945228;`
- `GO:GO:0005886; GO:0008320; GO:0033281; GO:0043953; GO:0065002`

## Notes

Sec-independent protein translocase protein TatE
