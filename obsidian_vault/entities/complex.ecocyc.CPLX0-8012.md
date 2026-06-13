---
entity_id: "complex.ecocyc.CPLX0-8012"
entity_type: "complex"
name: "glucose-1-phosphate thymidylyltransferase 2"
source_database: "EcoCyc"
source_id: "CPLX0-8012"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glucose-1-phosphate thymidylyltransferase 2

`complex.ecocyc.CPLX0-8012`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8012`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P61887|protein.P61887]]

## Enriched Summary

dTDP-glucose pyrophosphorylase 2 (RffH) is involved in the synthesis of enterobacterial common antigen (ECA). This enzyme has been shown to have glucose-1-phosphate thymidyltransferase activity. RffH is one of two glucose-1-phosphate thymidylyltransferase isozymes encoded in E. coli K-12. dTDP-glucose pyrophosphorylase is encoded by the rffH gene which is paralogous to rfbA. RfbA is another dTDP-glucose pyrophosphorylase which catalyzes the same reaction as RffH, but functions in the rhamnose biosynthesis pathway. There is 68% amino acid sequence identity between RffH and RfbA. Of the two enzymes, CPLX0-8034 RfbA appears to be the major contributor to dTDP-glucose biosynthesis in vivo . The crystal structure has been reported in the presence of deoxythimidine (dTTP) and Mg2+. The crystal structure shows a tetrameric enzyme with monomers that have an overall α/β fold with two domains, the nucleotide binding and sugar domain. The active site is located at the domain interface. Two conserved aspartate residues act as ligands to the Mg2+ ion. dTDP-glucose pyrophosphorylase 2 (RffH) is involved in the synthesis of enterobacterial common antigen (ECA). This enzyme has been shown to have glucose-1-phosphate thymidyltransferase activity. RffH is one of two glucose-1-phosphate thymidylyltransferase isozymes encoded in E. coli K-12...

## Biological Role

Catalyzes DTDPGLUCOSEPP-RXN (reaction.ecocyc.DTDPGLUCOSEPP-RXN).

## Annotation

dTDP-glucose pyrophosphorylase 2 (RffH) is involved in the synthesis of enterobacterial common antigen (ECA). This enzyme has been shown to have glucose-1-phosphate thymidyltransferase activity. RffH is one of two glucose-1-phosphate thymidylyltransferase isozymes encoded in E. coli K-12. dTDP-glucose pyrophosphorylase is encoded by the rffH gene which is paralogous to rfbA. RfbA is another dTDP-glucose pyrophosphorylase which catalyzes the same reaction as RffH, but functions in the rhamnose biosynthesis pathway. There is 68% amino acid sequence identity between RffH and RfbA. Of the two enzymes, CPLX0-8034 RfbA appears to be the major contributor to dTDP-glucose biosynthesis in vivo . The crystal structure has been reported in the presence of deoxythimidine (dTTP) and Mg2+. The crystal structure shows a tetrameric enzyme with monomers that have an overall α/β fold with two domains, the nucleotide binding and sugar domain. The active site is located at the domain interface. Two conserved aspartate residues act as ligands to the Mg2+ ion.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P61887|protein.P61887]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8012`
- `QSPROTEOME:QS00182715`

## Notes

4*protein.P61887
