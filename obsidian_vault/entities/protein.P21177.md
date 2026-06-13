---
entity_id: "protein.P21177"
entity_type: "protein"
name: "fadB"
source_database: "UniProt"
source_id: "P21177"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadB oldB b3846 JW3822"
---

# fadB

`protein.P21177`

## Static

- Type: `protein`
- Source: `UniProt:P21177`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the aerobic and anaerobic degradation of long-chain fatty acids via beta-oxidation cycle. Catalyzes the formation of 3-oxoacyl-CoA from enoyl-CoA via L-3-hydroxyacyl-CoA. It can also use D-3-hydroxyacyl-CoA and cis-3-enoyl-CoA as substrate. {ECO:0000255|HAMAP-Rule:MF_01621, ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:1748662, ECO:0000269|PubMed:368024, ECO:0000269|PubMed:8454629, ECO:0000269|PubMed:8755745}. FadB is a multifunctional enzyme that is involved in the degradation of fatty acids via the β-oxidation cycle. Four enzymatic activities are associated with FadB: enoyl-CoA hydratase, 3-hydroxyacyl-CoA epimerase, 3-hydroxyacyl-CoA dehydrogenase, and Δ3-cis- Δ2-trans-enoyl-CoA isomerase . The 3-hydroxyacyl-CoA epimerase (EC 5.1.2.3) reaction occurs by a dehydration/hydration mechanism . The enoyl-CoA hydratase (EC 4.2.1.17) and 3-hydroxyacyl-CoA epimerase reactions are catalyzed by the same active site within the N-terminal domain of FadB. A Gly116Phe mutation eliminates both activities . The protonated γ-carboxylate of Glu139 and deprotonated γ-carboxylate of Glu119 provide acid/base functional groups for dehydration. A reaction mechanism was proposed . The L-3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35) activity maps to the C-terminal domain of FadB. A His435Gln mutation specifically eliminates 3-hydroxyacyl-CoA dehydrogenase activity...

## Biological Role

Catalyzes 3-hydroxyisovaleryl-CoA hydro-lyase (reaction.R04137), 3-hydroxypimeloyl-CoA:NAD+ oxidoreductase (reaction.R05305), (S)-3-hydroxyacyl-CoA:NAD+ oxidoreductase (reaction.R06941), (3S)-3-hydroxyacyl-CoA hydro-lyase (reaction.R06942), ENOYL-COA-DELTA-ISOM-RXN (reaction.ecocyc.ENOYL-COA-DELTA-ISOM-RXN), ENOYL-COA-HYDRAT-RXN (reaction.ecocyc.ENOYL-COA-HYDRAT-RXN), OHACYL-COA-DEHYDROG-RXN (reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN), OHBUTYRYL-COA-EPIM-RXN (reaction.ecocyc.OHBUTYRYL-COA-EPIM-RXN), and 15 more. Component of trifunctional fatty acid oxidation complex (complex.ecocyc.FAO-CPLX).

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

FUNCTION: Involved in the aerobic and anaerobic degradation of long-chain fatty acids via beta-oxidation cycle. Catalyzes the formation of 3-oxoacyl-CoA from enoyl-CoA via L-3-hydroxyacyl-CoA. It can also use D-3-hydroxyacyl-CoA and cis-3-enoyl-CoA as substrate. {ECO:0000255|HAMAP-Rule:MF_01621, ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:1748662, ECO:0000269|PubMed:368024, ECO:0000269|PubMed:8454629, ECO:0000269|PubMed:8755745}.

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

## Outgoing Edges (24)

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
- `catalyzes` --> [[reaction.ecocyc.RXN0-5391|reaction.ecocyc.RXN0-5391]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5393|reaction.ecocyc.RXN0-5393]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.FAO-CPLX|complex.ecocyc.FAO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3846|gene.b3846]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21177`
- `KEGG:ecj:JW3822;eco:b3846;ecoc:C3026_20795;`
- `GeneID:948336;`
- `GO:GO:0003857; GO:0004165; GO:0004300; GO:0006635; GO:0008692; GO:0016509; GO:0018812; GO:0036125; GO:0070403`
- `EC:1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8`

## Notes

Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)]
