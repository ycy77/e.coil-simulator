---
entity_id: "protein.P25539"
entity_type: "protein"
name: "ribD"
source_database: "UniProt"
source_id: "P25539"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ribD ribG ybaE b0414 JW0404"
---

# ribD

`protein.P25539`

## Static

- Type: `protein`
- Source: `UniProt:P25539`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts 2,5-diamino-6-(ribosylamino)-4(3h)-pyrimidinone 5'-phosphate into 5-amino-6-(ribosylamino)-2,4(1h,3h)-pyrimidinedione 5'-phosphate. {ECO:0000269|PubMed:9068650}. The ribD gene encodes a bifunctional enzyme that catalyzes the second (deamination) and third (reduction) steps in the riboflavin biosynthesis pathway. The N-terminal domain encodes the deaminase activity, and the C-terminal domain encodes the reductase activity . The deaminase domain shows structural similarity to the cytidine deaminase superfamily of enzymes . The kcat of the reduction reaction, 19 min-1, is 20 times slower than the kcat of the deamination reaction, 370 min-1, suggesting that there is no channeling of the substrate and no kinetic coupling between the two active sites . A kinetic mechanism similar to that of dihydrofolate reductase has been proposed . The enzyme is a dimer in solution. Crystal structures of RibD alone and in complex with the oxidized cosubstrate NADP+ or the substrate analog ribose-5-phosphate have been solved . ribD is an essential gene .

## Biological Role

Catalyzes 5-amino-6-(5-phosphoribitylamino)uracil:NADP+ 1'-oxidoreductase (reaction.R03458). Component of fused diaminohydroxyphosphoribosylaminopyrimidine deaminase / 5-amino-6-(5-phosphoribosylamino)uracil reductase (complex.ecocyc.CPLX0-7659).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Converts 2,5-diamino-6-(ribosylamino)-4(3h)-pyrimidinone 5'-phosphate into 5-amino-6-(ribosylamino)-2,4(1h,3h)-pyrimidinedione 5'-phosphate. {ECO:0000269|PubMed:9068650}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03458|reaction.R03458]] `KEGG` `database` - via EC:1.1.1.193
- `is_component_of` --> [[complex.ecocyc.CPLX0-7659|complex.ecocyc.CPLX0-7659]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0414|gene.b0414]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25539`
- `KEGG:ecj:JW0404;eco:b0414;ecoc:C3026_02020;`
- `GeneID:945620;`
- `GO:GO:0008270; GO:0008703; GO:0008835; GO:0009231; GO:0050661`
- `EC:1.1.1.193; 3.5.4.26`

## Notes

Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil reductase (EC 1.1.1.193) (HTP reductase)]
