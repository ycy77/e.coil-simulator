---
entity_id: "protein.P0ABA6"
entity_type: "protein"
name: "atpG"
source_database: "UniProt"
source_id: "P0ABA6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpG papC uncG b3733 JW3711"
---

# atpG

`protein.P0ABA6`

## Static

- Type: `protein`
- Source: `UniProt:P0ABA6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The gamma chain is believed to be important in regulating ATPase activity and the flow of protons through the CF(0) complex. The gamma subunit appears to play an important role in coupling the catalytic site events with proton translocation in association with the epsilon subunit. The coupling involves conformational changes and probable translocations of one or both subunits . The rate limiting rotation step carried out by this subunit has been investigated and residues involved in this rotation process have been identified . ArcA appears to repress atpG gene expression under anaerobiosis. Two putative ArcA binding sites were identified upstream of this gene , but no promoter upstream of it has been identified. Instead, atpG is transcribed from three promoters: one of them is located usptream of atpI gene and the others are located upstream of atpB gene.

## Biological Role

Component of ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The gamma chain is believed to be important in regulating ATPase activity and the flow of protons through the CF(0) complex.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3733|gene.b3733]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABA6`
- `KEGG:ecj:JW3711;eco:b3733;ecoc:C3026_20230;`
- `GeneID:86861841;93778234;948243;`
- `GO:GO:0005524; GO:0005886; GO:0015986; GO:0016020; GO:0042777; GO:0045259; GO:0046933; GO:0046961`

## Notes

ATP synthase gamma chain (ATP synthase F1 sector gamma subunit) (F-ATPase gamma subunit)
