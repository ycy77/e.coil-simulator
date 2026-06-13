---
entity_id: "protein.P77439"
entity_type: "protein"
name: "fryA"
source_database: "UniProt"
source_id: "P77439"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fryA ypdD b2383 JW2380"
---

# fryA

`protein.P77439`

## Static

- Type: `protein`
- Source: `UniProt:P77439`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Multifunctional protein that includes general (non sugar-specific) and sugar-specific components of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FryABC PTS system is involved in fructose transport. {ECO:0000305|PubMed:11361063}. fryA is predicted to encode a triphosphoryl transfer protein with the domain order H-I-IIA. fryA encodes a hybrid protein containing an HPr-like domain, an Enzyme I-like domain and an Enzyme IIAFry domain. The EIIA domain of FryA has similarity to the IIA domains of the PTS Enzymes II specific for fructose. FryA is homologous to EG11906-MONOMER "PtsA" throughout its length .

## Biological Role

Component of putative PTS enzyme II FryBCA (complex.ecocyc.CPLX0-8119).

## Annotation

FUNCTION: Multifunctional protein that includes general (non sugar-specific) and sugar-specific components of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FryABC PTS system is involved in fructose transport. {ECO:0000305|PubMed:11361063}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8119|complex.ecocyc.CPLX0-8119]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2383|gene.b2383]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77439`
- `KEGG:ecj:JW2380;eco:b2383;ecoc:C3026_13250;`
- `GeneID:946852;`
- `GO:GO:0005737; GO:0008965; GO:0008982; GO:0009401; GO:0015764; GO:0016020; GO:0016301; GO:0046872`
- `EC:2.7.1.202; 2.7.3.9`

## Notes

Multiphosphoryl transfer protein 1 (MTP 1) (Triphosphoryl transfer protein 1) (TTP 1) [Includes: Phosphoenolpyruvate-protein phosphotransferase (EC 2.7.3.9) (Phosphotransferase system enzyme I); Phosphocarrier protein HPr (Protein H); PTS system fructose-like EIIA component (EC 2.7.1.202) (Fructose-like phosphotransferase enzyme IIA component)]
