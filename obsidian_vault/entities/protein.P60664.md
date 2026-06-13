---
entity_id: "protein.P60664"
entity_type: "protein"
name: "hisF"
source_database: "UniProt"
source_id: "P60664"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisF b2025 JW2007"
---

# hisF

`protein.P60664`

## Static

- Type: `protein`
- Source: `UniProt:P60664`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: IGPS catalyzes the conversion of PRFAR and glutamine to IGP, AICAR and glutamate. The HisF subunit catalyzes the cyclization activity that produces IGP and AICAR from PRFAR using the ammonia provided by the HisH subunit. HisF is the synthase subunit of imidazole glycerol phosphate synthase (HisFH). HisFH catalyzes the fifth step of histidine biosynthesis, as well as generates aminoimidazole carboxamide ribonucleotide, an intermediate in purine nucleotide biosynthesis. The two components of the HisFH dimer work together to catalyze the addition of nitrogen from glutamine to the imidazole ring of phosphoribulosylformimino-AICAR-phosphate to generate aminoimidazole carboxamide ribonucleotide, D-erythro-imidazole-glycerol-phosphate, and glutamate . Although isolated HisH has no activity, isolated HisF catalyzes an ammonia-dependent reaction that uses ammonia as a nitrogen donor in the place of the physiological donor glutamine . The kinetics of HisFH have been modeled . HisFH is a 1:1 dimer of HisF and HisH . The critical residues involved in subunit interaction in general and in the specific case of cooperation of the two active sites have been examined . In vivo interactions between HisF and HisH has been demonstrated...

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256), R12152 (reaction.R12152). Component of imidazole glycerol phosphate synthase (complex.ecocyc.GLUTAMIDOTRANS-CPLX).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: IGPS catalyzes the conversion of PRFAR and glutamine to IGP, AICAR and glutamate. The HisF subunit catalyzes the cyclization activity that produces IGP and AICAR from PRFAR using the ammonia provided by the HisH subunit.

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:4.3.2.10
- `catalyzes` --> [[reaction.R12152|reaction.R12152]] `KEGG` `database` - via EC:4.3.2.10
- `is_component_of` --> [[complex.ecocyc.GLUTAMIDOTRANS-CPLX|complex.ecocyc.GLUTAMIDOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2025|gene.b2025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60664`
- `KEGG:ecj:JW2007;eco:b2025;ecoc:C3026_11415;`
- `GeneID:86946979;946516;`
- `GO:GO:0000105; GO:0000107; GO:0005829; GO:0009382; GO:0016829`
- `EC:4.3.2.10`

## Notes

Imidazole glycerol phosphate synthase subunit HisF (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit HisF) (ImGP synthase subunit HisF) (IGPS subunit HisF)
