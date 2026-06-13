---
entity_id: "protein.P32099"
entity_type: "protein"
name: "lplA"
source_database: "UniProt"
source_id: "P32099"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lplA yjjF b4386 JW4349"
---

# lplA

`protein.P32099`

## Static

- Type: `protein`
- Source: `UniProt:P32099`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes both the ATP-dependent activation of exogenously supplied lipoate to lipoyl-AMP and the transfer of the activated lipoyl onto the lipoyl domains of lipoate-dependent enzymes. Is also able to catalyze very poorly the transfer of lipoyl and octanoyl moiety from their acyl carrier protein. {ECO:0000269|PubMed:7639702}. LplA is a lipoyl-protein ligase . Lipoate modification of the E2 subunits is important for the function of PYRUVATEDEH-CPLX , 2OXOGLUTARATEDEH-CPLX "α-ketoglutarate dehydrogenase" , and the GCVMULTI-CPLX . It was initially thought that LplA only utilizes lipoate imported from outside the cell, in contrast to the other lipoyl-protein ligase, LipB, which utilizes octanoyl-ACP. However, E. coli lipB mutants are able to grow with externally supplied octanoate instead of lipoate. Octanoate growth requires both LplA and CPLX0-782, the enzyme that converts octanoyl side chains to lipoyl side chains, suggesting that LplA attaches octanoate to the E2 domain, and CPLX0-782 converts the octanoate to lipoate . The two-part reaction requires ATP and Mg2+ and proceeds through a lipoyl-AMP intermediate . The conserved Lys133 residue is required for both the lipoate adenylation and the lipoate transfer reaction . LplA can also utilize lipoyl-ACP or octanoyl-ACP, albeit very inefficiently...

## Biological Role

Catalyzes R07770 (reaction.R07770), R07771 (reaction.R07771), RXN-17127 (reaction.ecocyc.RXN-17127), RXN0-1139 (reaction.ecocyc.RXN0-1139), RXN0-1140 (reaction.ecocyc.RXN0-1140), lipoate--GcvH protein ligase (reaction.ecocyc.RXN0-1141), RXN0-5098 (reaction.ecocyc.RXN0-5098). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes both the ATP-dependent activation of exogenously supplied lipoate to lipoyl-AMP and the transfer of the activated lipoyl onto the lipoyl domains of lipoate-dependent enzymes. Is also able to catalyze very poorly the transfer of lipoyl and octanoyl moiety from their acyl carrier protein. {ECO:0000269|PubMed:7639702}.

## Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R07770|reaction.R07770]] `KEGG` `database` - via EC:6.3.1.20
- `catalyzes` --> [[reaction.R07771|reaction.R07771]] `KEGG` `database` - via EC:6.3.1.20
- `catalyzes` --> [[reaction.ecocyc.RXN-17127|reaction.ecocyc.RXN-17127]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1139|reaction.ecocyc.RXN0-1139]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1140|reaction.ecocyc.RXN0-1140]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1141|reaction.ecocyc.RXN0-1141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5098|reaction.ecocyc.RXN0-5098]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4386|gene.b4386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32099`
- `KEGG:ecj:JW4349;eco:b4386;ecoc:C3026_23700;`
- `GeneID:944865;`
- `GO:GO:0005524; GO:0005737; GO:0005829; GO:0009249; GO:0016979; GO:0017118`
- `EC:6.3.1.20`

## Notes

Lipoate-protein ligase A (EC 6.3.1.20) (Lipoate--protein ligase)
