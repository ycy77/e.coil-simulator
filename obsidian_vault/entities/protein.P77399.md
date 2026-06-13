---
entity_id: "protein.P77399"
entity_type: "protein"
name: "fadJ"
source_database: "UniProt"
source_id: "P77399"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadJ yfcX b2341 JW2338"
---

# fadJ

`protein.P77399`

## Static

- Type: `protein`
- Source: `UniProt:P77399`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the formation of a hydroxyacyl-CoA by addition of water on enoyl-CoA. Also exhibits 3-hydroxyacyl-CoA epimerase and 3-hydroxyacyl-CoA dehydrogenase activities. Strongly involved in the anaerobic degradation of long and medium-chain fatty acids in the presence of nitrate and weakly involved in the aerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12270828, ECO:0000269|PubMed:12535077}. During anaerobic β-oxidation of fatty acids, G7213 FadI, G7212 FadJ, and EG12357 FadK serve functions parallel to those of EG10278 FadA, EG10279 FadB, and EG11530 FadD in the aerobic pathway . FadJ shows sequence similarity to FadB; the enoyl-CoA hydratase, 3-hydroxyacyl-CoA epimerase, and 3-hydroxyacyl-CoA dehydrogenase active site residues appear to be conserved. In a strain engineered for polyhydroxyalkanoate (PHA) production, FadJ is essential for processing of long-chain fatty acids to medium-chain PHA if fadB is absent. Crude cell extracts from a strain that overproduced FadJ contain increased enoyl-CoA hydratase and 3-hydroxyacyl-CoA dehydrogenase activity . FadJ and FadI exhibit partial functional redundancy with FadA and FadB under aerobic conditions; the two complexes are proposed to increase efficiency of β-oxidation by favoring substrates of different chain length...

## Biological Role

Catalyzes 3-hydroxyisovaleryl-CoA hydro-lyase (reaction.R04137), 3-hydroxypimeloyl-CoA:NAD+ oxidoreductase (reaction.R05305), (S)-3-hydroxyacyl-CoA:NAD+ oxidoreductase (reaction.R06941), (3S)-3-hydroxyacyl-CoA hydro-lyase (reaction.R06942), ENOYL-COA-DELTA-ISOM-RXN (reaction.ecocyc.ENOYL-COA-DELTA-ISOM-RXN), ENOYL-COA-HYDRAT-RXN (reaction.ecocyc.ENOYL-COA-HYDRAT-RXN), OHACYL-COA-DEHYDROG-RXN (reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN), OHBUTYRYL-COA-EPIM-RXN (reaction.ecocyc.OHBUTYRYL-COA-EPIM-RXN), and 14 more. Component of anaerobic fatty acid β-oxidation complex (complex.ecocyc.CPLX0-1668).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of a hydroxyacyl-CoA by addition of water on enoyl-CoA. Also exhibits 3-hydroxyacyl-CoA epimerase and 3-hydroxyacyl-CoA dehydrogenase activities. Strongly involved in the anaerobic degradation of long and medium-chain fatty acids in the presence of nitrate and weakly involved in the aerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12270828, ECO:0000269|PubMed:12535077}.

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (23)

- `catalyzes` --> [[reaction.R04137|reaction.R04137]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` --> [[reaction.R05305|reaction.R05305]] `KEGG` `database` - via EC:1.1.1.35
- `catalyzes` --> [[reaction.R06941|reaction.R06941]] `KEGG` `database` - via EC:1.1.1.35
- `catalyzes` --> [[reaction.R06942|reaction.R06942]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` --> [[reaction.ecocyc.ENOYL-COA-DELTA-ISOM-RXN|reaction.ecocyc.ENOYL-COA-DELTA-ISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ENOYL-COA-HYDRAT-RXN|reaction.ecocyc.ENOYL-COA-HYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN|reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.OHBUTYRYL-COA-EPIM-RXN|reaction.ecocyc.OHBUTYRYL-COA-EPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14393|reaction.ecocyc.RXN-14393]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17776|reaction.ecocyc.RXN-17776]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17777|reaction.ecocyc.RXN-17777]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17780|reaction.ecocyc.RXN-17780]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17781|reaction.ecocyc.RXN-17781]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17785|reaction.ecocyc.RXN-17785]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17786|reaction.ecocyc.RXN-17786]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17789|reaction.ecocyc.RXN-17789]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17790|reaction.ecocyc.RXN-17790]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17793|reaction.ecocyc.RXN-17793]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17794|reaction.ecocyc.RXN-17794]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17797|reaction.ecocyc.RXN-17797]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17798|reaction.ecocyc.RXN-17798]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5393|reaction.ecocyc.RXN0-5393]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-1668|complex.ecocyc.CPLX0-1668]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2341|gene.b2341]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77399`
- `KEGG:ecj:JW2338;eco:b2341;ecoc:C3026_13030;`
- `GeneID:949097;`
- `GO:GO:0003857; GO:0004300; GO:0005737; GO:0006635; GO:0008692; GO:0016509; GO:0018812; GO:0036125; GO:0070403`
- `EC:1.1.1.35; 4.2.1.17; 5.1.2.3`

## Notes

Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)]
