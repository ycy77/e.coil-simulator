---
entity_id: "protein.P0A6K6"
entity_type: "protein"
name: "deoB"
source_database: "UniProt"
source_id: "P0A6K6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00740, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "deoB drm thyR b4383 JW4346"
---

# deoB

`protein.P0A6K6`

## Static

- Type: `protein`
- Source: `UniProt:P0A6K6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00740, ECO:0000305}.

## Enriched Summary

FUNCTION: Isomerase that catalyzes the conversion of deoxy-ribose 1-phosphate (dRib-1-P) and ribose 1-phosphate (Rib-1-P) to deoxy-ribose 5-phosphate (dRib-5-P) and ribose 5-phosphate (Rib-5-P), respectively. {ECO:0000255|HAMAP-Rule:MF_00740, ECO:0000269|PubMed:1089430, ECO:0000269|PubMed:4992818}. Phosphopentomutase is a catabolic enzyme which catalyzes the transfer of a phosphate group between the C1 and the C5 carbon atoms of ribose and deoxyribose, respectively . A mutation in deoB suppresses the high thymine requirement for growth of thy mutants and improves the survival of thyA mutants in stationary phase . Transposon insertion mutations in deoB suppress the growth defect of a tktA tktB mutant . Deletion of deoB increases glycerol consumption as well as hydrogen and ethanol production compared to wild type , and increases lycopene production in an engineered strain . The deo operon has a complex pattern of regulation . Expression of deoB is downregulated by nitrogen starvation . The E. coli phosphopentomutase appears to be biochemically and structurally distinct from mammalian phosphopentomutase , making it a potential target for antibiotic development. DeoB: "necessary for growth on deoxythymidine or deoxyuridine as the sole source of carbon"

## Biological Role

Catalyzes D-deoxyribose 1,5-phosphomutase (reaction.ecocyc.D-PPENTOMUT-RXN), PPENTOMUT-RXN (reaction.ecocyc.PPENTOMUT-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Isomerase that catalyzes the conversion of deoxy-ribose 1-phosphate (dRib-1-P) and ribose 1-phosphate (Rib-1-P) to deoxy-ribose 5-phosphate (dRib-5-P) and ribose 5-phosphate (Rib-5-P), respectively. {ECO:0000255|HAMAP-Rule:MF_00740, ECO:0000269|PubMed:1089430, ECO:0000269|PubMed:4992818}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PPENTOMUT-RXN|reaction.ecocyc.PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4383|gene.b4383]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6K6`
- `KEGG:ecj:JW4346;eco:b4383;ecoc:C3026_23685;`
- `GeneID:86862497;89519362;948910;`
- `GO:GO:0000287; GO:0005829; GO:0006015; GO:0006018; GO:0006974; GO:0008973; GO:0009264; GO:0030145; GO:0043094`
- `EC:5.4.2.7`

## Notes

Phosphopentomutase (EC 5.4.2.7) (Phosphodeoxyribomutase) (Phosphoribomutase)
