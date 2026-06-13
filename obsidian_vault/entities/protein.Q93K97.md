---
entity_id: "protein.Q93K97"
entity_type: "protein"
name: "nudF"
source_database: "UniProt"
source_id: "Q93K97"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudF aspP yqiE yzzG b3034 JW3002"
---

# nudF

`protein.Q93K97`

## Static

- Type: `protein`
- Source: `UniProt:Q93K97`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts on ADP-mannose and ADP-glucose as well as ADP-ribose. Prevents glycogen biosynthesis. The reaction catalyzed by this enzyme is a limiting step of the gluconeogenic process. {ECO:0000269|PubMed:11416161}. NudF is a member of the family of Nudix hydrolases and has ADP-sugar pyrophosphatase activity . ADP-glucose is a precursor molecule for glycogen biosynthesis; thus, it appears that the activity of NudF needs to be regulated. NudF is thought to control the flow of carbon toward glycogen, interconnecting gluconeogenesis with other metabolic pathways . NudF also contributes to the production of dimethylallyl phosphate, which is the substrate for UBIX-MONOMER UbiX-catalyzed generation of the prFMN cofactor in ubiquinone biosynthesis . Gel filtration experiments indicate that the enzyme is a dimer in solution . Crystal structures of NudF in various forms have been solved, showing a domain-swapped dimer where the Nudix motif residues compose a catalytic center . Binding of the substrate and Mg2+ results in a conformational change from an open to a closed complex. The reaction mechanism involves a nucleophilic attack by water at the phosphorus of the adenosyl phosphate . NudF activity is enhanced by macromolecular crowding and is stimulated by glucose-1,6-bisphosphate and nucleotide sugars...

## Biological Role

Component of ADP-sugar pyrophosphatase (complex.ecocyc.CPLX0-3721).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Acts on ADP-mannose and ADP-glucose as well as ADP-ribose. Prevents glycogen biosynthesis. The reaction catalyzed by this enzyme is a limiting step of the gluconeogenic process. {ECO:0000269|PubMed:11416161}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3721|complex.ecocyc.CPLX0-3721]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3034|gene.b3034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q93K97`
- `KEGG:ecj:JW3002;eco:b3034;ecoc:C3026_16570;`
- `GeneID:93778959;947519;`
- `GO:GO:0000287; GO:0005829; GO:0006753; GO:0009408; GO:0016462; GO:0019144; GO:0019693; GO:0042803; GO:0047631`
- `EC:3.6.1.13`

## Notes

ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (ASPPase) (Adenosine diphosphoribose pyrophosphatase) (ADPR-PPase)
