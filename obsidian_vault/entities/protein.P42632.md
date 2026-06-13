---
entity_id: "protein.P42632"
entity_type: "protein"
name: "tdcE"
source_database: "UniProt"
source_id: "P42632"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcE yhaS b3114 JW5522"
---

# tdcE

`protein.P42632`

## Static

- Type: `protein`
- Source: `UniProt:P42632`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the cleavage of 2-ketobutyrate to propionyl-CoA and formate. It can also use pyruvate as substrate. {ECO:0000269|PubMed:9484901}. The tdcE gene encodes a protein with both 2-oxobutanoate formate-lyase and pyruvate formate-lyase activities that is equally active with both substrates. TdcE is a glycyl radical enzyme, and its activity is dependent on the same PFLACTENZ-MONOMER that is associated with the pflB-encoded pyruvate formate-lyase . The 2-oxobutanoate formate-lyase (KFL) activity is part of an anaerobic pathway for degradation of L-threonine . Overexpression of tdcE can partially complement the growth defect of a pflB mutant under conditions of anaerobic growth on glucose . Expression of the tdcABCDEFG operon is normally under catabolite repression and induced under anaerobic growth conditions in the presence of L-threonine . A tdcE deletion mutant does not have an obvious growth defect ; later it was shown that a transposon insertion in tdcE leads to constitutive SOS expression . TdcE showes 79% identity and 89% overall similarity to PflB over the entire amino acid sequence, although TdcE has an N-terminal extension of four amino acids . Review:

## Biological Role

Catalyzes acetyl-CoA:formate C-acetyltransferase (reaction.R00212), propanoyl-CoA:formate C-propanoyltransferase (reaction.R06987), KETOBUTFORMLY-RXN (reaction.ecocyc.KETOBUTFORMLY-RXN), PYRUVFORMLY-RXN (reaction.ecocyc.PYRUVFORMLY-RXN).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of 2-ketobutyrate to propionyl-CoA and formate. It can also use pyruvate as substrate. {ECO:0000269|PubMed:9484901}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00212|reaction.R00212]] `KEGG` `database` - via EC:2.3.1.54
- `catalyzes` --> [[reaction.R06987|reaction.R06987]] `KEGG` `database` - via EC:2.3.1.54
- `catalyzes` --> [[reaction.ecocyc.KETOBUTFORMLY-RXN|reaction.ecocyc.KETOBUTFORMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRUVFORMLY-RXN|reaction.ecocyc.PYRUVFORMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3114|gene.b3114]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42632`
- `KEGG:ecj:JW5522;eco:b3114;ecoc:C3026_16985;`
- `GeneID:75205077;947623;`
- `GO:GO:0005737; GO:0005829; GO:0005975; GO:0008861; GO:0016020; GO:0043875; GO:0070689`
- `EC:2.3.1.-; 2.3.1.54`

## Notes

PFL-like enzyme TdcE (Keto-acid formate acetyltransferase) (Keto-acid formate-lyase) (Ketobutyrate formate-lyase) (KFL) (EC 2.3.1.-) (Pyruvate formate-lyase) (PFL) (EC 2.3.1.54)
