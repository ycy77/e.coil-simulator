---
entity_id: "protein.P0AGC5"
entity_type: "protein"
name: "mltF"
source_database: "UniProt"
source_id: "P0AGC5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_02016, ECO:0000269|PubMed:18234673}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_02016, ECO:0000269|PubMed:18234673}. Note=Attached to the inner leaflet of the outer membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mltF yfhD b2558 JW2542"
---

# mltF

`protein.P0AGC5`

## Static

- Type: `protein`
- Source: `UniProt:P0AGC5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_02016, ECO:0000269|PubMed:18234673}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_02016, ECO:0000269|PubMed:18234673}. Note=Attached to the inner leaflet of the outer membrane.

## Enriched Summary

FUNCTION: Murein-degrading enzyme that degrades murein glycan strands and insoluble, high-molecular weight murein sacculi, with the concomitant formation of a 1,6-anhydromuramoyl product. Lytic transglycosylases (LTs) play an integral role in the metabolism of the peptidoglycan (PG) sacculus. Their lytic action creates space within the PG sacculus to allow for its expansion as well as for the insertion of various structures such as secretion systems and flagella. mltF encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan (PG) with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. mtlF encodes a predicted protein with a cleavable signal sequence, an N-terminal non-glycosylase domain and a C-terminal domain with glycosyltransferase activity; MtlF is an outer membrane associated protein . The purified enzyme (residues 23 - 518) degrades insoluble peptidoglycan to release 1,6-anhydromuropeptides in vitro; the purified C-terminal domain of the enzyme (residues 283Ala-518Asn) is able to bind and degrade insoluble PG in vitro; the purified N-terminal (non glycosylase) domain (residues 22Leu-271Asp) is devoid of PG binding and lytic activity; the N-terminal domain may serve to modulate the activity of the C-terminal domain...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391).

## Annotation

FUNCTION: Murein-degrading enzyme that degrades murein glycan strands and insoluble, high-molecular weight murein sacculi, with the concomitant formation of a 1,6-anhydromuramoyl product. Lytic transglycosylases (LTs) play an integral role in the metabolism of the peptidoglycan (PG) sacculus. Their lytic action creates space within the PG sacculus to allow for its expansion as well as for the insertion of various structures such as secretion systems and flagella.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2558|gene.b2558]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGC5`
- `KEGG:ecj:JW2542;eco:b2558;ecoc:C3026_14160;`
- `GeneID:75206251;947028;`
- `GO:GO:0008933; GO:0009253; GO:0009279; GO:0016998; GO:0071555`
- `EC:4.2.2.n1`

## Notes

Membrane-bound lytic murein transglycosylase F (EC 4.2.2.n1) (Murein lyase F)
