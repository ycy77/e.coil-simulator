---
entity_id: "protein.P0ABU5"
entity_type: "protein"
name: "elbB"
source_database: "UniProt"
source_id: "P0ABU5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "elbB elb2 yzzB b3209 JW3176"
---

# elbB

`protein.P0ABU5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABU5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Displays glyoxalase activity, catalyzing the conversion of glyoxal to glycolate (PubMed:26678554). However, this apparent glyoxalase activity may reflect a protein deglycase activity, which could be the primary function of this protein like other DJ-1 superfamily members such as PARK7, YajL, YhbO and HchA (Probable). Is not able to use methylglyoxal as substrate (PubMed:26678554). {ECO:0000269|PubMed:26678554, ECO:0000305}. ElbB belongs to the DJ-1/ThiJ/PfpI superfamily of proteins . A crystal structure has been solved at 1.65 Å resolution , and the predicted functional site somewhat resembles that of the human protein DJ-1 . The protein exhibits low glyoxalase activity with glyoxal, but not methylglyoxal, as the substrate . The ElbB protein cross-reacts with an antibody prepared against a peptide of the 2.2 region of σ70 and σ32 and was therefore originally named sigma cross-reacting protein 27A (SCRP-27A) . elbB was identified in a mutant screen designed to identify genes involved in the biosynthesis of isopentenyl diphosphate, a precursor of isoprenoids . Overexpression of elbB from a high-copy number plasmid improves lycopene production in an engineered strain . Increased expression of elbB does not lead to increased resistance to glyoxal, but may lead to a decrease in carboxymethylated proteins in glyoxal-treated cells . ElbB: "enhancing lycopene biosynthesis"

## Biological Role

Catalyzes RXN0-7173 (reaction.ecocyc.RXN0-7173).

## Annotation

FUNCTION: Displays glyoxalase activity, catalyzing the conversion of glyoxal to glycolate (PubMed:26678554). However, this apparent glyoxalase activity may reflect a protein deglycase activity, which could be the primary function of this protein like other DJ-1 superfamily members such as PARK7, YajL, YhbO and HchA (Probable). Is not able to use methylglyoxal as substrate (PubMed:26678554). {ECO:0000269|PubMed:26678554, ECO:0000305}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7173|reaction.ecocyc.RXN0-7173]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3209|gene.b3209]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABU5`
- `KEGG:ecj:JW3176;eco:b3209;ecoc:C3026_17460;`
- `GeneID:947903;`
- `GO:GO:0005829; GO:0008299; GO:0016829; GO:0045828`
- `EC:4.2.1.-`

## Notes

Glyoxalase ElbB (EC 4.2.1.-) (Sigma cross-reacting protein 27A) (SCRP-27A)
