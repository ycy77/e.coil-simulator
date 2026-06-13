---
entity_id: "protein.P0ABT5"
entity_type: "protein"
name: "dusB"
source_database: "UniProt"
source_id: "P0ABT5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dusB yhdG b3260 JW3228"
---

# dusB

`protein.P0ABT5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABT5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. {ECO:0000255|HAMAP-Rule:MF_02042, ECO:0000269|PubMed:11983710}. DusB and EG12022-MONOMER (DusC) together account for about half of the 5,6-dihydrouridine modification observed in wild-type cellular tRNA, and EG11932-MONOMER (DusA) accounts for the other half . Crystal structure of DusB in complex with a tRNA transcript was obtained showing conservation the Dus fold. Despite some structural similarities DusB was found to have a new uridine binding mechanism not seen previously in the Dus family proteins . A dusA dusB dusC triple mutant exhibits a complete lack of 5,6-dihydrouridine modification in cellular tRNA, whereas each single mutant exhibits a partial reduction, compared to wild type . Using a ΔdusB mutant, the specificity of DusB for dihydrouridylation of nucleotide 17 (D17) was determined in ARG-tRNAs (ICG), ILE-tRNAs (GAU) and LEU-tRNAs (CAG) . Follow-up experiments with the Δ3 mutant found that mRNAs are not dihydrouridylated and that the dihydrouridine nucleotide in 23S rRNA is dihydrouridylated by some other dihydrouridine synthase than DusA, DusB or DusC...

## Biological Role

Catalyzes dihydrouridine synthase (reaction.ecocyc.RXN0-1281).

## Annotation

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. {ECO:0000255|HAMAP-Rule:MF_02042, ECO:0000269|PubMed:11983710}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1281|reaction.ecocyc.RXN0-1281]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3260|gene.b3260]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABT5`
- `KEGG:ecj:JW3228;eco:b3260;ecoc:C3026_17735;`
- `GeneID:86862342;93778727;947707;`
- `GO:GO:0000049; GO:0002943; GO:0009314; GO:0010181; GO:0017150; GO:0050660; GO:0071461`
- `EC:1.3.1.-`

## Notes

tRNA-dihydrouridine synthase B (EC 1.3.1.-)
