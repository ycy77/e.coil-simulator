---
entity_id: "protein.P37306"
entity_type: "protein"
name: "allK"
source_database: "UniProt"
source_id: "P37306"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allK arcC ybcF b0521 JW0510"
---

# allK

`protein.P37306`

## Static

- Type: `protein`
- Source: `UniProt:P37306`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Kinase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:36384810). Catalyzes the transfer of a phosphate group from carbamoyl phosphate to ADP to produce ATP and leave carbamate, which spontaneously hydrolyzes to ammonia and hydrogencarbonate (PubMed:36384810). {ECO:0000269|PubMed:36384810}. This gene is the last gene within the TU0-12962 operon whose first three genes encode subunits of the CPLX0-12207 complex . Using sequence orthology and genome and metabolic context methods, ybcF is predicted to encode the catabolic carbamate kinase activity of the anaerobic allantoin degradation pathway . Using both inactivation and overexpression mutants, and purified AllK in vitro, the carbamate kinase activity was verified in anaerobic conditions with allantoin as the sole nitrogen source. This activity is also referred to as oxamic transcarbamylase (OXTCase) .

## Biological Role

Catalyzes ATP:carbamate phosphotransferase (reaction.R00150), CARBAMATE-KINASE-RXN (reaction.ecocyc.CARBAMATE-KINASE-RXN).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Kinase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:36384810). Catalyzes the transfer of a phosphate group from carbamoyl phosphate to ADP to produce ATP and leave carbamate, which spontaneously hydrolyzes to ammonia and hydrogencarbonate (PubMed:36384810). {ECO:0000269|PubMed:36384810}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00150|reaction.R00150]] `KEGG` `database` - via EC:2.7.2.2
- `catalyzes` --> [[reaction.ecocyc.CARBAMATE-KINASE-RXN|reaction.ecocyc.CARBAMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0521|gene.b0521]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37306`
- `KEGG:ecj:JW0510;eco:b0521;ecoc:C3026_02555;`
- `GeneID:944972;`
- `GO:GO:0000256; GO:0005524; GO:0005829; GO:0008804; GO:0019546`
- `EC:2.7.2.2`

## Notes

Carbamate kinase (EC 2.7.2.2) (Catabolic carbamate kinase) (Catabolic CK)
