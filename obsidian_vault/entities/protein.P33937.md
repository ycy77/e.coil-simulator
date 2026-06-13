---
entity_id: "protein.P33937"
entity_type: "protein"
name: "napA"
source_database: "UniProt"
source_id: "P33937"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01630, ECO:0000269|PubMed:10234835}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "napA yojC yojD yojE b2206 JW2194"
---

# napA

`protein.P33937`

## Static

- Type: `protein`
- Source: `UniProt:P33937`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01630, ECO:0000269|PubMed:10234835}.

## Enriched Summary

FUNCTION: Catalytic subunit of the periplasmic nitrate reductase complex NapAB. Receives electrons from NapB and catalyzes the reduction of nitrate to nitrite. {ECO:0000255|HAMAP-Rule:MF_01630, ECO:0000269|PubMed:17130127}. The EG12067 gene encodes the molybdoprotein subunit of the periplasmic nitrate reductase . NapA is synthesized as a precursor with a 36 residue signal peptide that is removed upon export to the periplasm . It binds a CPD-7 "[4Fe-4S]" cluster and CPD-582 . Prior to export the signal peptide of NapA is bound to the EG12143 NapD chaperon, preventing premature export. In the absence of NapD, NapA is unstable and is degraded . A NapD binding epitope is located towards the N-terminus of the NapA signal peptide and partially overlaps with a twin arginine motif . An NMR structure of the NapD-NapA signal peptide complex has been reported .

## Biological Role

Catalyzes ferrocytochrome-b:nitrate oxidoreductase (reaction.R00792). Component of periplasmic nitrate reductase (complex.ecocyc.NAP-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

FUNCTION: Catalytic subunit of the periplasmic nitrate reductase complex NapAB. Receives electrons from NapB and catalyzes the reduction of nitrate to nitrite. {ECO:0000255|HAMAP-Rule:MF_01630, ECO:0000269|PubMed:17130127}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00792|reaction.R00792]] `KEGG` `database` - via EC:1.9.6.1
- `is_component_of` --> [[complex.ecocyc.NAP-CPLX|complex.ecocyc.NAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2206|gene.b2206]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33937`
- `KEGG:ecj:JW2194;eco:b2206;ecoc:C3026_12325;`
- `GeneID:947093;`
- `GO:GO:0005506; GO:0006777; GO:0008940; GO:0009055; GO:0009061; GO:0009325; GO:0016020; GO:0030151; GO:0030288; GO:0042128; GO:0042597; GO:0043546; GO:0050140; GO:0051539`
- `EC:1.9.6.1`

## Notes

Periplasmic nitrate reductase (EC 1.9.6.1)
