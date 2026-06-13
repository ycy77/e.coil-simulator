---
entity_id: "protein.P69797"
entity_type: "protein"
name: "manX"
source_database: "UniProt"
source_id: "P69797"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119}. Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2999119}; Peripheral membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2999119}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "manX gptB ptsL b1817 JW1806"
---

# manX

`protein.P69797`

## Static

- Type: `protein`
- Source: `UniProt:P69797`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119}. Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2999119}; Peripheral membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2999119}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2681202, ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119, ECO:0000269|PubMed:8262947}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}. The ManX subunit of the mannose PTS permease consists of two domains, IIAman and IIBman, linked by a hinge peptide. Each domain contains a phosphorylation site and phosphoryl transfer occurs between His-10 of IIA and His-175 of IIB . ManX exists as a dimer and is found membrane associated as well as free in the cytoplasm . ManX can be phosphorylated in a phosphoenolpyruvate-dependent reaction and ManX is required for for the phosphorylation of 2-deoxyglucose in vitro . Two forms of a complex between IIA and IIB have been isolated...

## Biological Role

Component of mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165), mannose-specific PTS enzyme IIAB component (complex.ecocyc.CPLX0-7921).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2681202, ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119, ECO:0000269|PubMed:8262947}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7921|complex.ecocyc.CPLX0-7921]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1817|gene.b1817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69797`
- `KEGG:ecj:JW1806;eco:b1817;ecoc:C3026_10350;`
- `GeneID:93776066;946334;`
- `GO:GO:0005737; GO:0005829; GO:0005886; GO:0008982; GO:0009401; GO:0015761; GO:0015764; GO:0016020; GO:0016301; GO:0022870; GO:0042803; GO:0098708; GO:1902495; GO:1990539`
- `EC:2.7.1.191`

## Notes

PTS system mannose-specific EIIAB component (EC 2.7.1.191) (EIIAB-Man) (EIII-Man) [Includes: Mannose-specific phosphotransferase enzyme IIA component (PTS system mannose-specific EIIA component); Mannose-specific phosphotransferase enzyme IIB component (PTS system mannose-specific EIIB component)]
