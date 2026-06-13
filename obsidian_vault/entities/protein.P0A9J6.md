---
entity_id: "protein.P0A9J6"
entity_type: "protein"
name: "rbsK"
source_database: "UniProt"
source_id: "P0A9J6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01987, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbsK b3752 JW3731"
---

# rbsK

`protein.P0A9J6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9J6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01987, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of ribose at O-5 in a reaction requiring ATP and magnesium. The resulting D-ribose-5-phosphate can then be used either for sythesis of nucleotides, histidine, and tryptophan, or as a component of the pentose phosphate pathway. {ECO:0000255|HAMAP-Rule:MF_01987, ECO:0000269|PubMed:11563694, ECO:0000269|PubMed:3011794}. RbsK is a ribokinase that belongs to the ribokinase subfamily of sugar kinases . Crystal structures of ribokinase alone and in ternary complexes have been solved . They suggest an ordered reaction mechanism with a critical role for conformational changes ; monovalent cation binding leads to a conformational change and activation of the enzyme . Ribokinase specifically binds to the α-furanose form of ribose, as shown in the crystal structure and by NMR techniques . The rare codon AGG, encoding the Arg307 and Arg309 residues, together with the inefficient termination codon UGA lead to tagging of 10-25% of newly synthesized molecules of RbsK by the SsrA system . An rbsK mutant can not utilize D-ribose as the sole source of carbon and energy . In an rbsK mutant, D-ribose is able to leak from the cell . The gene was identified by a computational analysis as a candidate for encoding resistance to the antiobiotic CPD0-2068...

## Biological Role

Component of ribokinase (complex.ecocyc.CPLX0-7647).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of ribose at O-5 in a reaction requiring ATP and magnesium. The resulting D-ribose-5-phosphate can then be used either for sythesis of nucleotides, histidine, and tryptophan, or as a component of the pentose phosphate pathway. {ECO:0000255|HAMAP-Rule:MF_01987, ECO:0000269|PubMed:11563694, ECO:0000269|PubMed:3011794}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7647|complex.ecocyc.CPLX0-7647]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3752|gene.b3752]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9J6`
- `KEGG:ecj:JW3731;eco:b3752;ecoc:C3026_20325;`
- `GeneID:93778197;948260;`
- `GO:GO:0004747; GO:0005524; GO:0005829; GO:0019303; GO:0042803; GO:0046872`
- `EC:2.7.1.15`

## Notes

Ribokinase (RK) (EC 2.7.1.15)
