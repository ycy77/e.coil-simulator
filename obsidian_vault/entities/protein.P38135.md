---
entity_id: "protein.P38135"
entity_type: "protein"
name: "fadK"
source_database: "UniProt"
source_id: "P38135"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein. Note=Partially membrane-associated. {ECO:0000305|PubMed:15213221}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadK ydiD b1701 JW5910"
---

# fadK

`protein.P38135`

## Static

- Type: `protein`
- Source: `UniProt:P38135`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein. Note=Partially membrane-associated. {ECO:0000305|PubMed:15213221}.

## Enriched Summary

FUNCTION: Catalyzes the esterification, concomitant with transport, of exogenous fatty acids into metabolically active CoA thioesters for subsequent degradation or incorporation into phospholipids. Is maximally active on C6:0, C8:0 and C12:0 fatty acids, while has a low activity on C14-C18 chain length fatty acids (PubMed:15213221, PubMed:19477415). Is involved in the anaerobic beta-oxidative degradation of fatty acids, which allows anaerobic growth of E.coli on fatty acids as a sole carbon and energy source in the presence of nitrate or fumarate as a terminal electron acceptor (PubMed:12535077). Can functionally replace FadD under anaerobic conditions (PubMed:12535077). {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:15213221, ECO:0000269|PubMed:19477415}. FadK is an acyl-CoA synthetase that is primarily active on medium-chain (C6:0 and C8:0) fatty acids and acts in anaerobic β-oxidation of fatty acids . During anaerobic β-oxidation of fatty acids, G7213 FadI, G7212 FadJ, and EG12357 FadK serve functions parallel to those of EG10278 FadA, EG10279 FadB, and EG11530 FadD in the aerobic pathway . FadK has a FACS (fatty acyl-CoA-binding) motif and an ATP/AMP binding motif . Based on sequence similarity, FadK has been predicted to be a hydroxycinnamate-CoA ligase...

## Biological Role

Catalyzes RXN-19959 (reaction.ecocyc.RXN-19959), RXN0-7238 (reaction.ecocyc.RXN0-7238), RXN0-7239 (reaction.ecocyc.RXN0-7239), RXN0-7248 (reaction.ecocyc.RXN0-7248), TRANS-RXN0-623 (reaction.ecocyc.TRANS-RXN0-623). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Catalyzes the esterification, concomitant with transport, of exogenous fatty acids into metabolically active CoA thioesters for subsequent degradation or incorporation into phospholipids. Is maximally active on C6:0, C8:0 and C12:0 fatty acids, while has a low activity on C14-C18 chain length fatty acids (PubMed:15213221, PubMed:19477415). Is involved in the anaerobic beta-oxidative degradation of fatty acids, which allows anaerobic growth of E.coli on fatty acids as a sole carbon and energy source in the presence of nitrate or fumarate as a terminal electron acceptor (PubMed:12535077). Can functionally replace FadD under anaerobic conditions (PubMed:12535077). {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:15213221, ECO:0000269|PubMed:19477415}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-19959|reaction.ecocyc.RXN-19959]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7238|reaction.ecocyc.RXN0-7238]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7239|reaction.ecocyc.RXN0-7239]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7248|reaction.ecocyc.RXN0-7248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-623|reaction.ecocyc.TRANS-RXN0-623]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1701|gene.b1701]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38135`
- `KEGG:ecj:JW5910;eco:b1701;`
- `GeneID:946213;`
- `GO:GO:0005524; GO:0005886; GO:0006635; GO:0019395; GO:0031956`
- `EC:6.2.1.-`

## Notes

Medium-chain fatty-acid--CoA ligase (EC 6.2.1.-) (Acyl-CoA synthetase) (ACS) (Fatty acyl-CoA synthetase FadK)
