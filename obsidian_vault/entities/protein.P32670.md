---
entity_id: "protein.P32670"
entity_type: "protein"
name: "ptsA"
source_database: "UniProt"
source_id: "P32670"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptsA frwA yijH b3947 JW5555"
---

# ptsA

`protein.P32670`

## Static

- Type: `protein`
- Source: `UniProt:P32670`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Multifunctional protein that includes general (non sugar-specific) and sugar-specific components of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrwABC PTS system is involved in fructose transport. {ECO:0000305|PubMed:7773398}. Sequence analysis indicates that ptsA encodes a protein with similarity to sugar phosphotransferase system (PTS) components. The 560 residue N-terminal domain is similar to Enzymes I of the PTS and is more similar to Enzyme I's from gram positive bacteria than to Enzyme I's from gram negative bacteria. This domain contains a conserved histidine residue (his301) predicted to be the site of phosphorylation. The C-terminal domain of PtsA has similarity to the IIA domains of the PTS Enzymes II specific for fructose . ptsA is predicted to encode a triphosphoryl transfer protein with the domain order H-I-IIA. ptsA encodes a hybrid protein containing an HPr-like domain, an Enzyme I-like domain and an Enzyme IIAFrw domain. PtsA is homologous to G7246-MONOMER "FryA" throughout its length . Expression of ptsA is induced in cells treated with the supernatant from a stationary phase culture of E. coli .

## Biological Role

Component of putative PTS enzyme II FrwCBDPtsA (complex.ecocyc.CPLX-160).

## Annotation

FUNCTION: Multifunctional protein that includes general (non sugar-specific) and sugar-specific components of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrwABC PTS system is involved in fructose transport. {ECO:0000305|PubMed:7773398}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-160|complex.ecocyc.CPLX-160]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3947|gene.b3947]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32670`
- `KEGG:ecj:JW5555;eco:b3947;ecoc:C3026_21335;`
- `GeneID:948437;`
- `GO:GO:0005737; GO:0008965; GO:0009401; GO:0015764; GO:0016301; GO:0046872; GO:1902495; GO:1990539`
- `EC:2.7.1.202; 2.7.3.9`

## Notes

Multiphosphoryl transfer protein 2 (MTP 2) (Triphosphoryl transfer protein 2) (TTP 2) [Includes: Phosphoenolpyruvate-protein phosphotransferase (EC 2.7.3.9) (Enzyme I-Ani) (Phosphotransferase system enzyme I); Phosphocarrier protein HPr (Protein H); PTS system fructose-like EIIA component (EC 2.7.1.202) (Fructose-like phosphotransferase enzyme IIA component)]
