---
entity_id: "protein.P45424"
entity_type: "protein"
name: "nanQ"
source_database: "UniProt"
source_id: "P45424"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:33895133}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanQ yhcH b3221 JW3190"
---

# nanQ

`protein.P45424`

## Static

- Type: `protein`
- Source: `UniProt:P45424`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:33895133}.

## Enriched Summary

FUNCTION: Opens both the alpha- and beta-forms of N-acetylneuraminate (sialic acid; Neu5Ac) to provide aceneuramate, the preferred substrate for NanA. Has preferential activity on the beta-anomer rather than the alpha-anomer. Accelerates a reaction that is spontaneous at slightly alkaline pH, facilitates the reaction at acidic pH. {ECO:0000269|PubMed:33895133}. NanQ catalyzes the conversion of N-acetylneuraminate (Neu5Ac) from its cyclic forms to its linear (aldehydo) form. It preferentially acts on the β anomer, which is also the most prevalent form of Neu5Ac in solution. Addition of NanQ increases the activity of ACNEULY-MONOMER in vitro, suggesting that linear Neu5Ac is not a tightly bound intermediate in the NanQ catalytic cycle . Purified NanQ was found to contain Zn2+. Zn2+ and other divalent cations themselves increase the rate of formation of the linear form of Neu5Ac, albeit at non-physiological concentrations. The Zn2+ contained in NanQ could therefore play a catalytic role . Growth of a nanQ mutant on Neu5Ac as the sole source of carbon at pH 6 and 20°C is delayed compared to wild-type; in a competition assay, the mutant is 6-fold less abundant than wild-type after six cycles of exponential growth . nanQ is not required for growth on N-acetylmannosamine , Neu5Ac or N-glycolylneuraminate under standard growth conditions. NanQ: "N-acetylneuraminate"

## Biological Role

Catalyzes RXN0-7389 (reaction.ecocyc.RXN0-7389). Bound by Zinc cation (molecule.C00038).

## Annotation

FUNCTION: Opens both the alpha- and beta-forms of N-acetylneuraminate (sialic acid; Neu5Ac) to provide aceneuramate, the preferred substrate for NanA. Has preferential activity on the beta-anomer rather than the alpha-anomer. Accelerates a reaction that is spontaneous at slightly alkaline pH, facilitates the reaction at acidic pH. {ECO:0000269|PubMed:33895133}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7389|reaction.ecocyc.RXN0-7389]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3221|gene.b3221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45424`
- `KEGG:ecj:JW3190;eco:b3221;ecoc:C3026_17525;`
- `GeneID:75206071;947750;`
- `GO:GO:0005829; GO:0006974; GO:0008270; GO:0016857; GO:0019262`

## Notes

N-acetylneuraminate anomerase NanQ (N-acetylneuraminate openase)
