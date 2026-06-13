---
entity_id: "protein.P69811"
entity_type: "protein"
name: "fruB"
source_database: "UniProt"
source_id: "P69811"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fruB fpr fruF b2169 JW2156"
---

# fruB

`protein.P69811`

## Static

- Type: `protein`
- Source: `UniProt:P69811`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FruAB PTS system is involved in fructose transport. {ECO:0000269|PubMed:3510127, ECO:0000305|PubMed:8013873}. fruB encodes a tridomain protein in which a IIA domain is linked to an HPr-like domain called FPr (fructose-inducible HPr) or H by a central domain (M) of unknown function . Phosphate transfer to fructose by the fructose PTS occurs via the FPr domain of FruB rather than by HPr as is typical for other PTS pathways . Phosphate transfer is predicted to occur from Enzyme I (PtsI) to histidine residue 299 in the FruB H domain to histidine residue 62 in the FruB IIA domain. FruB is also known as the diphosphoryl transfer protein (DTP). A modified form of FruB phosphorylated at histidine residue 299

## Biological Role

Component of fructose-specific PTS enzyme II (complex.ecocyc.CPLX-158).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FruAB PTS system is involved in fructose transport. {ECO:0000269|PubMed:3510127, ECO:0000305|PubMed:8013873}.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-158|complex.ecocyc.CPLX-158]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2169|gene.b2169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69811`
- `KEGG:ecj:JW2156;eco:b2169;`
- `GeneID:75172297;75206422;946677;`
- `GO:GO:0005737; GO:0005886; GO:0009401; GO:0016301; GO:0022877; GO:0090563; GO:1902495; GO:1990539`

## Notes

Multiphosphoryl transfer protein (MTP) (Diphosphoryl transfer protein) (DTP) (Phosphotransferase FPr protein) (Pseudo-HPr) [Includes: Phosphocarrier protein HPr (Protein H); PTS system fructose-specific EIIA component (EIIA-Fru) (EIII-Fru) (Fructose-specific phosphotransferase enzyme IIA component)]
